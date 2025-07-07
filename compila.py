# import sys
# import os
# import json
# from antlr4 import *

# # Adiciona src/grammar ao path
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'grammar'))

# from CompiladorGVLexer import CompiladorGVLexer
# from CompiladorGVParser import CompiladorGVParser
# from MyParserErrorListener import MyParserErrorListener
# from ParseTreeGenerator import ParseTreeGenerator
# from ASTBuilderVisitor import ASTBuilderVisitor
# from SemanticAnalyzer import SemanticAnalyzer


# def executar_scanner(input_stream):
#     lexer = CompiladorGVLexer(input_stream)
#     print("-" * 40)
#     print(f"{'Tipo':<10} {'Lexema':<15} {'Linha':<6} {'Coluna'}")
#     print("-" * 40)

#     try:
#         token = lexer.nextToken()
#         while token.type != Token.EOF:
#             tipo_token = lexer.symbolicNames[token.type]
#             lexema = token.text
#             linha = token.line
#             coluna = token.column + 1
#             print(f"{tipo_token:<10} '{lexema}'{' ' * (14 - len(lexema))} {linha:<6} {coluna}")
#             token = lexer.nextToken()
#     except Exception as e:
#         print(str(e))
#         sys.exit(1)


# def executar_parser(input_stream):
#     lexer = CompiladorGVLexer(input_stream)
#     tokens = CommonTokenStream(lexer)
#     parser = CompiladorGVParser(tokens)

#     parser.removeErrorListeners()
#     parser.addErrorListener(MyParserErrorListener())

#     try:
#         tree = parser.inicio()
#         visitor = ParseTreeGenerator()
#         visitor.visit(tree)

#         with open("saida_ast.dot", "w") as f:
#             f.write("digraph AST {\n")
#             f.write("\n".join(visitor.output))
#             f.write("\n}")
#         print("✅ Árvore Sintática gerada em 'saida_ast.dot'")
#         return tree
#     except Exception as e:
#         print(f"\033[91mErro durante a análise sintática: {e}\033[0m")
#         sys.exit(1)


# def executar_semantico(tree):
#     print("🌲 Etapa 3: Construindo AST...")
#     builder = ASTBuilderVisitor()
#     ast = builder.visit(tree)
#     print(json.dumps(ast, indent=2, ensure_ascii=False))

#     print("🧠 Etapa 4: Análise semântica...")
#     analyzer = SemanticAnalyzer()
#     analyzer.analyze(ast)

#     if analyzer.errors:
#         print("❌ Erros semânticos encontrados:")
#         for erro in analyzer.errors:
#             print(f"   - {erro}")
#     else:
#         print("✅ Análise semântica concluída sem erros.")


# def main():
#     if len(sys.argv) < 2:
#         print("Uso: python compilador.py <arquivo_fonte.gv>")
#         return

#     input_file = sys.argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")

#     print("🔍 Etapa 1: Scanner - Análise Léxica")
#     executar_scanner(input_stream)

#     print("\n🧠 Etapa 2: Parser - Análise Sintática")
#     input_stream = FileStream(input_file, encoding="utf-8")
#     tree = executar_parser(input_stream)

#     print("\n🧠 Etapa 3: Análise Semântica")
#     executar_semantico(tree)


# if __name__ == '__main__':
#     main()




import sys
import os
import json
from antlr4 import *



# # Adiciona src/grammar ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'grammar'))
from antlr4 import *
from CompiladorGVLexer import CompiladorGVLexer
from CompiladorGVParser import CompiladorGVParser
from MyParserErrorListener import MyParserErrorListener
from ParseTreeGenerator import ParseTreeGenerator
from ASTBuilderVisitor import ASTBuilderVisitor
from SemanticAnalyzer import SemanticAnalyzer
import sys


# import TACGenerator
from TACGenerator import TACGenerator

# import LLVMGenerator

from LLVMGenerator import LLVMGenerator
from TACParser import carregar_tac_de_arquivo 

# compilar o codigo final 

import subprocess


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
        print("Nenhum erro Detectado ✅")
        print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
    except Exception as e:
        print(f"\033[91mErro durante a análise: {e}\033[0m")
        sys.exit(1)

def executar_semantico():
    #japa implementacao
    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as file:
        code = file.read()


    input_stream = InputStream(code)
    lexer = CompiladorGVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiladorGVParser(stream)

    tree = parser.inicio()
    # 🔹 AST Builder
    print("🌲 Construindo AST...")
    builder = ASTBuilderVisitor()
    ast = builder.visit(tree)
    print(json.dumps(ast, indent=2, ensure_ascii=False)) 

    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)
    # Exibir erros, se houver
    if analyzer.errors:
        print("❌ Erros semânticos encontrados:")
        for erro in analyzer.errors:
            print(f"\033[91mErro durante a análise: {erro}\033[0m")
            sys.exit(1)
    else:
        print("✅ Análise semântica concluída sem erros.")   


def executar_tac():
    input_stream = FileStream(sys.argv[1], encoding='utf-8')    #Lê o conteúdo do arquivo-fonte informado via terminal como um stream de texto.
    lexer = CompiladorGVLexer(input_stream)                 #Usa o lexer para gerar tokens a partir do conteúdo do arquivo.
    tokens = CommonTokenStream(lexer)                       #Esses tokens são agrupados em um CommonTokenStream, necessário para o parser funcionar corretamente.
    parser = CompiladorGVParser(tokens)                    #Cria uma instância do parser e alimenta com os tokens para iniciar a análise sintática.
   
    parser.removeErrorListeners()
    parser.addErrorListener(MyParserErrorListener())
    

    if "--gerar-tac" in sys.argv:
        # print("🚧 Etapa 4: Geração de Código Intermediário (TAC)")
        tree = parser.inicio()
        tacgen = TACGenerator()
        tacgen.visit(tree)
        tacgen.salvar_em_arquivo("saida.tac")
        print("✅ Código TAC gerado em 'saida.tac'")

    # try:
    #     tree = parser.inicio()  #Tenta executar a análise sintática chamando a regra inicial da gramática (inicio). O retorno é a árvore sintática (parse tree).
    #     visitor = ParseTreeGenerator()
    #     visitor.visit(tree)

    #     #Cria um arquivo no formato DOT, que representa graficamente a árvore gerada (AST).
    #     with open("saida_ast.dot", "w") as f:
    #         f.write("digraph AST {\n")
    #         f.write("\n".join(visitor.output))
    #         f.write("\n}")
    #     print("Programa analisado com sucesso! ✅")
    #     print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
    # except Exception as e:
    #     print(f"\033[91mErro durante a análise: {e}\033[0m")
    #     sys.exit(1)


def executarLLVMGenerator():
    with open("saida.tac", "r") as f:
        tac_instrs = carregar_tac_de_arquivo(f.read())
    
    llvm_gen = LLVMGenerator(tac_instrs)
    llvm_ir = llvm_gen.gerar()

    with open("main.ll", "w") as f:
        f.write(llvm_ir)
    
    print("✅ LLVM IR gerado em 'main.ll'")

import subprocess
import platform
import os

def compilar_e_rodar_llvm():
    sistema = platform.system()

    # Compilar o LLVM IR
    subprocess.run(["clang", "main.ll", "-o", "main.exe" if sistema == "Windows" else "main"], check=True)
    
    # Rodar o executável
    if sistema == "Windows":
        resultado = subprocess.run(["main.exe"], capture_output=True, text=True)
    else:
        # Garante permissão de execução em Unix
        os.chmod("main", 0o755)
        resultado = subprocess.run(["./main"], capture_output=True, text=True)

    print("Saída do programa: \n")
    print(resultado.stdout)


def main(argv):
    if len(argv) < 2:
        print("Uso: python compila.py <arquivo_fonte>")
        return

    input_file = argv[1]
    # input_stream = FileStream(input_file, encoding="utf-8")
    

    print("\n🔍 Etapa 1: Scanner - Analisador Léxico")
    print("")
    executar_scanner(FileStream(input_file, encoding="utf-8"))

    print("\n🧠 Etapa 2: Parser - Analisador Sintático")
    print("")
    executar_parser(FileStream(input_file, encoding="utf-8"))

    print("\n🧩 Etapa 3:  - Analisador Semántico")
    print("")
    executar_semantico()
    
    print("\n🚧  Etapa 4:  - Geração de Código Intermediário (TAC)")
    print("")
    executar_tac()

    print("\nEtapa 5: - Geração de Código llvm")
    print("")
    executarLLVMGenerator()

    print("\nEtapa 6: - Compila o codigo .ll")
    print("")
    compilar_e_rodar_llvm()

if __name__ == '__main__':
    main(sys.argv)