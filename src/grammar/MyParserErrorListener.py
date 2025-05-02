# from antlr4.error.ErrorListener import ErrorListener

# class MyParserErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         RED = "\033[91m"
#         RESET = "\033[0m"

#         simbolo = offendingSymbol.text if offendingSymbol else "simbolo desconhecido"
#         if simbolo == "<EOF>":
#             simbolo = "fim do arquivo"

#         if msg.startswith("missing"):
#             esperado = msg.split(" ")[1].strip("'")
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado '{esperado}' após '{simbolo}'{RESET}")
#         else:
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg} próximo de '{simbolo}'{RESET}")



# from antlr4.error.ErrorListener import ErrorListener
# import sys

# class MyParserErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         RED = "\033[91m"
#         RESET = "\033[0m"
#         simbolo = offendingSymbol.text if offendingSymbol else "símbolo desconhecido"
#         if simbolo == "<EOF>":
#             simbolo = "fim do arquivo"

#         if msg.startswith("missing"):
#             esperado = msg.split(" ")[1].strip("'")
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado '{esperado}' após '{simbolo}'{RESET}")
#         else:
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg} próximo de '{simbolo}'{RESET}")

#         sys.exit(1)  # encerra imediatamente após erro sintático            


from antlr4.error.ErrorListener import ErrorListener
import sys

class MyParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        RED = "\033[91m"
        RESET = "\033[0m"
        simbolo = offendingSymbol.text if offendingSymbol else "símbolo desconhecido"
        if simbolo == "<EOF>":
            simbolo = "fim do arquivo"

        # Tratamento de mensagens específicas
        if msg.startswith("missing"):
            esperado = msg.split(" ")[1].strip("'")
            print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado '{esperado}' após '{simbolo}'{RESET}")
        elif "no viable alternative" in msg:
            print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Comando incompleto ou mal formado antes de '{simbolo}'{RESET}")
        else:
            print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg} próximo de '{simbolo}'{RESET}")

        sys.exit(1)