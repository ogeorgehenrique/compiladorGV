import sys
import os
import json
from antlr4 import *

import TACGenerator



# Adiciona src/grammar ao path para que os módulos possam ser importados
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'grammar'))

from CompiladorGVLexer import CompiladorGVLexer
from CompiladorGVParser import CompiladorGVParser
# from CompiladorGVVisitor import CompiladorGVVisitor
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
    try:
        # 🔹 Lexer e Parser
        input_stream = InputStream(code)
        lexer = CompiladorGVLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CompiladorGVParser(stream)

        print("🧩 Etapa 1: Análise sintática...")
        tree = parser.inicio()

        # 🔹 AST Builder
        print("🌲 Etapa 2: Construindo AST...")
        builder = ASTBuilderVisitor()
        ast = builder.visit(tree)
        print(json.dumps(ast, indent=2, ensure_ascii=False))


        # 🔹 Análise semântica
        print("🧠 Etapa 3: Análise semântica...")
        analyzer = SemanticAnalyzer()
        analyzer.analyze(ast)
        # Exibir erros, se houver
        if analyzer.errors:
            print("❌ Erros semânticos encontrados:")
            for erro in analyzer.errors:
                print(f"   - {erro}")
        else:
            print("✅ Análise semântica concluída sem erros.")

        if "--gerar-tac" in argv:
                print("\n🚧 Etapa 4: Geração de Código Intermediário (TAC)")
                tacgen = TACGenerator()
                tacgen.visit(tree)
                tacgen.salvar_em_arquivo("saida.tac")
                print("✅ Código TAC gerado em 'saida.tac'")

    except Exception as e:
        print(f"\033[91mErro durante a análise: {e}\033[0m")
        sys.exit(1)





if __name__ == "__main__":
    main()
