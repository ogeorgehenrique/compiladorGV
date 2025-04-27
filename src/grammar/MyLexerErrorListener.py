#Esse código cria um “ouvidor” que intercepta qualquer erro léxico e exibe sua mensagem formatada.
#Em outras palavras ele ira substituir a mensagem padrao do ANTLR de erro

from antlr4.error.ErrorListener import ErrorListener

class MyLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        erro = msg.split(":")[-1].strip()
        print(f"ERRO LÉXICO [Linha {line}, Coluna {column + 1}]: Símbolo '{erro}' inválido.")
        print("-" * 60)
