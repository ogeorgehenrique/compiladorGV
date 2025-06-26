# from antlr4 import *                                        #importa todos os utilitários da biblioteca ANTLR4
# from CompiladorGVLexer import CompiladorGVLexer             #Importa a classe léxica gerada automaticamente pelo ANTLR a partir da gramática .g4. Essa classe é usada para converter o código-fonte em tokens.
# from CompiladorGVParser import CompiladorGVParser           #importa a classe do parser gerado pelo ANTLR. Essa classe define as regras de análise sintática da linguagem.
# from MyParserErrorListener import MyParserErrorListener     #importa uma classe personalizada que estende o comportamento padrão de tratamento de erros do ANTLR, permitindo exibir mensagens de erro sintático mais claras e customizadas.
# from ParseTreeGenerator import ParseTreeGenerator           #Importa uma classe visitante personalizada usada para percorrer a árvore sintática gerada e montar sua representação visual (AST).
# import sys


# #Define a função principal que será executada com os argumentos da linha de comando.
# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python parser.py <arquivo_fonte>")
#         return

#     input_stream = FileStream(argv[1], encoding='utf-8')    #Lê o conteúdo do arquivo-fonte informado via terminal como um stream de texto.
#     lexer = CompiladorGVLexer(input_stream)                 #Usa o lexer para gerar tokens a partir do conteúdo do arquivo.
#     tokens = CommonTokenStream(lexer)                       #Esses tokens são agrupados em um CommonTokenStream, necessário para o parser funcionar corretamente.
#     parser = CompiladorGVParser(tokens)                     #Cria uma instância do parser e alimenta com os tokens para iniciar a análise sintática.


#     #Remove os tratadores de erro padrão do ANTLR e adiciona o personalizado 
#     parser.removeErrorListeners()
#     parser.addErrorListener(MyParserErrorListener())

    

#     # Gerar TAC se ativado
#     if "--gerar-tac" in argv:
#         print("🚧 Etapa 4: Geração de Código Intermediário (TAC)")
#         tacgen = TACGenerator()
#         tacgen.visit(tree)
#         tacgen.salvar_em_arquivo("saida.tac")
#         print("✅ Código TAC gerado em 'saida.tac'")

#     try:
#         tree = parser.inicio()  #Tenta executar a análise sintática chamando a regra inicial da gramática (inicio). O retorno é a árvore sintática (parse tree).
#         visitor = ParseTreeGenerator()
#         visitor.visit(tree)

#         #Cria um arquivo no formato DOT, que representa graficamente a árvore gerada (AST).
#         with open("saida_ast.dot", "w") as f:
#             f.write("digraph AST {\n")
#             f.write("\n".join(visitor.output))
#             f.write("\n}")
#         print("Programa analisado com sucesso! ✅")
#         print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")
#     except Exception as e:
#         print(f"\033[91mErro durante a análise: {e}\033[0m")
#         sys.exit(1)

# if __name__ == '__main__':
#     main(sys.argv) # type: ignore



from antlr4 import *
from CompiladorGVLexer import CompiladorGVLexer
from CompiladorGVParser import CompiladorGVParser
from MyParserErrorListener import MyParserErrorListener
from ParseTreeGenerator import ParseTreeGenerator
from TACGenerator import TACGenerator  # ✅ import do gerador TAC
import sys

def main(argv):
    if len(argv) < 2:
        print("Uso: python parser.py <arquivo_fonte> [--gerar-tac]")
        return

    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CompiladorGVLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CompiladorGVParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(MyParserErrorListener())

    try:
        tree = parser.inicio()  # regra inicial
        visitor = ParseTreeGenerator()
        visitor.visit(tree)

        with open("saida_ast.dot", "w") as f:
            f.write("digraph AST {\n")
            f.write("\n".join(visitor.output))
            f.write("\n}")
        print("Programa analisado com sucesso! ✅")
        print("Arquivo 'saida_ast.dot' gerado com sucesso! 🌳")

        # ✅ Geração de código TAC, se for requisitado
        if "--gerar-tac" in argv:
            print("\n🚧 Etapa 4: Geração de Código Intermediário (TAC)")
            tacgen = TACGenerator()
            tacgen.visit(tree)
            tacgen.salvar_em_arquivo("saida.tac")
            print("✅ Código TAC gerado em 'saida.tac'")

    except Exception as e:
        print(f"\033[91mErro durante a análise: {e}\033[0m")
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)