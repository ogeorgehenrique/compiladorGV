import sys
import os
import json
from antlr4 import *

from src.grammar.MyParserErrorListener import MyParserErrorListener
from src.grammar.ParseTreeGenerator import ParseTreeGenerator


# Adiciona src/grammar ao path para que os módulos possam ser importados
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'grammar'))

from CompiladorGVLexer import CompiladorGVLexer
from CompiladorGVParser import CompiladorGVParser
from ASTBuilderVisitor import ASTBuilderVisitor
from SemanticAnalyzer import SemanticAnalyzer

def main():
    # 🔹 Lê o arquivo de entrada
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.gv>")
        return

    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as file:
        code = file.read()

    # 🔹 Lexer e Parser
    input_stream = InputStream(code)
    lexer = CompiladorGVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiladorGVParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(MyParserErrorListener())
    print("#" * 80)
    print("Etapa 1: Análise sintática...")
    print("")
    try:
        tree = parser.inicio()  
        visitor = ParseTreeGenerator()
        visitor.visit(tree)

        
        with open("saida_ast.dot", "w") as f:
            f.write("digraph AST {\n")
            f.write("\n".join(visitor.output))
            f.write("\n}")
        print("Programa analisado com sucesso! ✅")
        print("")
        print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
    except Exception as e:
        print(f"\033[91mErro durante a análise: {e}\033[0m")
        sys.exit(1)

    # 🔹 AST Builder
    print("#" * 80)
    print("Etapa 2: Construindo AST...")
    print("")
    builder = ASTBuilderVisitor()
    ast = builder.visit(tree)
    print(json.dumps(ast, indent=2, ensure_ascii=False))


    # 🔹 Análise semântica
    print("#" * 80)
    print("Etapa 3: Análise semântica...")
    print("")
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)
    # Exibir erros, se houver
    if analyzer.errors:
        print("❌ Erros semânticos encontrados:")
        for erro in analyzer.errors:
            print(f"{erro}")
    else:
        print("✅ Análise semântica concluída sem erros.")




if __name__ == "__main__":
    main()
