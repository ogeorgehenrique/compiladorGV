from antlr4 import *
from CompiladorGVLexer import CompiladorGVLexer
import sys

def main(argv):
    if len(argv) < 2:
        print("Uso: python scanner.py <caminho_do_arquivo>")
        return

    input_file = argv[1]
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = CompiladorGVLexer(input_stream)

    token = lexer.nextToken()
    print("-" * 33)
    print(f"{'Tipo||':<5} {'Lexema||':<5} {'Linha||':<5} {'Coluna||'}")
    print("-" * 33)

    try:
        while token.type != Token.EOF:
            tipo_token = lexer.symbolicNames[token.type]
            lexema = token.text
            linha = token.line
            coluna = token.column + 1

            print(f"<{tipo_token}, '{lexema}', {linha}, {coluna}>")

            token = lexer.nextToken()
    except Exception as e:
        print(str(e))
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)