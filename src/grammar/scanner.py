#O objetivo desse script é realizar a análise léxica de um código fonte da sua linguagem, utilizando o ANTLR4.


from antlr4 import *                            #ferramentas da biblioteca ANTLR4 para leitura e análise de texto.
from CompiladorGVLexer import CompiladorGVLexer #o lexer gerado pelo ANTLR a partir da sua gramática .g4.
import sys

                                                #função inicial: Verifica se o usuário passou o caminho 
                                                #do arquivo como argumento. Se não passou, exibe a instrução correta de uso.
def main(argv):
    if len(argv) < 2:
        print("Uso: python scanner.py <caminho_do_arquivo>")
        return
    

    
    input_file = argv[1]                                     #pega o nome do arquivo a ser analisado.
    input_stream = FileStream(input_file, encoding="utf-8")  #lê o conteúdo desse arquivo como uma cadeia de caracteres 
    lexer = CompiladorGVLexer(input_stream)                  #cria uma instância do lexer, que será responsável por dividir o código em tokens segundo as regras definidas na gramática
    token = lexer.nextToken()                                #inicia a leitura do primeiro token.
    
    
    print("-" * 33)                                          #cabeçalho da tabela 
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