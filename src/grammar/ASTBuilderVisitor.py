# from src.grammar.CompiladorGVVisitor import CompiladorGVVisitor
# from src.grammar.CompiladorGVParser import CompiladorGVParser

# class SymbolTable:
#     def __init__(self):
#         self.scopes = [{}]  # pilha de escopos

#     def push_scope(self):
#         self.scopes.append({})

#     def pop_scope(self):
#         self.scopes.pop()

#     def define(self, name, info):
#         self.scopes[-1][name] = info

#     def lookup(self, name):
#         for scope in reversed(self.scopes):
#             if name in scope:
#                 return scope[name]
#         return None

# class ASTBuilderVisitor(CompiladorGVVisitor):
#     def __init__(self):
#         super().__init__()
#         self.symbol_table = SymbolTable()

#     def visitInicio(self, ctx: CompiladorGVParser.InicioContext):
#         return {
#             "type": "Program",
#             "body": [self.visit(c) for c in ctx.comandos()]
#         }

#     def visitComandos(self, ctx: CompiladorGVParser.ComandosContext):
#         if ctx.comando_declaracao_funcao():
#             return self.visit(ctx.comando_declaracao_funcao())
#         elif ctx.comando_chamada_funcao():
#             return self.visit(ctx.comando_chamada_funcao())
#         elif ctx.comando_retorno():
#             return self.visit(ctx.comando_retorno())
#         elif ctx.comando_ler():
#             return self.visit(ctx.comando_ler())
#         elif ctx.comando_escrever():
#             return self.visit(ctx.comando_escrever())
#         elif ctx.comando_se():
#             return self.visit(ctx.comando_se())
#         elif ctx.comando_para():
#             return self.visit(ctx.comando_para())
#         elif ctx.comando_enquanto():
#             return self.visit(ctx.comando_enquanto())
#         elif ctx.comando_atribuicao():
#             return self.visit(ctx.comando_atribuicao())
#         elif ctx.comando_declaracao():
#             return self.visit(ctx.comando_declaracao())
#         else:
#             return None

#     def visitComando_declaracao_funcao(self, ctx):
#         tipo = ctx.getChild(0).getText()
#         nome = ctx.ID().getText()
#         parametros = []
#         if ctx.parametros():
#             parametros = [self.visit(p) for p in ctx.parametros().parametro()]
#         corpo = self.visit(ctx.bloco_funcao())
        
#         node = {
#             "type": "FunctionDeclaration",
#             "returnType": tipo,
#             "name": nome,
#             "params": parametros,
#             "body": corpo
#         }
#         # Definir função na tabela de símbolos
#         self.visitFunctionDeclaration(node)
#         return node

#     def visitParametro(self, ctx):
#         return {
#             "type": "Parameter",
#             "paramType": ctx.getChild(0).getText(),
#             "name": ctx.ID().getText()
#         }

#     def visitComando_declaracao_funcao(self, ctx):
#         tipo = ctx.getChild(0).getText()
#         nome = ctx.ID().getText()
#         parametros = []
#         if ctx.parametros():
#             parametros = [self.visit(p) for p in ctx.parametros().parametro()]
#         corpo = self.visit(ctx.bloco_funcao())
#         return {
#             "type": "FunctionDeclaration",
#             "returnType": tipo,
#             "name": nome,
#             "params": parametros,
#             "body": corpo
#         }


#     def visitComando_retorno(self, ctx):
#         return {
#             "type": "Return",
#             "value": self.visit(ctx.expressao())
#         }

#     def visitComando_ler(self, ctx):
#         return {
#             "type": "Read",
#             "identifier": ctx.ID().getText()
#         }

#     def visitComando_escrever(self, ctx):
#         if ctx.STRING():
#             return {
#                 "type": "Write",
#                 "value": ctx.STRING().getText()
#             }
#         return {
#             "type": "Write",
#             "value": self.visit(ctx.expressao())
#         }

#     def visitComando_se(self, ctx):
#         return {
#             "type": "IfStatement",
#             "condition": self.visit(ctx.condicao()),
#             "then": self.visit(ctx.bloco(0)),
#             "else": self.visit(ctx.bloco(1)) if ctx.SENAO() else None
#         }

#     def visitComando_para(self, ctx):
#         return {
#             "type": "ForStatement",
#             "init": self.visit(ctx.atribuicao()),
#             "condition": self.visit(ctx.condicao()),
#             "increment": self.visit(ctx.incremento()),
#             "body": self.visit(ctx.bloco())
#         }

#     def visitComando_enquanto(self, ctx):
#         return {
#             "type": "WhileStatement",
#             "condition": self.visit(ctx.condicao()),
#             "body": self.visit(ctx.bloco())
#         }

#     def visitComando_atribuicao(self, ctx):
#         return self.visit(ctx.atribuicao())

#     def visitAtribuicao(self, ctx):
#         return {
#             "type": "Assignment",
#             "target": ctx.ID().getText(),
#             "value": self.visit(ctx.expressao())
#         }

#     def visitComando_declaracao(self, ctx):
#         tipo = ctx.getChild(0).getText()
#         nome = ctx.ID().getText()
#         valor = self.visit(ctx.expressao()) if ctx.expressao() else None
        
#         # Define variável no escopo atual
#         self.symbol_table.define(nome, {
#             "type": "variable",
#             "varType": tipo,
#             "value": valor
#         })
        
#         return {
#             "type": "VariableDeclaration",
#             "varType": tipo,
#             "name": nome,
#             "value": valor
#         }

#     def visitIncremento(self, ctx):
#         if ctx.INCREMENTO():
#             return {"type": "Increment", "target": ctx.ID().getText()}
#         elif ctx.DECREMENTO():
#             return {"type": "Decrement", "target": ctx.ID().getText()}
#         else:
#             return self.visit(ctx.atribuicao())

#     def visitCondicao(self, ctx):
#         if ctx.operador():  # caso: expressao operador expressao
#             return {
#                 "type": "condicao_binaria",
#                 "left": self.visit(ctx.expressao(0)),
#                 "op": ctx.operador().getText(),
#                 "right": self.visit(ctx.expressao(1))
#             }
#         elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
#             # caso: (condicao)
#             return self.visit(ctx.condicao(0))
#         elif ctx.AND():
#             # caso: condicao AND condicao
#             return {
#                 "type": "condicao_logica",
#                 "op": "&&",
#                 "left": self.visit(ctx.condicao(0)),
#                 "right": self.visit(ctx.condicao(1))
#             }
#         elif ctx.OR():
#             # caso: condicao OR condicao
#             return {
#                 "type": "condicao_logica",
#                 "op": "||",
#                 "left": self.visit(ctx.condicao(0)),
#                 "right": self.visit(ctx.condicao(1))
#             }
#         else:
#             raise Exception("Condicao não reconhecida")

#     def visitExpressao(self, ctx):
#         if hasattr(ctx, "op") and ctx.op:
#             return {
#                 "type": "BinaryExpression",
#                 "operator": ctx.op.text,
#                 "left": self.visit(ctx.expressao(0)),
#                 "right": self.visit(ctx.expressao(1))
#             }
#         elif ctx.ID() and ctx.ABRE_PAR():
#             nome = ctx.ID().getText()
#             args = []
#             # if ctx.lista_argumentos():
#             if hasattr(ctx, "lista_argumentos") and ctx.lista_argumentos():
#                 args = [self.visit(e) for e in ctx.lista_argumentos().expressao()]
#             return {
#                 "type": "FunctionCall",
#                 "name": nome,
#                 "arguments": args
#             }
#         elif ctx.ABRE_PAR():
#             return self.visit(ctx.expressao(0))
#         elif ctx.INTEIRO():
#             return {"type": "IntLiteral", "value": int(ctx.INTEIRO().getText())}
#         elif ctx.FLOAT():
#             return {"type": "FloatLiteral", "value": float(ctx.FLOAT().getText())}
#         elif ctx.STRING():
#             return {"type": "StringLiteral", "value": ctx.STRING().getText()}
#         elif ctx.ID():
#             return {"type": "Identifier", "name": ctx.ID().getText()}

#     def visitBloco(self, ctx):
#         return {
#             "type": "Block",
#             "statements": [self.visit(c) for c in ctx.comandos()]
#         }

#     def visitBloco_funcao(self, ctx):
#         statements = [self.visit(c) for c in ctx.comandos()]
#         retorno = self.visit(ctx.comando_retorno())
#         statements.append(retorno)
#         return {
#             "type": "Block",
#             "statements": statements
#         }
    
#     def visitFunctionDeclaration(self, node):
#         func_name = node["name"]
#         return_type = node["returnType"]
#         params = node["params"]

#         # Define função no escopo global (nível 0)
#         self.symbol_table.define(func_name, {
#             "type": "function",
#             "returnType": return_type,
#             "params": params
#         })

#         # Cria escopo para corpo da função
#         self.symbol_table.push_scope()

#         # Define parâmetros no escopo da função
#         for param in params:
#             self.symbol_table.define(param["name"], {"type": param["paramType"]})

#         # Visita corpo para capturar definições internas
#         self.visit(node["body"])

#         # Sai do escopo da função
#         self.symbol_table.pop_scope()

from src.grammar.CompiladorGVVisitor import CompiladorGVVisitor
from src.grammar.CompiladorGVParser import CompiladorGVParser

class SymbolTable:
    def __init__(self):
        self.scopes = [{}]

    def push_scope(self):
        self.scopes.append({})

    def pop_scope(self):
        self.scopes.pop()

    def define(self, name, info):
        self.scopes[-1][name] = info

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

class ASTBuilderVisitor(CompiladorGVVisitor):
    def __init__(self):
        super().__init__()
        self.symbol_table = SymbolTable()

    def get_position(self, token):
        return {"line": token.line, "column": token.column} if token else {}

    def visitInicio(self, ctx):
        return {
            "type": "Program",
            "body": [self.visit(c) for c in ctx.comandos()],
            **self.get_position(ctx.start)
        }

    def visitComandos(self, ctx):
        for method in [
            ctx.comando_declaracao_funcao, ctx.comando_chamada_funcao,
            ctx.comando_retorno, ctx.comando_ler, ctx.comando_escrever,
            ctx.comando_se, ctx.comando_para, ctx.comando_enquanto,
            ctx.comando_atribuicao, ctx.comando_declaracao
        ]:
            if method():
                return self.visit(method())
        return None

    def visitParametro(self, ctx):
        return {
            "type": "Parameter",
            "paramType": ctx.getChild(0).getText(),
            "name": ctx.ID().getText(),
            **self.get_position(ctx.ID().getSymbol())
        }

    def visitComando_declaracao_funcao(self, ctx):
        tipo = ctx.getChild(0).getText()
        nome = ctx.ID().getText()
        parametros = []
        if ctx.parametros():
            parametros = [self.visit(p) for p in ctx.parametros().parametro()]
        corpo = self.visit(ctx.bloco_funcao())
        return {
            "type": "FunctionDeclaration",
            "returnType": tipo,
            "name": nome,
            "params": parametros,
            "body": corpo,
            **self.get_position(ctx.ID().getSymbol())
        }

    def visitComando_retorno(self, ctx):
        return {
            "type": "Return",
            "value": self.visit(ctx.expressao()),
            **self.get_position(ctx.start)
        }

    def visitComando_ler(self, ctx):
        return {
            "type": "Read",
            "identifier": ctx.ID().getText(),
            **self.get_position(ctx.ID().getSymbol())
        }

    def visitComando_escrever(self, ctx):
        return {
            "type": "Write",
            "value": ctx.STRING().getText() if ctx.STRING() else self.visit(ctx.expressao()),
            **self.get_position(ctx.start)
        }

    def visitComando_se(self, ctx):
        return {
            "type": "IfStatement",
            "condition": self.visit(ctx.condicao()),
            "then": self.visit(ctx.bloco(0)),
            "else": self.visit(ctx.bloco(1)) if ctx.SENAO() else None,
            **self.get_position(ctx.start)
        }

    def visitComando_para(self, ctx):
        return {
            "type": "ForStatement",
            "init": self.visit(ctx.atribuicao()),
            "condition": self.visit(ctx.condicao()),
            "increment": self.visit(ctx.incremento()),
            "body": self.visit(ctx.bloco()),
            **self.get_position(ctx.start)
        }

    def visitComando_enquanto(self, ctx):
        return {
            "type": "WhileStatement",
            "condition": self.visit(ctx.condicao()),
            "body": self.visit(ctx.bloco()),
            **self.get_position(ctx.start)
        }

    def visitComando_atribuicao(self, ctx):
        return self.visit(ctx.atribuicao())

    def visitAtribuicao(self, ctx):
        return {
            "type": "Assignment",
            "target": ctx.ID().getText(),
            "value": self.visit(ctx.expressao()),
            **self.get_position(ctx.ID().getSymbol())
        }

    def visitComando_declaracao(self, ctx):
        tipo = ctx.getChild(0).getText()
        nome = ctx.ID().getText()
        valor = self.visit(ctx.expressao()) if ctx.expressao() else None

        self.symbol_table.define(nome, {
            "type": "variable",
            "varType": tipo,
            "value": valor
        })

        return {
            "type": "VariableDeclaration",
            "varType": tipo,
            "name": nome,
            "value": valor,
            **self.get_position(ctx.ID().getSymbol())
        }

    def visitIncremento(self, ctx):
        if ctx.INCREMENTO():
            return {
                "type": "Increment",
                "target": ctx.ID().getText(),
                **self.get_position(ctx.ID().getSymbol())
            }
        elif ctx.DECREMENTO():
            return {
                "type": "Decrement",
                "target": ctx.ID().getText(),
                **self.get_position(ctx.ID().getSymbol())
            }
        return self.visit(ctx.atribuicao())

    def visitCondicao(self, ctx):
        if ctx.operador():
            return {
                "type": "condicao_binaria",
                "op": ctx.operador().getText(),
                "left": self.visit(ctx.expressao(0)),
                "right": self.visit(ctx.expressao(1)),
                **self.get_position(ctx.start)
            }
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.condicao(0))
        elif ctx.AND():
            return {
                "type": "condicao_logica",
                "op": "&&",
                "left": self.visit(ctx.condicao(0)),
                "right": self.visit(ctx.condicao(1)),
                **self.get_position(ctx.start)
            }
        elif ctx.OR():
            return {
                "type": "condicao_logica",
                "op": "||",
                "left": self.visit(ctx.condicao(0)),
                "right": self.visit(ctx.condicao(1)),
                **self.get_position(ctx.start)
            }
        raise Exception("Condicao não reconhecida")

    def visitExpressao(self, ctx):
        if hasattr(ctx, "op") and ctx.op:
            return {
                "type": "BinaryExpression",
                "operator": ctx.op.text,
                "left": self.visit(ctx.expressao(0)),
                "right": self.visit(ctx.expressao(1)),
                **self.get_position(ctx.start)
            }
        elif ctx.ID() and ctx.ABRE_PAR():
            nome = ctx.ID().getText()
            args = []
            if hasattr(ctx, "lista_argumentos") and ctx.lista_argumentos():
                args = [self.visit(e) for e in ctx.lista_argumentos().expressao()]
            return {
                "type": "FunctionCall",
                "name": nome,
                "arguments": args,
                **self.get_position(ctx.ID().getSymbol())
            }
        elif ctx.ABRE_PAR():
            return self.visit(ctx.expressao(0))
        elif ctx.INTEIRO():
            return {
                "type": "IntLiteral",
                "value": int(ctx.INTEIRO().getText()),
                **self.get_position(ctx.INTEIRO().getSymbol())
            }
        elif ctx.FLOAT():
            return {
                "type": "FloatLiteral",
                "value": float(ctx.FLOAT().getText()),
                **self.get_position(ctx.FLOAT().getSymbol())
            }
        elif ctx.STRING():
            return {
                "type": "StringLiteral",
                "value": ctx.STRING().getText(),
                **self.get_position(ctx.STRING().getSymbol())
            }
        elif ctx.ID():
            return {
                "type": "Identifier",
                "name": ctx.ID().getText(),
                **self.get_position(ctx.ID().getSymbol())
            }

    def visitBloco(self, ctx):
        return {
            "type": "Block",
            "statements": [self.visit(c) for c in ctx.comandos()],
            **self.get_position(ctx.start)
        }

    def visitBloco_funcao(self, ctx):
        statements = [self.visit(c) for c in ctx.comandos()]
        retorno = self.visit(ctx.comando_retorno())
        statements.append(retorno)
        return {
            "type": "Block",
            "statements": statements,
            **self.get_position(ctx.start)
        }

    def visitFunctionDeclaration(self, node):
        func_name = node["name"]
        return_type = node["returnType"]
        params = node["params"]

        self.symbol_table.define(func_name, {
            "type": "function",
            "returnType": return_type,
            "params": params
        })

        self.symbol_table.push_scope()
        for param in params:
            self.symbol_table.define(param["name"], {"type": param["paramType"]})
        self.visit(node["body"])
        self.symbol_table.pop_scope()