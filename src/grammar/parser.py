# from antlr4 import *
# from CompiladorGVLexer import CompiladorGVLexer
# from CompiladorGVParser import CompiladorGVParser
# import sys
# from antlr4.error.ErrorListener import ErrorListener

# class MeuErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         print(f"ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg}")

# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python parser.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")
    
#     lexer = CompiladorGVLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = CompiladorGVParser(token_stream)

#     # Remove os listeners padrões do ANTLR
#     parser.removeErrorListeners()

#     # Adiciona nosso listener personalizado
#     parser.addErrorListener(MeuErrorListener())

#     try:
#         # Tentamos começar pelo símbolo inicial da sua gramática
#         parser.inicio()
#         print("\nPrograma analisado com sucesso! ✅\n")
#     except Exception as e:
#         print(f"Erro durante a análise: {e}")

# if __name__ == '__main__':
#     main(sys.argv)

## funcao antiga que gera uma arvore AST simples         
# from antlr4 import *
# from antlr4.error.ErrorListener import ErrorListener
# from CompiladorGVLexer import CompiladorGVLexer
# from CompiladorGVParser import CompiladorGVParser
# from ASTGeneratorVisitor import ASTGeneratorVisitor
# import sys

# class MeuErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         print(f"ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg}")

# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python parser.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")

#     lexer = CompiladorGVLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = CompiladorGVParser(token_stream)

#     parser.removeErrorListeners()
#     parser.addErrorListener(MeuErrorListener())

#     try:
#         tree = parser.inicio()

#         print("\nPrograma analisado com sucesso! ✅\n")

#         # Agora gerar o DOT
#         visitor = ASTGeneratorVisitor()
#         visitor.visit(tree)

#         with open("saida_ast.dot", "w") as f:
#             f.write("digraph AST {\n")
#             f.write("\n".join(visitor.output))
#             f.write("\n}")
        
#         print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
#     except Exception as e:
#         print(f"Erro durante a análise: {e}")

# if __name__ == '__main__':
#     main(sys.argv)    



# from antlr4 import *
# from MyParserErrorListener import MyParserErrorListener
# from antlr4.error.ErrorListener import ErrorListener
# from CompiladorGVLexer import CompiladorGVLexer
# from CompiladorGVParser import CompiladorGVParser
# from ParseTreeGenerator import ParseTreeGenerator
# import sys

# class MeuErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         print(f"ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg}")

# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python parser.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")

#     lexer = CompiladorGVLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     parser = CompiladorGVParser(token_stream)
#     parser.removeErrorListeners()
#     parser.addErrorListener(MyParserErrorListener())

#     parser.removeErrorListeners()
#     parser.addErrorListener(MeuErrorListener())

#     try:
#         tree = parser.inicio()

#         print("\nPrograma analisado com sucesso! ✅\n")

#         # Agora gerar o DOT
#         visitor = ParseTreeGenerator()
#         visitor.visit(tree)

#         with open("saida_ast.dot", "w") as f:
#             f.write("digraph AST {\n")
#             f.write("\n".join(visitor.output))
#             f.write("\n}")
        
#         print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
#     except Exception as e:
#         print(f"Erro durante a análise: {e}")

# if __name__ == '__main__':
#     main(sys.argv)    

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

    # Remove o listener padrão e adiciona o personalizado
    parser.removeErrorListeners()
    parser.addErrorListener(MyParserErrorListener())

    try:
        tree = parser.inicio()  # ou sua regra inicial
        visitor = ParseTreeGenerator()
        visitor.visit(tree)

        with open("saida_ast.dot", "w") as f:
            f.write("digraph AST {\n")
            f.write("\n".join(visitor.output))
            f.write("\n}")
        print("")    
        print("Programa analisado com sucesso! ✅")
    except Exception as e:
        print("Erro durante a análise:", e)

if __name__ == '__main__':
    main(sys.argv)