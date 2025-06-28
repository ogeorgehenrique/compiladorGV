# #
# from CompiladorGVVisitor import CompiladorGVVisitor
# from TAC_Instruction import TAC_Instruction
# from TAC_Operand import TAC_Operand

# class TACGenerator(CompiladorGVVisitor):
#     def __init__(self):
#         self.temp_counter = 0
#         self.label_counter = 0
#         self.instrucoes = []

#     def novo_temp(self):
#         temp = f"_t{self.temp_counter}"
#         self.temp_counter += 1
#         return TAC_Operand("temp", temp)

#     def nova_label(self):
#         label = f"L{self.label_counter}"
#         self.label_counter += 1
#         return TAC_Operand("label", label)

#     def add_instrucao(self, instrucao):
#         self.instrucoes.append(instrucao)

#     def salvar_em_arquivo(self, nome_arquivo):
#         with open(nome_arquivo, "w") as f:
#             for instr in self.instrucoes:
#                 f.write(str(instr) + "\n")

#     # ----------------- Exemplo de implementação -------------------

#     def visitInicio(self, ctx):
#         self.visitChildren(ctx)
#         return None

#     # def visitComando_declaracao(self, ctx):
#     #     if ctx.expressao():
#     #         nome = ctx.ID().getText()
#     #         valor = self.visit(ctx.expressao())
#     #         self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
#     #     return None
    
#     def visitComando_declaracao(self, ctx):
#         nome = ctx.ID().getText()

#         # Tenta pegar a expressão, se existir
#         expressao_ctx = ctx.expressao()
#         if expressao_ctx:
#             valor = self.visit(expressao_ctx)
#             self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
        
#         return None


#     def visitComando_atribuicao(self, ctx):
#         nome = ctx.atribuicao().ID().getText()
#         valor = self.visit(ctx.atribuicao().expressao())
#         self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
#         return None
    
    

#     # def visitExpressao(self, ctx):
#     #     if ctx.getChildCount() == 3:
#     #         arg1 = self.visit(ctx.expressao(0))
#     #         arg2 = self.visit(ctx.expressao(1))
#     #         op = ctx.op.text
#     #         temp = self.novo_temp()
#     #         self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
#     #         return temp
#     #     elif ctx.INTEIRO():
#     #         return TAC_Operand("const", ctx.INTEIRO().getText())
#     #     elif ctx.ID():
#     #         return TAC_Operand("var", ctx.ID().getText())
#     #     else:
#     #         return self.visitChildren(ctx)

#     def visitExpressao(self, ctx):
#         if ctx.getChildCount() == 3:
#             # Caso: expressao '+' expressao
#             arg1 = self.visit(ctx.expressao(0))
#             arg2 = self.visit(ctx.expressao(1))
#             op = ctx.op.text
#             temp = self.novo_temp()
#             self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
#             return temp

#         elif ctx.ABRE_PAR():
#             # Caso: ( expressao )
#             return self.visit(ctx.expressao(0))

#         elif ctx.INTEIRO():
#             return TAC_Operand("const", ctx.INTEIRO().getText())

#         elif ctx.ID():
#             return TAC_Operand("var", ctx.ID().getText())

#         else:
#             return self.visitChildren(ctx)


# src/grammar/TACGenerator.py

from CompiladorGVVisitor import CompiladorGVVisitor
from TAC_Instruction import TAC_Instruction
from TAC_Operand import TAC_Operand

class TACGenerator(CompiladorGVVisitor):
    def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0
        self.instrucoes = []

    def novo_temp(self):
        nome = f"_t{self.temp_counter}"
        self.temp_counter += 1
        return TAC_Operand("temp", nome)

    def nova_label(self):
        nome = f"L{self.label_counter}"
        self.label_counter += 1
        return TAC_Operand("label", nome)

    def add_instrucao(self, instrucao):
        self.instrucoes.append(instrucao)

    def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "w") as f:
            for instr in self.instrucoes:
                f.write(str(instr) + "\n")

    # ---------- Visitando a regra inicial ----------
    def visitInicio(self, ctx):
        self.visitChildren(ctx)
        return None

    # ---------- Declaração de variável ----------
    def visitComando_declaracao(self, ctx):
        nome = ctx.ID().getText()
        expressao_ctx = ctx.expressao()
        
        if expressao_ctx:
            valor = self.visit(expressao_ctx)
            self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
        
        return None

    # ---------- Atribuição ----------
    def visitComando_atribuicao(self, ctx):
        nome = ctx.atribuicao().ID().getText()
        valor = self.visit(ctx.atribuicao().expressao())
        self.add_instrucao(TAC_Instruction("=", TAC_Operand("var", nome), valor))
        return None

    # ---------- Expressões aritméticas e simples ----------
    # def visitExpressao(self, ctx):
    #     print(f"[DEBUG] EXPRESSAO: {ctx.getText()} ({ctx.getChildCount()} filhos)")

    #     if ctx.getChildCount() == 3:
    #         arg1 = self.visit(ctx.expressao(0))
    #         arg2 = self.visit(ctx.expressao(1))
    #         op = ctx.op.text
    #         temp = self.novo_temp()
    #         self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
    #         return temp

    #     elif ctx.ABRE_PAR():
    #         print("[DEBUG] Parênteses detectado")
    #         return self.visit(ctx.expressao(0))

    #     elif ctx.INTEIRO():
    #         return TAC_Operand("const", ctx.INTEIRO().getText())

    #     elif ctx.ID():
    #         return TAC_Operand("var", ctx.ID().getText())

    #     return None
        




    # def visitExpressao(self, ctx):
    #     # print(f"[DEBUG] EXPRESSAO: {ctx.getText()} ({ctx.getChildCount()} filhos)")
    #     filhos = ctx.getChildCount()
    #     texto = ctx.getText()
    #     print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")
        



    #     # EXPRESSAO BINÁRIA: a + b
    #     if filhos == 3 and ctx.getChild(1).getText() in ['+', '-', '*', '/']:
    #         arg1 = self.visit(ctx.getChild(0))
    #         op = ctx.getChild(1).getText()
    #         arg2 = self.visit(ctx.getChild(2))
    #         temp = self.novo_temp()
    #         self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
    #         print(f"[DEBUG] TAC: {temp} = {arg1} {op} {arg2}")
            
    #         return temp

    #     # EXPRESSAO COM PARÊNTESES: (a + b)
    #     elif filhos == 3 and ctx.getChild(0).getText() == '(':
    #         return self.visit(ctx.getChild(1))

    #     # LITERAL: número inteiro
    #     elif ctx.INTEIRO():
    #         return TAC_Operand("const", ctx.INTEIRO().getText())

    #     # LITERAL: número float
    #     elif ctx.FLOAT():
    #         return TAC_Operand("const", ctx.FLOAT().getText())

    #     # LITERAL: string
    #     elif ctx.STRING():
    #         return TAC_Operand("const", ctx.STRING().getText())

    #     # VARIÁVEL
    #     elif ctx.ID():
    #         return TAC_Operand("var", ctx.ID().getText())

    #     return self.visitChildren(ctx)    



    # def visitExpressao(self, ctx):
    #     if ctx.getChildCount() == 3:
    #         # Expressão binária: a + b, (a + b), etc.
    #         arg1 = self.visit(ctx.expressao(0))
    #         arg2 = self.visit(ctx.expressao(1))
    #         op = ctx.op.text
    #         temp = self.novo_temp()
    #         self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
    #         return temp

    #     elif ctx.ABRE_PAR():
    #         # Expressão entre parênteses: (a + b)
    #         return self.visit(ctx.expressao(0))

    #     elif ctx.INTEIRO():
    #         return TAC_Operand("const", ctx.INTEIRO().getText())

    #     elif ctx.FLOAT():
    #         return TAC_Operand("const", ctx.FLOAT().getText())

    #     elif ctx.STRING():
    #         return TAC_Operand("const", ctx.STRING().getText())

    #     elif ctx.ID():
    #         return TAC_Operand("var", ctx.ID().getText())

    #     return None



    #nao detectava a chamada de funcoes 
    # def visitExpressao(self, ctx):
    #     filhos = ctx.getChildCount()
    #     texto = ctx.getText()
    #     print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

    #     # EXPRESSAO BINÁRIA: a + b, a - b, etc.
    #     if filhos == 3 and ctx.getChild(1).getText() in ['+', '-', '*', '/']:
    #         arg1 = self.visit(ctx.getChild(0))
    #         op = ctx.getChild(1).getText()
    #         arg2 = self.visit(ctx.getChild(2))
    #         temp = self.novo_temp()
    #         self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
    #         # print(f"[DEBUG] TAC: {temp} = {arg1} {op} {arg2}")
    #         print(f"\033[94m[DEBUG] EXPRESSAO: {arg1} {op} {arg2} → {temp}\033[0m")
    #         return temp

    #     # EXPRESSAO COM PARÊNTESES: (a + b)
    #     elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
    #         print("[DEBUG] Parênteses detectado")
    #         return self.visit(ctx.getChild(1))

    #     # LITERAL INTEIRO
    #     elif ctx.INTEIRO():
    #         valor = ctx.INTEIRO().getText()
    #         print(f"[DEBUG] INTEIRO: {valor}")
    #         return TAC_Operand("const", valor)

    #     # LITERAL FLOAT
    #     elif ctx.FLOAT():
    #         valor = ctx.FLOAT().getText()
    #         print(f"[DEBUG] FLOAT: {valor}")
    #         return TAC_Operand("const", valor)

    #     # LITERAL STRING
    #     elif ctx.STRING():
    #         valor = ctx.STRING().getText()
    #         print(f"[DEBUG] STRING: {valor}")
    #         return TAC_Operand("const", valor)

    #     # IDENTIFICADOR
    #     elif ctx.ID():
    #         nome = ctx.ID().getText()
    #         print(f"[DEBUG] ID: {nome}")
    #         return TAC_Operand("var", nome)


    #     elif ctx.getChildCount() == 4 and ctx.getChild(1).getText() == "(":
    #         nome_funcao = ctx.getChild(0).getText()
    #         argumentos = []  # futuramente analise argumentos
    #         # TODO: tratar lista de argumentos (ctx.expressao()) dentro dos parênteses
    #         temp = self.novo_temp()
    #         self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
    #         return temp

    #     # Fallback
    #     print("[DEBUG] Visitando filhos como fallback")
    #     return self.visitChildren(ctx)
    
    #sem o debug
    # def visitComando_se(self, ctx):
    #     cond_resultado = self.visit(ctx.condicao())  # retorna _t0 com o resultado de a > b

    #     label_then = self.nova_label()
    #     label_else = self.nova_label()
    #     label_end = self.nova_label()

    #     # if cond_resultado goto label_then
    #     self.add_instrucao(TAC_Instruction("if_goto", dest=label_then, arg1=cond_resultado))

    #     # else (pula direto para o else se condicao for falsa)
    #     self.add_instrucao(TAC_Instruction("goto", dest=label_else))

    #     # bloco THEN
    #     self.add_instrucao(TAC_Instruction("label", dest=label_then))
    #     for comando in ctx.bloco(0).comandos():
    #         self.visit(comando)
    #     self.add_instrucao(TAC_Instruction("goto", dest=label_end))

    #     # bloco ELSE (se existir)
    #     self.add_instrucao(TAC_Instruction("label", dest=label_else))
    #     if ctx.SENAO():
    #         for comando in ctx.bloco(1).comandos():
    #             self.visit(comando)

    #     # fim
    #     self.add_instrucao(TAC_Instruction("label", dest=label_end))


    #sem debug
    # def visitCondicao(self, ctx):
    #     arg1 = self.visit(ctx.expressao(0))
    #     op = ctx.operador().getText()
    #     arg2 = self.visit(ctx.expressao(1))

    #     temp = self.novo_temp()
    #     self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
    #     return temp




    # def visitExpressao(self, ctx):
        filhos = ctx.getChildCount()
        texto = ctx.getText()
        print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

        # EXPRESSAO BINÁRIA: a + b, a - b, etc.
        if filhos == 3 and ctx.getChild(1).getText() in ['+', '-', '*', '/']:
            arg1 = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            arg2 = self.visit(ctx.getChild(2))
            temp = self.novo_temp()
            self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
            print(f"\033[94m[DEBUG] EXPRESSAO: {arg1} {op} {arg2} → {temp}\033[0m")
            return temp

        # EXPRESSAO COM PARÊNTESES: (a + b)
        elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            print("[DEBUG] Parênteses detectado")
            return self.visit(ctx.getChild(1))

        # CHAMADA DE FUNÇÃO: ex: soma(i, 2)
        elif filhos >= 4 and ctx.getChild(1).getText() == "(" and ctx.getChild(filhos - 1).getText() == ")":
            nome_funcao = ctx.getChild(0).getText()
            print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")

            # Captura os argumentos reais (se houver)
            argumentos_ctx = ctx.expressao()
            argumentos = [self.visit(arg) for arg in argumentos_ctx]

            # Emite 'param' para cada argumento
            for arg in argumentos:
                self.add_instrucao(TAC_Instruction("param", arg))
                print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

            # Emite chamada e resultado
            temp = self.novo_temp()
            self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
            print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")

            return temp


        # LITERAL INTEIRO
        elif ctx.INTEIRO():
            valor = ctx.INTEIRO().getText()
            print(f"[DEBUG] INTEIRO: {valor}")
            return TAC_Operand("const", valor)

        # LITERAL FLOAT
        elif ctx.FLOAT():
            valor = ctx.FLOAT().getText()
            print(f"[DEBUG] FLOAT: {valor}")
            return TAC_Operand("const", valor)

        # LITERAL STRING
        elif ctx.STRING():
            valor = ctx.STRING().getText()
            print(f"[DEBUG] STRING: {valor}")
            return TAC_Operand("const", valor)

        # IDENTIFICADOR
        elif ctx.ID():
            nome = ctx.ID().getText()
            print(f"[DEBUG] ID: {nome}")
            return TAC_Operand("var", nome)

        # Fallback
        print("[DEBUG] Visitando filhos como fallback")
        return self.visitChildren(ctx)


    # def visitExpressao(self, ctx):
        filhos = ctx.getChildCount()
        texto = ctx.getText()
        print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

        # EXPRESSÃO BINÁRIA (aritmética, comparação, lógica)
        if filhos == 3:
            esq = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            dir = self.visit(ctx.getChild(2))

            op_validos = ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=', '&&', '||']

            if op in op_validos:
                temp = self.novo_temp()
                self.add_instrucao(TAC_Instruction(op, temp, esq, dir))
                print(f"\033[94m[DEBUG] EXPRESSAO BINARIA: {esq} {op} {dir} → {temp}\033[0m")
                return temp
            else:
                print(f"\033[91m[ERRO SEMÂNTICO] Operador inválido: {op}\033[0m")
                return None

        # EXPRESSÃO COM PARÊNTESES
        elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            print("[DEBUG] EXPRESSAO entre parênteses detectada")
            return self.visit(ctx.getChild(1))

        # LITERAIS
        elif ctx.INTEIRO():
            valor = ctx.INTEIRO().getText()
            print(f"[DEBUG] INTEIRO: {valor}")
            return TAC_Operand("const", valor)

        elif ctx.FLOAT():
            valor = ctx.FLOAT().getText()
            print(f"[DEBUG] FLOAT: {valor}")
            return TAC_Operand("const", valor)

        elif ctx.STRING():
            valor = ctx.STRING().getText()
            print(f"[DEBUG] STRING: {valor}")
            return TAC_Operand("const", valor)

        # VARIÁVEIS
        elif ctx.ID():
            nome = ctx.ID().getText()
            print(f"[DEBUG] ID: {nome}")
            return TAC_Operand("var", nome)

        # CHAMADA DE FUNÇÃO (com args)
        elif filhos >= 4 and ctx.getChild(1).getText() == "(":
            nome_funcao = ctx.getChild(0).getText()
            print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")
            argumentos_ctx = ctx.expressao()
            argumentos = [self.visit(arg) for arg in argumentos_ctx]

            for arg in argumentos:
                self.add_instrucao(TAC_Instruction("param", arg))
                print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

            temp = self.novo_temp()
            self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
            print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")
            return temp

        elif filhos >= 5:
            print("\033[93m[DEBUG] EXPRESSAO COMPLEXA (n >= 5)\033[0m")
            resultado = self.visit(ctx.getChild(0))
            for i in range(1, filhos - 1, 2):
                op = ctx.getChild(i).getText()
                direito = self.visit(ctx.getChild(i + 1))
                temp = self.novo_temp()
                self.add_instrucao(TAC_Instruction(op, temp, resultado, direito))
                print(f"\033[94m[DEBUG] EXPRESSAO ENCADEADA: {resultado} {op} {direito} → {temp}\033[0m")
                resultado = temp
            return resultado

        # Fallback
        print("[DEBUG] Fallback visitChildren")
        return self.visitChildren(ctx)


    # def visitCondicao(self, ctx):
        arg1 = self.visit(ctx.expressao(0))
        op = ctx.operador().getText()
        arg2 = self.visit(ctx.expressao(1))

        temp = self.novo_temp()
        instrucao = TAC_Instruction(op, temp, arg1, arg2)
        self.add_instrucao(instrucao)

        print(f"\033[94m[DEBUG] CONDIÇÃO: {arg1} {op} {arg2} → {temp}\033[0m")
        return temp

    # def visitCondicao(self, ctx):
        filhos = ctx.getChildCount()
        texto = ctx.getText()
        print(f"\033[91m[DEBUG] CONDICAO: {texto} ({filhos} filhos)\033[0m")

        if filhos == 3:
            esq = ctx.getChild(0)
            op = ctx.getChild(1).getText()
            dir = ctx.getChild(2)

            # Recursivamente visita condicoes
            if hasattr(esq, 'condicao') or isinstance(esq, type(ctx)):
                arg1 = self.visit(esq)
            else:
                arg1 = self.visit(esq)

            if hasattr(dir, 'condicao') or isinstance(dir, type(ctx)):
                arg2 = self.visit(dir)
            else:
                arg2 = self.visit(dir)

            temp = self.novo_temp()
            self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
            print(f"\033[92m[DEBUG] CONDICAO BINARIA: {arg1} {op} {arg2} → {temp}\033[0m")
            return temp

        elif filhos == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))

        else:
            print("\033[91m[ERRO] Condição inválida ou não suportada ainda\033[0m")
            return None

#ERRO: faz chamada dublicada de escreva mesmo apos o programa terminar
    # def visitExpressao(self, ctx):
        filhos = ctx.getChildCount()
        texto = ctx.getText()
        print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

        # EXPRESSÃO BINÁRIA (aritmética, comparação, lógica)
        if filhos == 3:
            esq = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            dir = self.visit(ctx.getChild(2))

            op_validos = ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=', '&&', '||']

            if op in op_validos:
                temp = self.novo_temp()
                self.add_instrucao(TAC_Instruction(op, temp, esq, dir))
                print(f"\033[94m[DEBUG] EXPRESSAO BINARIA: {esq} {op} {dir} → {temp}\033[0m")
                return temp
            else:
                print(f"\033[91m[ERRO SEMÂNTICO] Operador inválido: {op}\033[0m")
                return None

        # EXPRESSÃO COM PARÊNTESES
        elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            print("[DEBUG] EXPRESSAO entre parênteses detectada")
            return self.visit(ctx.getChild(1))

        # LITERAIS
        elif ctx.INTEIRO():
            valor = ctx.INTEIRO().getText()
            print(f"[DEBUG] INTEIRO: {valor}")
            return TAC_Operand("const", valor)

        elif ctx.FLOAT():
            valor = ctx.FLOAT().getText()
            print(f"[DEBUG] FLOAT: {valor}")
            return TAC_Operand("const", valor)

        elif ctx.STRING():
            valor = ctx.STRING().getText()
            print(f"[DEBUG] STRING: {valor}")
            return TAC_Operand("const", valor)

        # VARIÁVEIS
        elif ctx.ID():
            nome = ctx.ID().getText()
            print(f"[DEBUG] ID: {nome}")
            return TAC_Operand("var", nome)


        # CHAMADA DE FUNÇÃO (com args)
        elif filhos >= 4 and ctx.getChild(1).getText() == "(":
            nome_funcao = ctx.getChild(0).getText()

            # ⚠️ IGNORAR chamadas a escreva/leia dentro de expressões
            if nome_funcao in ["escreva", "leia"]:
                print(f"\033[93m[AVISO] Ignorando chamada direta a '{nome_funcao}' dentro de expressão\033[0m")
                return None

            print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")
            argumentos_ctx = ctx.expressao()
            argumentos = [self.visit(arg) for arg in argumentos_ctx]

            for arg in argumentos:
                self.add_instrucao(TAC_Instruction("param", arg))
                print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

            temp = self.novo_temp()
            self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
            print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")
            return temp        

        elif filhos >= 5:
            print("\033[93m[DEBUG] EXPRESSAO COMPLEXA (n >= 5)\033[0m")
            resultado = self.visit(ctx.getChild(0))
            for i in range(1, filhos - 1, 2):
                op = ctx.getChild(i).getText()
                direito = self.visit(ctx.getChild(i + 1))
                temp = self.novo_temp()
                self.add_instrucao(TAC_Instruction(op, temp, resultado, direito))
                print(f"\033[94m[DEBUG] EXPRESSAO ENCADEADA: {resultado} {op} {direito} → {temp}\033[0m")
                resultado = temp
            return resultado

        # # Fallback
        # print("[DEBUG] Fallback visitChildren")
        # return self.visitChildren(ctx)
        # Fallback: retorna None se nenhuma das condições acima se aplicar
        print("[DEBUG] Nenhuma correspondência na expressão — retornando None")
        return None


    # def visitCondicao(self, ctx):
        arg1 = self.visit(ctx.expressao(0))
        op = ctx.operador().getText()
        arg2 = self.visit(ctx.expressao(1))

        temp = self.novo_temp()
        instrucao = TAC_Instruction(op, temp, arg1, arg2)
        self.add_instrucao(instrucao)

        print(f"\033[94m[DEBUG] CONDIÇÃO: {arg1} {op} {arg2} → {temp}\033[0m")
        return temp


# #ERRO:na chamada de funcao, ele trata uma funcao como uma variavel
#     def visitExpressao(self, ctx):
#         filhos = ctx.getChildCount()
#         texto = ctx.getText()
#         print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

#         # EXPRESSÃO BINÁRIA (aritmética, comparação, lógica)
#         if filhos == 3:
#             esq = self.visit(ctx.getChild(0))
#             op = ctx.getChild(1).getText()
#             dir = self.visit(ctx.getChild(2))

#             op_validos = ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=', '&&', '||']

#             if op in op_validos:
#                 temp = self.novo_temp()
#                 self.add_instrucao(TAC_Instruction(op, temp, esq, dir))
#                 print(f"\033[94m[DEBUG] EXPRESSAO BINARIA: {esq} {op} {dir} → {temp}\033[0m")
#                 return temp
#             else:
#                 print(f"\033[91m[ERRO SEMÂNTICO] Operador inválido: {op}\033[0m")
#                 return None

#         # EXPRESSÃO COM PARÊNTESES
#         elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
#             print("[DEBUG] EXPRESSAO entre parênteses detectada")
#             return self.visit(ctx.getChild(1))

#         # LITERAIS
#         elif ctx.INTEIRO():
#             valor = ctx.INTEIRO().getText()
#             print(f"[DEBUG] INTEIRO: {valor}")
#             return TAC_Operand("const", valor)

#         elif ctx.FLOAT():
#             valor = ctx.FLOAT().getText()
#             print(f"[DEBUG] FLOAT: {valor}")
#             return TAC_Operand("const", valor)

#         elif ctx.STRING():
#             valor = ctx.STRING().getText()
#             print(f"[DEBUG] STRING: {valor}")
#             return TAC_Operand("const", valor)

#         # VARIÁVEIS
#         elif ctx.ID():
#             nome = ctx.ID().getText()
#             print(f"[DEBUG] ID: {nome}")
#             return TAC_Operand("var", nome)

#         # CHAMADA DE FUNÇÃO (com argumentos)
#         elif filhos >= 4 and ctx.getChild(1).getText() == "(":
#             nome_funcao = ctx.getChild(0).getText()

#             # ⚠️ Evitar interpretar escreva/leia como chamada de função
#             if nome_funcao in ["escreva", "leia"]:
#                 print(f"\033[93m[AVISO] Ignorando chamada direta a '{nome_funcao}' dentro de expressão\033[0m")
#                 return None

#             print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")
#             argumentos_ctx = ctx.expressao()
#             argumentos = [self.visit(arg) for arg in argumentos_ctx]

#             for arg in argumentos:
#                 self.add_instrucao(TAC_Instruction("param", arg))
#                 print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

#             temp = self.novo_temp()
#             self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
#             print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")
#             return temp

#         # EXPRESSÕES ENCADEADAS: ex: a + b + c + d
#         elif filhos >= 5:
#             print("\033[93m[DEBUG] EXPRESSAO COMPLEXA (n >= 5)\033[0m")
#             resultado = self.visit(ctx.getChild(0))
#             for i in range(1, filhos - 1, 2):
#                 op = ctx.getChild(i).getText()
#                 direito = self.visit(ctx.getChild(i + 1))
#                 temp = self.novo_temp()
#                 self.add_instrucao(TAC_Instruction(op, temp, resultado, direito))
#                 print(f"\033[94m[DEBUG] EXPRESSAO ENCADEADA: {resultado} {op} {direito} → {temp}\033[0m")
#                 resultado = temp
#             return resultado

#         # Fallback: evita chamada recursiva perigosa
#         print("[DEBUG] Nenhuma correspondência na expressão — retornando None")
#         return None

    # def visitExpressao(self, ctx):
    #     filhos = ctx.getChildCount()
    #     texto = ctx.getText()
    #     print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

    #     # EXPRESSÃO BINÁRIA (aritmética, comparação, lógica)
    #     if filhos == 3:
    #         esq = self.visit(ctx.getChild(0))
    #         op = ctx.getChild(1).getText()
    #         dir = self.visit(ctx.getChild(2))

    #         op_validos = ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=', '&&', '||']

    #         if op in op_validos:
    #             temp = self.novo_temp()
    #             self.add_instrucao(TAC_Instruction(op, temp, esq, dir))
    #             print(f"\033[94m[DEBUG] EXPRESSAO BINARIA: {esq} {op} {dir} → {temp}\033[0m")
    #             return temp
    #         else:
    #             print(f"\033[91m[ERRO SEMÂNTICO] Operador inválido: {op}\033[0m")
    #             return None

    #     # EXPRESSÃO COM PARÊNTESES
    #     elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
    #         print("[DEBUG] EXPRESSAO entre parênteses detectada")
    #         return self.visit(ctx.getChild(1))

    #     # LITERAIS
    #     elif ctx.INTEIRO():
    #         valor = ctx.INTEIRO().getText()
    #         print(f"[DEBUG] INTEIRO: {valor}")
    #         return TAC_Operand("const", valor)

    #     elif ctx.FLOAT():
    #         valor = ctx.FLOAT().getText()
    #         print(f"[DEBUG] FLOAT: {valor}")
    #         return TAC_Operand("const", valor)

    #     elif ctx.STRING():
    #         valor = ctx.STRING().getText()
    #         print(f"[DEBUG] STRING: {valor}")
    #         return TAC_Operand("const", valor)

    #     # IDENTIFICADOR (variável simples)
    #     elif ctx.ID() and not ctx.expressao():  # evitar confusão com chamada de função
    #         nome = ctx.ID().getText()
    #         print(f"[DEBUG] ID: {nome}")
    #         return TAC_Operand("var", nome)

    #     # CHAMADA DE FUNÇÃO (forma robusta)
    #     elif ctx.ID() and ctx.getChildCount() >= 4 and ctx.getChild(1).getText() == "(":
    #         nome_funcao = ctx.ID().getText()

    #         if nome_funcao in ["escreva", "leia"]:
    #             print(f"\033[93m[AVISO] Ignorando chamada direta a '{nome_funcao}' dentro de expressão\033[0m")
    #             return None

    #         print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")

    #         argumentos_ctx = ctx.expressao() or []
    #         argumentos = [self.visit(arg) for arg in argumentos_ctx]

    #         for arg in argumentos:
    #             self.add_instrucao(TAC_Instruction("param", arg))
    #             print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

    #         temp = self.novo_temp()
    #         self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
    #         print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")
    #         return temp

    #     # EXPRESSÕES ENCADEADAS: ex: a + b + c + d
    #     elif filhos >= 5:
    #         print("\033[93m[DEBUG] EXPRESSAO COMPLEXA (n >= 5)\033[0m")
    #         resultado = self.visit(ctx.getChild(0))
    #         for i in range(1, filhos - 1, 2):
    #             op = ctx.getChild(i).getText()
    #             direito = self.visit(ctx.getChild(i + 1))
    #             temp = self.novo_temp()
    #             self.add_instrucao(TAC_Instruction(op, temp, resultado, direito))
    #             print(f"\033[94m[DEBUG] EXPRESSAO ENCADEADA: {resultado} {op} {direito} → {temp}\033[0m")
    #             resultado = temp
    #         return resultado

    #     # Fallback
    #     print("\033[93m[DEBUG] Fallback: expressão não reconhecida\033[0m")
    #     return None


    # def visitExpressao(self, ctx):
    #     filhos = ctx.getChildCount()
    #     texto = ctx.getText()
    #     print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

    #     # EXPRESSÃO BINÁRIA (aritmética, comparação, lógica)
    #     if filhos == 3:
    #         esq = self.visit(ctx.getChild(0))
    #         op = ctx.getChild(1).getText()
    #         dir = self.visit(ctx.getChild(2))

    #         op_validos = ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=', '&&', '||']
    #         if op in op_validos:
    #             temp = self.novo_temp()
    #             self.add_instrucao(TAC_Instruction(op, temp, esq, dir))
    #             print(f"\033[94m[DEBUG] EXPRESSAO BINARIA: {esq} {op} {dir} → {temp}\033[0m")
    #             return temp
    #         else:
    #             print(f"\033[91m[ERRO SEMÂNTICO] Operador inválido: {op}\033[0m")
    #             return None

    #     # EXPRESSÃO COM PARÊNTESES
    #     elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
    #         print("[DEBUG] EXPRESSAO entre parênteses detectada")
    #         return self.visit(ctx.getChild(1))

    #     # LITERAIS
    #     elif ctx.INTEIRO():
    #         valor = ctx.INTEIRO().getText()
    #         print(f"[DEBUG] INTEIRO: {valor}")
    #         return TAC_Operand("const", valor)

    #     elif ctx.FLOAT():
    #         valor = ctx.FLOAT().getText()
    #         print(f"[DEBUG] FLOAT: {valor}")
    #         return TAC_Operand("const", valor)

    #     elif ctx.STRING():
    #         valor = ctx.STRING().getText()
    #         print(f"[DEBUG] STRING: {valor}")
    #         return TAC_Operand("const", valor)

    #     # VARIÁVEIS
    #     # elif ctx.ID() and not ctx.lista_argumentos():  # evitar confusão com chamada de função
    #     elif ctx.ID() and not hasattr(ctx, "lista_argumentos"):
    #         nome = ctx.ID().getText()
    #         print(f"[DEBUG] ID: {nome}")
    #         return TAC_Operand("var", nome)

    #     # CHAMADA DE FUNÇÃO
    #     elif ctx.ID() and ctx.getChildCount() >= 4 and ctx.getChild(1).getText() == "(":
    #         nome_funcao = ctx.ID().getText()

    #         if nome_funcao in ["escreva", "leia"]:
    #             print(f"\033[93m[AVISO] Ignorando chamada direta a '{nome_funcao}' dentro de expressão\033[0m")
    #             return None

    #         print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")

    #         argumentos_ctx = ctx.lista_argumentos()
    #         argumentos = []

    #         if argumentos_ctx:
    #             for expressao_ctx in argumentos_ctx.expressao():
    #                 arg = self.visit(expressao_ctx)
    #                 argumentos.append(arg)
    #                 self.add_instrucao(TAC_Instruction("param", arg))
    #                 print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

    #         temp = self.novo_temp()
    #         self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
    #         print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")
    #         return temp

    #     # EXPRESSÃO ENCADEADA: ex: a + b + c + d
    #     elif filhos >= 5:
    #         print("\033[93m[DEBUG] EXPRESSAO COMPLEXA (n >= 5)\033[0m")
    #         resultado = self.visit(ctx.getChild(0))
    #         for i in range(1, filhos - 1, 2):
    #             op = ctx.getChild(i).getText()
    #             direito = self.visit(ctx.getChild(i + 1))
    #             temp = self.novo_temp()
    #             self.add_instrucao(TAC_Instruction(op, temp, resultado, direito))
    #             print(f"\033[94m[DEBUG] EXPRESSAO ENCADEADA: {resultado} {op} {direito} → {temp}\033[0m")
    #             resultado = temp
    #         return resultado

    #     # Fallback
    #     print("\033[93m[DEBUG] Fallback: expressão não reconhecida\033[0m")
    #     return None

# #ERRO: no acesso aos argumentos passados pelas funcoes
#     def visitExpressao(self, ctx):
#         filhos = ctx.getChildCount()
#         texto = ctx.getText()
#         print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

#         # EXPRESSÃO BINÁRIA (aritmética, comparação, lógica)
#         if filhos == 3:
#             esq = self.visit(ctx.getChild(0))
#             op = ctx.getChild(1).getText()
#             dir = self.visit(ctx.getChild(2))

#             op_validos = ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=', '&&', '||']
#             if op in op_validos:
#                 temp = self.novo_temp()
#                 self.add_instrucao(TAC_Instruction(op, temp, esq, dir))
#                 print(f"\033[94m[DEBUG] EXPRESSAO BINARIA: {esq} {op} {dir} → {temp}\033[0m")
#                 return temp
#             else:
#                 print(f"\033[91m[ERRO SEMÂNTICO] Operador inválido: {op}\033[0m")
#                 return None

#         # EXPRESSÃO COM PARÊNTESES
#         elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
#             print("[DEBUG] EXPRESSAO entre parênteses detectada")
#             return self.visit(ctx.getChild(1))

#         # LITERAIS
#         elif ctx.INTEIRO():
#             valor = ctx.INTEIRO().getText()
#             print(f"[DEBUG] INTEIRO: {valor}")
#             return TAC_Operand("const", valor)

#         elif ctx.FLOAT():
#             valor = ctx.FLOAT().getText()
#             print(f"[DEBUG] FLOAT: {valor}")
#             return TAC_Operand("const", valor)

#         elif ctx.STRING():
#             valor = ctx.STRING().getText()
#             print(f"[DEBUG] STRING: {valor}")
#             return TAC_Operand("const", valor)

#         # VARIÁVEIS (identificadores simples)
#         elif ctx.ID() and ctx.getChildCount() == 1:
#             nome = ctx.ID().getText()
#             print(f"[DEBUG] ID: {nome}")
#             return TAC_Operand("var", nome)

#         # CHAMADA DE FUNÇÃO: ID '(' lista_argumentos? ')'
#         elif ctx.ID() and ctx.getChildCount() >= 3 and ctx.getChild(1).getText() == "(":
#             nome_funcao = ctx.ID().getText()

#             if nome_funcao in ["escreva", "leia"]:
#                 print(f"\033[93m[AVISO] Ignorando chamada direta a '{nome_funcao}' dentro de expressão\033[0m")
#                 return None

#             print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")

#             argumentos = []
#             if ctx.lista_argumentos():
#                 for exp_ctx in ctx.lista_argumentos().expressao():
#                     arg = self.visit(exp_ctx)
#                     argumentos.append(arg)
#                     self.add_instrucao(TAC_Instruction("param", arg))
#                     print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

#             temp = self.novo_temp()
#             self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
#             print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")
#             return temp

#         # EXPRESSÕES ENCADEADAS: ex: a + b + c + d
#         elif filhos >= 5:
#             print("\033[93m[DEBUG] EXPRESSAO COMPLEXA (n >= 5)\033[0m")
#             resultado = self.visit(ctx.getChild(0))
#             for i in range(1, filhos - 1, 2):
#                 op = ctx.getChild(i).getText()
#                 direito = self.visit(ctx.getChild(i + 1))
#                 temp = self.novo_temp()
#                 self.add_instrucao(TAC_Instruction(op, temp, resultado, direito))
#                 print(f"\033[94m[DEBUG] EXPRESSAO ENCADEADA: {resultado} {op} {direito} → {temp}\033[0m")
#                 resultado = temp
#             return resultado

#         # Fallback
#         print("\033[93m[DEBUG] Fallback: expressão não reconhecida\033[0m")
#         return None


    # def visitExpressao(self, ctx):
    #     filhos = ctx.getChildCount()
    #     texto = ctx.getText()
    #     print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

    #     # EXPRESSÃO BINÁRIA (aritmética, comparação, lógica)
    #     if filhos == 3:
    #         esq = self.visit(ctx.getChild(0))
    #         op = ctx.getChild(1).getText()
    #         dir = self.visit(ctx.getChild(2))

    #         op_validos = ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=', '&&', '||']
    #         if op in op_validos:
    #             temp = self.novo_temp()
    #             self.add_instrucao(TAC_Instruction(op, temp, esq, dir))
    #             print(f"\033[94m[DEBUG] EXPRESSAO BINARIA: {esq} {op} {dir} → {temp}\033[0m")
    #             return temp
    #         else:
    #             print(f"\033[91m[ERRO SEMÂNTICO] Operador inválido: {op}\033[0m")
    #             return None

    #     # EXPRESSÃO COM PARÊNTESES
    #     elif filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
    #         print("[DEBUG] EXPRESSAO entre parênteses detectada")
    #         return self.visit(ctx.getChild(1))

    #     # LITERAIS
    #     elif ctx.INTEIRO():
    #         valor = ctx.INTEIRO().getText()
    #         print(f"[DEBUG] INTEIRO: {valor}")
    #         return TAC_Operand("const", valor)

    #     elif ctx.FLOAT():
    #         valor = ctx.FLOAT().getText()
    #         print(f"[DEBUG] FLOAT: {valor}")
    #         return TAC_Operand("const", valor)

    #     elif ctx.STRING():
    #         valor = ctx.STRING().getText()
    #         print(f"[DEBUG] STRING: {valor}")
    #         return TAC_Operand("const", valor)

    #     # VARIÁVEIS (evita conflito com chamadas de função)
    #     elif ctx.ID() and not hasattr(ctx, "lista_argumentos"):
    #         nome = ctx.ID().getText()
    #         print(f"[DEBUG] ID: {nome}")
    #         return TAC_Operand("var", nome)

    #     # CHAMADA DE FUNÇÃO COM ARGUMENTOS
    #     elif ctx.ID() and ctx.getChildCount() >= 4 and ctx.getChild(1).getText() == "(":
    #         nome_funcao = ctx.ID().getText()

    #         if nome_funcao in ["escreva", "leia"]:
    #             print(f"\033[93m[AVISO] Ignorando chamada direta a '{nome_funcao}' dentro de expressão\033[0m")
    #             return None

    #         print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")

    #         argumentos = []
    #         argumentos_ctx = getattr(ctx, "lista_argumentos", None)

    #         if callable(argumentos_ctx):
    #             argumentos_ctx = argumentos_ctx()
    #             for expressao_ctx in argumentos_ctx.expressao():
    #                 arg = self.visit(expressao_ctx)
    #                 argumentos.append(arg)
    #                 self.add_instrucao(TAC_Instruction("param", arg))
    #                 print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

    #         temp = self.novo_temp()
    #         self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
    #         print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")
    #         return temp

    #     # EXPRESSÕES ENCADEADAS: ex: a + b + c + d
    #     elif filhos >= 5:
    #         print("\033[93m[DEBUG] EXPRESSAO COMPLEXA (n >= 5)\033[0m")
    #         resultado = self.visit(ctx.getChild(0))
    #         for i in range(1, filhos - 1, 2):
    #             op = ctx.getChild(i).getText()
    #             direito = self.visit(ctx.getChild(i + 1))
    #             temp = self.novo_temp()
    #             self.add_instrucao(TAC_Instruction(op, temp, resultado, direito))
    #             print(f"\033[94m[DEBUG] EXPRESSAO ENCADEADA: {resultado} {op} {direito} → {temp}\033[0m")
    #             resultado = temp
    #         return resultado

    #     # Fallback
    #     print("\033[93m[DEBUG] Fallback: expressão não reconhecida\033[0m")
    #     return None


    def visitExpressao(self, ctx):
        filhos = ctx.getChildCount()
        texto = ctx.getText()
        print(f"[DEBUG] EXPRESSAO: {texto} ({filhos} filhos)")

        # EXPRESSÃO COM PARÊNTESES: (expr)
        if filhos == 3 and ctx.getChild(0).getText() == '(' and ctx.getChild(2).getText() == ')':
            print("[DEBUG] EXPRESSAO entre parênteses detectada")
            return self.visit(ctx.getChild(1))

        # EXPRESSÃO BINÁRIA (a op b) — SEM parênteses explícitos
        elif filhos == 3:
            esquerda = self.visit(ctx.getChild(0))
            operador = ctx.getChild(1).getText()
            direita = self.visit(ctx.getChild(2))

            op_validos = ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=', '&&', '||']
            if operador in op_validos:
                temp = self.novo_temp()
                self.add_instrucao(TAC_Instruction(operador, temp, esquerda, direita))
                print(f"\033[94m[DEBUG] EXPRESSAO BINARIA: {esquerda} {operador} {direita} → {temp}\033[0m")
                return temp
            else:
                print(f"\033[91m[ERRO SEMÂNTICO] Operador inválido: {operador}\033[0m")
                return None

        # LITERAIS
        elif ctx.INTEIRO():
            valor = ctx.INTEIRO().getText()
            print(f"[DEBUG] INTEIRO: {valor}")
            return TAC_Operand("const", valor)

        elif ctx.FLOAT():
            valor = ctx.FLOAT().getText()
            print(f"[DEBUG] FLOAT: {valor}")
            return TAC_Operand("const", valor)

        elif ctx.STRING():
            valor = ctx.STRING().getText()
            print(f"[DEBUG] STRING: {valor}")
            return TAC_Operand("const", valor)

        # IDENTIFICADOR (variável simples)
        elif ctx.ID() and not hasattr(ctx, "lista_argumentos"):
            nome = ctx.ID().getText()
            print(f"[DEBUG] ID: {nome}")
            return TAC_Operand("var", nome)

        # CHAMADA DE FUNÇÃO COM ARGUMENTOS
        elif ctx.ID() and ctx.getChildCount() >= 4 and ctx.getChild(1).getText() == "(":
            nome_funcao = ctx.ID().getText()

            if nome_funcao in ["escreva", "leia"]:
                print(f"\033[93m[AVISO] Ignorando chamada direta a '{nome_funcao}' dentro de expressão\033[0m")
                return None

            print(f"\033[94m[DEBUG] INICIANDO CHAMADA DE FUNÇÃO: {nome_funcao}\033[0m")

            argumentos = []
            argumentos_ctx = getattr(ctx, "lista_argumentos", None)
            if callable(argumentos_ctx):
                argumentos_ctx = argumentos_ctx()
                for expressao_ctx in argumentos_ctx.expressao():
                    arg = self.visit(expressao_ctx)
                    argumentos.append(arg)
                    self.add_instrucao(TAC_Instruction("param", arg))
                    print(f"\033[94m[DEBUG] ARG → param {arg}\033[0m")

            temp = self.novo_temp()
            self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
            print(f"\033[94m[DEBUG] FUNÇÃO → {temp} = call {nome_funcao}({len(argumentos)} args)\033[0m")
            return temp

        # EXPRESSÕES COMPOSTAS/ENCADEADAS COM 5 OU MAIS FILHOS
        elif filhos >= 5:
            print(f"\033[93m[DEBUG] EXPRESSAO ENCADEADA COMPLEXA (n={filhos})\033[0m")
            atual = self.visit(ctx.getChild(0))

            i = 1
            while i < filhos - 1:
                operador = ctx.getChild(i).getText()
                proxima = self.visit(ctx.getChild(i + 1))
                temp = self.novo_temp()
                self.add_instrucao(TAC_Instruction(operador, temp, atual, proxima))
                print(f"\033[94m[DEBUG] EXPRESSAO ENCADEADA: {atual} {operador} {proxima} → {temp}\033[0m")
                atual = temp
                i += 2

            return atual

        # Fallback (casos não tratados)
        print("\033[93m[DEBUG] Fallback: expressão não reconhecida\033[0m")
        return None

    
    def visitCondicao(self, ctx):
        filhos = ctx.getChildCount()
        texto = ctx.getText()
        print(f"\033[91m[DEBUG] CONDICAO: {texto} ({filhos} filhos)\033[0m")

        if filhos == 3:
            esq = ctx.getChild(0)
            op = ctx.getChild(1).getText()
            dir = ctx.getChild(2)

            # Recursivamente visita condicoes
            if hasattr(esq, 'condicao') or isinstance(esq, type(ctx)):
                arg1 = self.visit(esq)
            else:
                arg1 = self.visit(esq)

            if hasattr(dir, 'condicao') or isinstance(dir, type(ctx)):
                arg2 = self.visit(dir)
            else:
                arg2 = self.visit(dir)

            temp = self.novo_temp()
            self.add_instrucao(TAC_Instruction(op, temp, arg1, arg2))
            print(f"\033[92m[DEBUG] CONDICAO BINARIA: {arg1} {op} {arg2} → {temp}\033[0m")
            return temp

        elif filhos == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))

        else:
            print("\033[91m[ERRO] Condição inválida ou não suportada ainda\033[0m")
            return None

    def visitComando_se(self, ctx):
        print("\033[96m[DEBUG] INICIANDO 'se'\033[0m")
        cond_resultado = self.visit(ctx.condicao())  # _t0

        label_then = self.nova_label()
        label_else = self.nova_label()
        label_end = self.nova_label()

        print(f"\033[96m[DEBUG] Labels: THEN={label_then}, ELSE={label_else}, END={label_end}\033[0m")

        self.add_instrucao(TAC_Instruction("if_goto", dest=label_then, arg1=cond_resultado))
        self.add_instrucao(TAC_Instruction("goto", dest=label_else))

        self.add_instrucao(TAC_Instruction("label", dest=label_then))
        print("\033[96m[DEBUG] Visitando bloco THEN\033[0m")
        for comando in ctx.bloco(0).comandos():
            self.visit(comando)
        self.add_instrucao(TAC_Instruction("goto", dest=label_end))

        self.add_instrucao(TAC_Instruction("label", dest=label_else))
        if ctx.SENAO():
            print("\033[96m[DEBUG] Visitando bloco ELSE\033[0m")
            for comando in ctx.bloco(1).comandos():
                self.visit(comando)

        self.add_instrucao(TAC_Instruction("label", dest=label_end))
        print("\033[96m[DEBUG] Finalizando 'se'\033[0m")

    def visitComando_se(self, ctx):
        print("\033[96m[DEBUG] INICIANDO 'se'\033[0m")
        cond_resultado = self.visit(ctx.condicao())  # _t0

        label_then = self.nova_label()
        label_else = self.nova_label()
        label_end = self.nova_label()

        print(f"\033[96m[DEBUG] Labels: THEN={label_then}, ELSE={label_else}, END={label_end}\033[0m")

        self.add_instrucao(TAC_Instruction("if_goto", dest=label_then, arg1=cond_resultado))
        self.add_instrucao(TAC_Instruction("goto", dest=label_else))

        self.add_instrucao(TAC_Instruction("label", dest=label_then))
        print("\033[96m[DEBUG] Visitando bloco THEN\033[0m")
        for comando in ctx.bloco(0).comandos():
            self.visit(comando)
        self.add_instrucao(TAC_Instruction("goto", dest=label_end))

        self.add_instrucao(TAC_Instruction("label", dest=label_else))
        if ctx.SENAO():
            print("\033[96m[DEBUG] Visitando bloco ELSE\033[0m")
            for comando in ctx.bloco(1).comandos():
                self.visit(comando)

        self.add_instrucao(TAC_Instruction("label", dest=label_end))
        print("\033[96m[DEBUG] Finalizando 'se'\033[0m")



    #sem debug
    # def visitComando_enquanto(self, ctx):
    #     label_inicio = self.nova_label()
    #     label_fim = self.nova_label()

    #     self.add_instrucao(TAC_Instruction("label", dest=label_inicio))

    #     cond = self.visit(ctx.condicao())
    #     self.add_instrucao(TAC_Instruction("if_goto", dest=label_fim, arg1=TAC_Operand("cond_invert", cond.valor)))

    #     for comando in ctx.bloco().comandos():
    #         self.visit(comando)

    #     self.add_instrucao(TAC_Instruction("goto", dest=label_inicio))
    #     self.add_instrucao(TAC_Instruction("label", dest=label_fim))


    # def visitComando_enquanto(self, ctx):
    #     print("\033[95m[DEBUG] INICIANDO 'enquanto'\033[0m")

    #     label_inicio = self.nova_label()
    #     label_fim = self.nova_label()

    #     print(f"\033[95m[DEBUG] Labels: INICIO={label_inicio}, FIM={label_fim}\033[0m")

    #     # Ponto de repetição
    #     self.add_instrucao(TAC_Instruction("label", dest=label_inicio))

    #     # Visita a condição
    #     cond_resultado = self.visit(ctx.condicao())  # _t0
    #     print(f"\033[95m[DEBUG] CONDICAO: {cond_resultado}\033[0m")

    #     # Se a condição for falsa, salta para o fim
    #     self.add_instrucao(TAC_Instruction("if_goto", dest=label_fim, arg1=TAC_Operand("cond_invert", cond_resultado.valor)))

    #     # Bloco do corpo
    #     print("\033[95m[DEBUG] Visitando bloco do 'enquanto'\033[0m")
    #     for comando in ctx.bloco().comandos():
    #         self.visit(comando)

    #     # Volta para o início
    #     self.add_instrucao(TAC_Instruction("goto", dest=label_inicio))

    #     # Marca o fim do laço
    #     self.add_instrucao(TAC_Instruction("label", dest=label_fim))
    #     print("\033[95m[DEBUG] Finalizando 'enquanto'\033[0m")


    # def visitComando_enquanto(self, ctx):
    #     print("\033[95m[DEBUG] INICIANDO 'enquanto'\033[0m")

    #     label_inicio = self.nova_label()
    #     label_fim = self.nova_label()

    #     print(f"\033[95m[DEBUG] Labels: INICIO={label_inicio}, FIM={label_fim}\033[0m")

    #     # Marca o início do laço
    #     self.add_instrucao(TAC_Instruction("label", dest=label_inicio))

    #     # Visita a condição e gera o teste
    #     cond_resultado = self.visit(ctx.condicao())  # _t0, _t1, etc.
    #     print(f"\033[95m[DEBUG] CONDICAO: {cond_resultado}\033[0m")

    #     # Gera salto para fora do laço se a condição for FALSA
    #     self.add_instrucao(TAC_Instruction("if_false", dest=label_fim, arg1=cond_resultado))

    #     # Bloco do corpo do laço
    #     print("\033[95m[DEBUG] Visitando bloco do 'enquanto'\033[0m")
    #     for comando in ctx.bloco().comandos():
    #         self.visit(comando)

    #     # Volta ao início
    #     self.add_instrucao(TAC_Instruction("goto", dest=label_inicio))

    #     # Marca o fim do laço
    #     self.add_instrucao(TAC_Instruction("label", dest=label_fim))
    #     print("\033[95m[DEBUG] Finalizando 'enquanto'\033[0m")


    def visitComando_enquanto(self, ctx):
        print("\033[95m[DEBUG] INICIANDO 'enquanto'\033[0m")

        label_inicio = self.nova_label()
        label_fim = self.nova_label()

        print(f"\033[95m[DEBUG] Labels: INICIO={label_inicio}, FIM={label_fim}\033[0m")

        self.add_instrucao(TAC_Instruction("label", dest=label_inicio))

        cond_resultado = self.visit(ctx.condicao())
        print(f"\033[95m[DEBUG] CONDICAO: {cond_resultado}\033[0m")

        # Correção: if_false condicao goto FIM
        self.add_instrucao(TAC_Instruction("if_false", dest=label_fim, arg1=cond_resultado))

        print("\033[95m[DEBUG] Visitando bloco do 'enquanto'\033[0m")
        for comando in ctx.bloco().comandos():
            self.visit(comando)

        self.add_instrucao(TAC_Instruction("goto", dest=label_inicio))
        self.add_instrucao(TAC_Instruction("label", dest=label_fim))
        print("\033[95m[DEBUG] Finalizando 'enquanto'\033[0m")

    

    # def visitComando_para(self, ctx):
    #     self.visit(ctx.atribuicao())  # int i = 0

    #     label_cond = self.nova_label()
    #     label_fim = self.nova_label()

    #     self.add_instrucao(TAC_Instruction("label", dest=label_cond))
    #     cond = self.visit(ctx.condicao())
    #     self.add_instrucao(TAC_Instruction("if_goto", dest=label_fim, arg1=TAC_Operand("cond_invert", cond.valor)))

    #     for comando in ctx.bloco().comandos():
    #         self.visit(comando)

    #     self.visit(ctx.incremento())
    #     self.add_instrucao(TAC_Instruction("goto", dest=label_cond))
    #     self.add_instrucao(TAC_Instruction("label", dest=label_fim))

    def visitComando_para(self, ctx):
        self.visit(ctx.atribuicao())  # inicialização

        label_cond = self.nova_label()
        label_fim = self.nova_label()

        self.add_instrucao(TAC_Instruction("label", dest=label_cond))

        cond = self.visit(ctx.condicao())
        # Correção aqui
        self.add_instrucao(TAC_Instruction("if_false", dest=label_fim, arg1=cond))

        for comando in ctx.bloco().comandos():
            self.visit(comando)

        self.visit(ctx.incremento())
        self.add_instrucao(TAC_Instruction("goto", dest=label_cond))
        self.add_instrucao(TAC_Instruction("label", dest=label_fim))


    # def visitComando_retorna(self, ctx):
    #     valor = self.visit(ctx.expressao())
    #     self.add_instrucao(TAC_Instruction("return", arg1=valor))

    # def visitComando_retorno(self, ctx):
    #     valor = self.visit(ctx.expressao())
    #     self.add_instrucao(TAC_Instruction("return", arg1=valor))
    #     print(f"\033[92m[DEBUG] RETORNO: return {valor}\033[0m")

    # def visitComando_retorno(self, ctx):
    #     print(f"\033[92m[DEBUG] ENTRANDO EM visitComando_retorno\033[0m")
    #     valor = self.visit(ctx.expressao())
    #     self.add_instrucao(TAC_Instruction("return", arg1=valor))
    #     print(f"\033[92m[DEBUG] RETORNO: return {valor}\033[0m")

    def visitComando_retorno(self, ctx):
        print(f"\033[92m[DEBUG] ENTRANDO EM visitComando_retorno\033[0m")

        valor = self.visit(ctx.expressao()) if ctx.expressao() else None

        if valor:
            self.add_instrucao(TAC_Instruction("return", arg1=valor))
            print(f"\033[92m[DEBUG] RETORNO: return {valor}\033[0m")
        else:
            self.add_instrucao(TAC_Instruction("return"))
            print("\033[91m[ERRO SEMÂNTICO] Retorno sem valor detectado!\033[0m")

    # def visitBloco(self, ctx):
    #     for comando in ctx.comandos():
    #         self.visit(comando)

    #     if ctx.comando_retorno():
    #         self.visit(ctx.comando_retorno())

    def visitBloco(self, ctx):
        print("\033[96m[DEBUG] Entrando em bloco comum\033[0m")
        
        for comando in ctx.comandos():
            self.visit(comando)

        if ctx.comando_retorno():
            print("\033[91m[AVISO] Retorno inesperado em bloco comum!\033[0m")
            self.visit(ctx.comando_retorno())

    # def visitBloco_funcao(self, ctx):
    #     for comando in ctx.comandos():
    #         self.visit(comando)

    #     self.visit(ctx.comando_retorno())

    def visitBloco_funcao(self, ctx):
        print("\033[96m[DEBUG] Entrando em bloco de função\033[0m")
        
        for comando in ctx.comandos():
            self.visit(comando)

        print("\033[96m[DEBUG] Visitando retorno da função\033[0m")
        self.visit(ctx.comando_retorno())



    def visitComando_declaracao_funcao(self, ctx):
        nome = ctx.ID().getText()
        print(f"\033[96m[DEBUG] FUNÇÃO: {nome}()\033[0m")

        self.add_instrucao(TAC_Instruction("func", dest=TAC_Operand("label", nome)))

        self.visit(ctx.bloco_funcao())

        self.add_instrucao(TAC_Instruction("endfunc"))
        print(f"\033[96m[DEBUG] FIM DA FUNÇÃO: {nome}()\033[0m")


    # def visitComando_escrever(self, ctx):
    #     print(f"\033[95m[DEBUG] ENTRANDO EM visitComando_escrever\033[0m")

    #     # valor = self.visit(ctx.expressao())
    #     valor = self.visit(ctx.getChild(2))  # Posição da expressao no nó: escreva ( expressao )
    #     self.add_instrucao(TAC_Instruction("param", arg1=valor))
    #     self.add_instrucao(TAC_Instruction("call", dest=None, arg1=TAC_Operand("func", "escreva")))

    #     print(f"\033[95m[DEBUG] ESCREVA: escreva({valor})\033[0m")

    # def visitComando_escrever(self, ctx):
    #     print(f"\033[94m[DEBUG] ENTRANDO EM visitComando_escrever\033[0m")

    #     filho = ctx.getChild(2)  # filho pode ser uma expressão ou um STRING

    #     if filho.getSymbol().type == ctx.parser.STRING:
    #         valor = TAC_Operand("const", filho.getText())
    #         print(f"\033[94m[DEBUG] STRING em escreva: {valor}\033[0m")
    #     else:
    #         valor = self.visit(filho)
    #         print(f"\033[94m[DEBUG] EXPRESSAO em escreva: {valor}\033[0m")

    #     self.add_instrucao(TAC_Instruction("param", arg1=valor))
    #     self.add_instrucao(TAC_Instruction("call", dest=None, arg1=TAC_Operand("func", "escreva")))

    #     print(f"\033[94m[DEBUG] ESCREVA: escreva({valor})\033[0m")


    # def visitComando_escrever(self, ctx):
    #     print("\033[92m[DEBUG] ENTRANDO EM visitComando_escrever\033[0m")

    #     if ctx.STRING():
    #         valor = ctx.STRING().getText()
    #         print(f"\033[92m[DEBUG] STRING em escreva: {valor}\033[0m")
    #         self.add_instrucao(TAC_Instruction("print", TAC_Operand("const", valor)))
    #     elif ctx.expressao():
    #         resultado = self.visit(ctx.expressao())
    #         self.add_instrucao(TAC_Instruction("print", resultado))
    #         print(f"\033[92m[DEBUG] ESCREVA: escreva({resultado})\033[0m")


    def visitComando_escrever(self, ctx):
        print("\033[92m[DEBUG] ENTRANDO EM visitComando_escrever\033[0m")

        if ctx.STRING():
            valor = ctx.STRING().getText()
            print(f"\033[92m[DEBUG] STRING em escreva: {valor}\033[0m")
            self.add_instrucao(TAC_Instruction("print", TAC_Operand("const", valor)))

        elif ctx.expressao():
            resultado = self.visit(ctx.expressao())

            if resultado is not None:
                self.add_instrucao(TAC_Instruction("print", resultado))
                print(f"\033[92m[DEBUG] ESCREVA: escreva({resultado})\033[0m")
            else:
                print(f"\033[91m[ERRO SEMÂNTICO] Não foi possível avaliar a expressão de 'escreva'. Ignorada.\033[0m")


    def visitComando_ler(self, ctx):
        print(f"\033[94m[DEBUG] ENTRANDO EM visitComando_ler\033[0m")

        nome_var = ctx.ID().getText()
        temp = self.novo_temp()

        self.add_instrucao(TAC_Instruction("call", dest=temp, arg1=TAC_Operand("func", "leia")))
        self.add_instrucao(TAC_Instruction("=", dest=TAC_Operand("var", nome_var), arg1=temp))

        print(f"\033[94m[DEBUG] LEIA: {nome_var} = leia() → {temp}\033[0m")
        