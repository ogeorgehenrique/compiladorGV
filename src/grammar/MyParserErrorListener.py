# from antlr4.error.ErrorListener import ErrorListener
# import sys

# class MyParserErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         RED = "\033[91m"
#         RESET = "\033[0m"
#         simbolo = offendingSymbol.text if offendingSymbol else "símbolo desconhecido"
#         if simbolo == "<EOF>":
#             simbolo = "fim do arquivo"

#         # Tratamento de mensagens específicas
#         if msg.startswith("missing"):
#             esperado = msg.split(" ")[1].strip("'")
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado '{esperado}' após '{simbolo}'{RESET}")
#         elif "no viable alternative" in msg:
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Comando incompleto ou mal formado antes de '{simbolo}'{RESET}")
#         else:
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg} próximo de '{simbolo}'{RESET}")

#         sys.exit(1)

from antlr4.error.ErrorListener import ErrorListener
import sys

class MyParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        RED = "\033[91m"
        RESET = "\033[0m"
        simbolo = offendingSymbol.text if offendingSymbol else "símbolo desconhecido"

        if simbolo == "<EOF>":
            simbolo = "fim do arquivo"

        # Tratamento de mensagens específicas com base no conteúdo da mensagem do ANTLR
        if msg.startswith("missing"):
            esperado = msg.split(" ")[1].strip("'")
            if esperado == "';'":
                print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado ';' após '{simbolo}'{RESET}")
            else:
                print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado {esperado} após '{simbolo}'{RESET}")

        elif "no viable alternative" in msg:
            print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Comando incompleto ou mal formado antes de '{simbolo}'{RESET}")

        else:
            print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg} próximo de '{simbolo}'{RESET}")

        sys.exit(1)

# from antlr4.error.ErrorListener import ErrorListener
# import sys

# class MyParserErrorListener(ErrorListener):
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         RED = "\033[91m"
#         RESET = "\033[0m"
#         simbolo = offendingSymbol.text if offendingSymbol else "símbolo desconhecido"
#         simbolo_lower = simbolo.lower()

#         if simbolo == "<EOF>":
#             simbolo = "fim do arquivo"

#         # Tratamento específico de erro por token ausente
#         if msg.startswith("missing"):
#             esperado = msg.split(" ")[1].strip("'")
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado '{esperado}' após '{simbolo}'{RESET}")

#         # Heurística para ausência de ponto e vírgula disfarçada de "no viable alternative"
#         elif "no viable alternative" in msg:
#             if simbolo_lower in ["retorna", "}", "escreva", "leia", "para", "se", "senao"]:
#                 print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Esperado ';' antes de '{simbolo}'{RESET}")
#             else:
#                 print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: Comando incompleto ou mal formado antes de '{simbolo}'{RESET}")

#         else:
#             print(f"{RED}ERRO SINTÁTICO [Linha {line}, Coluna {column + 1}]: {msg} próximo de '{simbolo}'{RESET}")

#         sys.exit(1)