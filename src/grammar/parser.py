from antlr4 import *
from CompiladorGVLexer import CompiladorGVLexer
from CompiladorGVParser import CompiladorGVParser
import sys
from antlr4.error.ErrorListener import ErrorListener

class MeuErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg}")

def main(argv):
    if len(argv) < 2:
        print("Uso: python parser.py <caminho_do_arquivo>")
        return

    input_file = argv[1]
    input_stream = FileStream(input_file, encoding="utf-8")
    
    lexer = CompiladorGVLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CompiladorGVParser(token_stream)

    # Remove os listeners padrões do ANTLR
    parser.removeErrorListeners()

    # Adiciona nosso listener personalizado
    parser.addErrorListener(MeuErrorListener())

    try:
        # Tentamos começar pelo símbolo inicial da sua gramática
        parser.inicio()
        print("\nPrograma analisado com sucesso! ✅\n")
    except Exception as e:
        print(f"Erro durante a análise: {e}")

if __name__ == '__main__':
    main(sys.argv)