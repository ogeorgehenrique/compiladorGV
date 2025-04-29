# #Scanner.py (Léxico): responsavel por reconhecer palavras (tokens) 
# # O scanner vê tudo como tokens: TIPO_INT, ID, ABRE_PAR, STRING, FECHA_PAR, RETORNA, INTEIRO, FECHA_CHAVE

from antlr4 import *
from CompiladorGVLexer import CompiladorGVLexer
from MyLexerErrorListener import MyLexerErrorListener
import sys

def main(argv):
    if len(argv) < 2:
        print("Uso: python scanner.py <caminho_do_arquivo>")
        return

    input_file = argv[1]
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = CompiladorGVLexer(input_stream)

    # Remove listeners padrões e adiciona o nosso
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyLexerErrorListener())

    token = lexer.nextToken()
    print("-" * 33)
    print(f"{'Tipo||':<5} {'Lexema||':<5} {'Linha||':<5} {'Coluna||'}")
    print("-" * 33)

    while token.type != Token.EOF:
        tipo_token = lexer.symbolicNames[token.type]
        lexema = token.text
        linha = token.line
        coluna = token.column + 1

        if tipo_token != "ERROR":
            print(f"<{tipo_token}, '{lexema}', {linha}, {coluna}>")

        token = lexer.nextToken()

if __name__ == '__main__':
    main(sys.argv)





##nao usar porque gera colunas simples
# from antlr4 import *
# from CompiladorGVLexer import CompiladorGVLexer
# import sys

# def main(argv):
#     # Verifica se o usuário passou o nome do arquivo
#     if len(argv) < 2:
#         print("Uso: python scanner.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")
#     lexer = CompiladorGVLexer(input_stream)
#     token = lexer.nextToken()

#     print(f"{'Tipo':<20} {'Lexema':<20} {'Linha':<5} {'Coluna'}")
#     print("-" * 60)

#     while token.type != Token.EOF:
#         tipo_token = lexer.symbolicNames[token.type]
#         lexema = token.text
#         linha = token.line
#         coluna = token.column

#         # Verificar erro léxico
#         if tipo_token == "ERROR":
#             print(f"[Erro Léxico] Símbolo inválido '{lexema}' na linha {linha}, coluna {coluna}")
#         else:
#             print(f"{tipo_token:<20} {lexema:<20} {linha:<5} {coluna}")

#         token = lexer.nextToken()

# if __name__ == '__main__':
#     main(sys.argv)
################################################

# from antlr4 import *
# from CompiladorGVLexer import CompiladorGVLexer
# import sys

# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python scanner.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")
#     lexer = CompiladorGVLexer(input_stream)
#     token = lexer.nextToken()
#     print("-" * 33)
#     print(f"{'Tipo||':<5} {'Lexema||':<5} {'Linha||':<5} {'Coluna||'}")
#     print("-" * 33)

#     while token.type != Token.EOF:
#         tipo_token = lexer.symbolicNames[token.type]
#         lexema = token.text
#         linha = token.line
#         coluna = token.column + 1  # Corrige para exibir a coluna como humano lê (começa no 1)

#         # Verificar erro léxico (se você criar o token ERRO depois)
#         if tipo_token == "ERROR":
#             print(f"[Erro Léxico] Símbolo inválido '{lexema}' na linha {linha}, coluna {coluna}")
#         else:
#             print(f"<{tipo_token}, '{lexema}', {linha}, {coluna}>")

#         token = lexer.nextToken()

# if __name__ == '__main__':
#     main(sys.argv)

########################################







# import sys
# from enum import Enum, auto

# class TipoToken(Enum):
#     # Palavras-chave
#     LEIA = auto()
#     ESCREVA = auto()
#     SE = auto()
#     SENAO = auto()
#     ENQUANTO = auto()
#     FAÇA = auto()
#     INT = auto()
#     STRING = auto()
    
#     # Operadores
#     OP_ARIT = auto()  # +, -, *, /
#     OP_LOG = auto()    # &&, ||, ==, !=
#     OP_REL = auto()    # >, <, >=, <=
#     ATRIBUICAO = auto()
    
#     # Delimitadores
#     ABRE_PAR = auto()
#     FECHA_PAR = auto()
#     ABRE_CHAVE = auto()
#     FECHA_CHAVE = auto()
#     VIRGULA = auto()
#     PONTO_VIRGULA = auto()
    
#     # Literais
#     NUM_INT = auto()
#     NUM_DEC = auto()
#     TEXTO = auto()
#     ID = auto()
    
#     # Fim de arquivo
#     EOF = auto()

# class Token:
#     def __init__(self, tipo, lexema, linha, coluna):
#         self.tipo = tipo
#         self.lexema = lexema
#         self.linha = linha
#         self.coluna = coluna
    
#     def __str__(self):
#         return f"<{self.tipo.name}, '{self.lexema}', {self.linha}, {self.coluna}>"

# class ErroLexico(Exception):
#     def __init__(self, msg, linha, coluna):
#         super().__init__(f"ERRO LÉXICO [Linha {linha}, Coluna {coluna}]: {msg}")

# class Scanner:
#     def __init__(self, codigo_fonte):
#         self.codigo = codigo_fonte
#         self.pos = 0
#         self.linha = 1
#         self.coluna = 1
#         self.palavras_chave = {
#             'leia': TipoToken.LEIA,
#             'escreva': TipoToken.ESCREVA,
#             'se': TipoToken.SE,
#             'senao': TipoToken.SENAO,
#             'enquanto': TipoToken.ENQUANTO,
#             'faça': TipoToken.FAÇA,
#             'int': TipoToken.INT,
#             'string': TipoToken.STRING
#         }
    
#     def proximo_token(self):
#         while self.pos < len(self.codigo):
#             char = self.codigo[self.pos]
            
#             # Ignorar espaços e quebras de linha
#             if char in ' \t':
#                 self.avancar()
#                 continue
#             elif char == '\n':
#                 self.linha += 1
#                 self.coluna = 1
#                 self.avancar()
#                 continue
            
#             # Comentários (//)
#             if char == '/' and self.pos + 1 < len(self.codigo) and self.codigo[self.pos + 1] == '/':
#                 self.ignorar_comentario()
#                 continue
            
#             # Identificadores e palavras-chave
#             if char.isalpha() or char == '_':
#                 return self.identificar_id_ou_palavra_chave()
            
#             # Números (inteiros ou decimais)
#             if char.isdigit():
#                 return self.identificar_numero()
            
#             # Strings (texto entre aspas)
#             if char == '"':
#                 return self.identificar_texto()
            
#             # Operadores e delimitadores
#             if char in '+-*/=!<>':
#                 return self.identificar_operador()
            
#             if char in '(){},;':
#                 return self.identificar_delimitador(char)
            
#             # Símbolo inválido
#             raise ErroLexico(f"Símbolo '{char}' inválido", self.linha, self.coluna)
        
#         # Fim do arquivo
#         return Token(TipoToken.EOF, '', self.linha, self.coluna)
    
#     def avancar(self):
#         self.pos += 1
#         self.coluna += 1
    
#     def ignorar_comentario(self):
#         while self.pos < len(self.codigo) and self.codigo[self.pos] != '\n':
#             self.avancar()
    
#     def identificar_id_ou_palavra_chave(self):
#         inicio = self.pos
#         while self.pos < len(self.codigo) and (self.codigo[self.pos].isalnum() or self.codigo[self.pos] == '_'):
#             self.avancar()
        
#         lexema = self.codigo[inicio:self.pos]
#         tipo = self.palavras_chave.get(lexema, TipoToken.ID)
#         return Token(tipo, lexema, self.linha, inicio - self.coluna + 1)
    
#     def identificar_numero(self):
#         inicio = self.pos
#         while self.pos < len(self.codigo) and self.codigo[self.pos].isdigit():
#             self.avancar()
        
#         # Verificar se é decimal
#         if self.pos < len(self.codigo) and self.codigo[self.pos] == '.':
#             self.avancar()
#             while self.pos < len(self.codigo) and self.codigo[self.pos].isdigit():
#                 self.avancar()
#             tipo = TipoToken.NUM_DEC
#         else:
#             tipo = TipoToken.NUM_INT
        
#         lexema = self.codigo[inicio:self.pos]
#         return Token(tipo, lexema, self.linha, inicio - self.coluna + 1)
    
#     def identificar_texto(self):
#         inicio = self.pos
#         self.avancar()  # Pular a aspas inicial
        
#         while self.pos < len(self.codigo) and self.codigo[self.pos] != '"':
#             if self.codigo[self.pos] == '\n':
#                 raise ErroLexico("Texto não fechado", self.linha, self.coluna)
#             self.avancar()
        
#         if self.pos >= len(self.codigo):
#             raise ErroLexico("Texto não fechado", self.linha, self.coluna)
        
#         lexema = self.codigo[inicio + 1:self.pos]  # Excluir as aspas
#         self.avancar()  # Pular a aspas final
#         return Token(TipoToken.TEXTO, lexema, self.linha, inicio - self.coluna + 1)
    
#     def identificar_operador(self):
#         char = self.codigo[self.pos]
#         inicio = self.pos
        
#         # Operadores compostos (==, !=, >=, <=, &&, ||)
#         if self.pos + 1 < len(self.codigo):
#             dois_chars = self.codigo[self.pos:self.pos + 2]
#             if dois_chars in ('==', '!=', '>=', '<=', '&&', '||'):
#                 self.avancar()
#                 self.avancar()
#                 return Token(TipoToken.OP_LOG, dois_chars, self.linha, inicio - self.coluna + 1)
        
#         # Operadores simples (+, -, *, /, =, !, <, >)
#         if char in '+-*/':
#             self.avancar()
#             return Token(TipoToken.OP_ARIT, char, self.linha, inicio - self.coluna + 1)
#         elif char in '=!<>':
#             self.avancar()
#             return Token(TipoToken.OP_REL, char, self.linha, inicio - self.coluna + 1)
    
#     def identificar_delimitador(self, char):
#         mapeamento = {
#             '(': TipoToken.ABRE_PAR,
#             ')': TipoToken.FECHA_PAR,
#             '{': TipoToken.ABRE_CHAVE,
#             '}': TipoToken.FECHA_CHAVE,
#             ',': TipoToken.VIRGULA,
#             ';': TipoToken.PONTO_VIRGULA
#         }
#         self.avancar()
#         return Token(mapeamento[char], char, self.linha, self.coluna - 1)

# # Exemplo de uso
# if __name__ == "__main__":
#     codigo = """
#     int n = 5}
#     escreva("Hello, world!");
#     """
    
#     scanner = Scanner(codigo)
#     try:
#         while True:
#             token = scanner.proximo_token()
#             print(token)
#             if token.tipo == TipoToken.EOF:
#                 break
#     except ErroLexico as e:
#         print(e)



# from antlr4 import *
# from CompiladorGVLexer import CompiladorGVLexer
# import sys

# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python scanner.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")
#     lexer = CompiladorGVLexer(input_stream)
    
#     # Cabeçalho da tabela de tokens
#     print(f"{'Tipo':<20} {'Lexema':<20} {'Linha':<5} {'Coluna':<5}")
#     print("-" * 50)

#     token = lexer.nextToken()
#     while token.type != Token.EOF:
#         tipo_nome = lexer.symbolicNames[token.type]
#         lexema = token.text
#         linha = token.line
#         coluna = token.column + 1  # ANTLR conta coluna a partir de 0

#         # Tratamento de erros léxicos (token do tipo ERROR)
#         if tipo_nome == "ERROR":
#             print(f"ERRO LÉXICO [Linha {linha}, Coluna {coluna}]: Símbolo '{lexema}' inválido", file=sys.stderr)
#         else:
#             # Saída formatada conforme especificação (<Tipo, Lexema, Linha, Coluna>)
#             print(f"<{tipo_nome}, '{lexema}', {linha}, {coluna}>")

#         token = lexer.nextToken()

# if __name__ == '__main__':
#     main(sys.argv)




# from antlr4 import *
# from CompiladorGVLexer import CompiladorGVLexer
# import sys

# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python scanner.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")
#     lexer = CompiladorGVLexer(input_stream)
#     token_stream = CommonTokenStream(lexer)
#     token_stream.fill()  # Carrega todos os tokens

#     # Imprime cabeçalho
#     print(f"{'Tipo':<20} {'Lexema':<20} {'Linha':<5} {'Coluna':<5}")
#     print("-" * 50)

#     for token in token_stream.tokens[:-1]:  # Ignora o token EOF
#         tipo_nome = lexer.symbolicNames[token.type]
#         lexema = token.text.replace("\n", "\\n")  # Escapa quebras de linha
#         linha = token.line
#         coluna = token.column + 1  # Ajuste para coluna iniciar em 1

#         if tipo_nome == "ERROR":
#             # Formatação EXATA como no PDF
#             erro_msg = f"ERRO LÉXICO [Linha {linha}, Coluna {coluna}]: Símbolo '{lexema}' inválido."
#             print(erro_msg, file=sys.stderr)
#         else:
#             print(f"<{tipo_nome}, '{lexema}', {linha}, {coluna}>")

# if __name__ == '__main__':
#     main(sys.argv)


# from antlr4 import *
# from antlr4.error.ErrorListener import ErrorListener
# from CompiladorGVLexer import CompiladorGVLexer
# import sys

# class MeuErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         # Ignora a mensagem padrão do ANTLR
#         pass

# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python scanner.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")
#     lexer = CompiladorGVLexer(input_stream)
    
#     # Remove os listeners padrão de erro do ANTLR
#     lexer.removeErrorListeners()
    
#     # Adiciona nosso listener personalizado (que ignora erros)
#     lexer.addErrorListener(MeuErrorListener())
    
#     token_stream = CommonTokenStream(lexer)
#     token_stream.fill()  # Carrega todos os tokens

#     print(f"{'Tipo':<20} {'Lexema':<20} {'Linha':<5} {'Coluna':<5}")
#     print("-" * 50)

#     for token in token_stream.tokens[:-1]:  # Ignora o token EOF
#         tipo_nome = lexer.symbolicNames[token.type]
#         lexema = token.text
#         linha = token.line
#         coluna = token.column + 1  # Ajuste para coluna iniciar em 1

#         if token.type == lexer.ERROR:  # Verifica se é um token de erro
#             print(f"ERRO LÉXICO [Linha {linha}, Coluna {coluna}]: Símbolo '{lexema}' inválido.", file=sys.stderr)
#         else:
#             print(f"<{tipo_nome}, '{lexema}', {linha}, {coluna}>")

# if __name__ == '__main__':
#     main(sys.argv)

# from antlr4 import *
# from antlr4.error.ErrorListener import ErrorListener
# from CompiladorGVLexer import CompiladorGVLexer
# import sys

# class MeuErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         pass  # Silencia erros padrão do ANTLR

# def main(argv):
#     if len(argv) < 2:
#         print("Uso: python scanner.py <caminho_do_arquivo>")
#         return

#     input_file = argv[1]
#     input_stream = FileStream(input_file, encoding="utf-8")
#     lexer = CompiladorGVLexer(input_stream)
#     lexer.removeErrorListeners()
#     lexer.addErrorListener(MeuErrorListener())
    
#     try:
#         token_stream = CommonTokenStream(lexer)
#         token_stream.fill()
        
#         print(f"{'Tipo':<20} {'Lexema':<20} {'Linha':<5} {'Coluna':<5}")
#         print("-" * 50)

#         for token in token_stream.tokens[:-1]:
#             tipo_nome = lexer.symbolicNames[token.type]
#             lexema = token.text.replace("\n", "\\n")
#             linha = token.line
#             coluna = token.column + 1
            
#             print(f"<{tipo_nome}, '{lexema}', {linha}, {coluna}>")
            
#     except Exception as e:
#         print(str(e), file=sys.stderr)

# if __name__ == '__main__':
#     main(sys.argv)