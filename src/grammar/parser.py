from antlr4 import *                                        
from CompiladorGVLexer import CompiladorGVLexer             
from CompiladorGVParser import CompiladorGVParser           
from MyParserErrorListener import MyParserErrorListener     
from ParseTreeGenerator import ParseTreeGenerator           
import sys

def main(argv):
    if len(argv) < 2:
        print("Uso: python parser.py <arquivo_fonte>")
        return

    input_stream = FileStream(argv[1], encoding='utf-8')    
    lexer = CompiladorGVLexer(input_stream)                 
    tokens = CommonTokenStream(lexer)                       
    parser = CompiladorGVParser(tokens)                     


    parser.removeErrorListeners()
    parser.addErrorListener(MyParserErrorListener())

    try:
        tree = parser.inicio()  
        visitor = ParseTreeGenerator()
        visitor.visit(tree)

        
        with open("saida_ast.dot", "w") as f:
            f.write("digraph AST {\n")
            f.write("\n".join(visitor.output))
            f.write("\n}")
        print("Programa analisado com sucesso! ✅")
        print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
    except Exception as e:
        print(f"\033[91mErro durante a análise: {e}\033[0m")
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv) # type: ignore