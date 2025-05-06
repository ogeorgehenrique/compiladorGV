from antlr4 import *
from CompiladorGVLexer import CompiladorGVLexer
from CompiladorGVParser import CompiladorGVParser
from MyParserErrorListener import MyParserErrorListener
from ParseTreeGenerator import ParseTreeGenerator
import sys

def executar_scanner(input_stream):
    lexer = CompiladorGVLexer(input_stream)
    print("-" * 33)
    print(f"{'Tipo||':<5} {'Lexema||':<5} {'Linha||':<5} {'Coluna||'}")
    print("-" * 33)

    try:
        token = lexer.nextToken()
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

def executar_parser(input_stream):
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

def main(argv):
    if len(argv) < 2:
        print("Uso: python executar_compilador.py <arquivo_fonte>")
        return

    input_file = argv[1]
    input_stream = FileStream(input_file, encoding="utf-8")

    print("\n🔍 Etapa 1: Scanner - Analisador Léxico")
    print("")
    executar_scanner(FileStream(input_file, encoding="utf-8"))

    print("\n🧠 Etapa 2: Parser - Analisador Sintático")
    print("")
    executar_parser(FileStream(input_file, encoding="utf-8"))

if __name__ == '__main__':
    main(sys.argv)