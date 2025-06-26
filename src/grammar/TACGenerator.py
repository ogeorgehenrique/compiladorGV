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
        



# essee funfa
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

    def visitExpressao(self, ctx):
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

        # # CHAMADA DE FUNÇÃO: ex: soma(i, 2)
        # elif filhos >= 4 and ctx.getChild(1).getText() == "(" and ctx.getChild(filhos - 1).getText() == ")":
        #     nome_funcao = ctx.getChild(0).getText()
        #     temp = self.novo_temp()
        #     self.add_instrucao(TAC_Instruction("call", temp, TAC_Operand("func", nome_funcao)))
        #     print(f"\033[94m[DEBUG] CHAMADA DE FUNÇÃO: {nome_funcao} → {temp}\033[0m")
        #     return temp

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


    def visitCondicao(self, ctx):
        arg1 = self.visit(ctx.expressao(0))
        op = ctx.operador().getText()
        arg2 = self.visit(ctx.expressao(1))

        temp = self.novo_temp()
        instrucao = TAC_Instruction(op, temp, arg1, arg2)
        self.add_instrucao(instrucao)

        print(f"\033[94m[DEBUG] CONDIÇÃO: {arg1} {op} {arg2} → {temp}\033[0m")
        return temp


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


    def visitComando_enquanto(self, ctx):
        print("\033[95m[DEBUG] INICIANDO 'enquanto'\033[0m")

        label_inicio = self.nova_label()
        label_fim = self.nova_label()

        print(f"\033[95m[DEBUG] Labels: INICIO={label_inicio}, FIM={label_fim}\033[0m")

        # Ponto de repetição
        self.add_instrucao(TAC_Instruction("label", dest=label_inicio))

        # Visita a condição
        cond_resultado = self.visit(ctx.condicao())  # _t0
        print(f"\033[95m[DEBUG] CONDICAO: {cond_resultado}\033[0m")

        # Se a condição for falsa, salta para o fim
        self.add_instrucao(TAC_Instruction("if_goto", dest=label_fim, arg1=TAC_Operand("cond_invert", cond_resultado.valor)))

        # Bloco do corpo
        print("\033[95m[DEBUG] Visitando bloco do 'enquanto'\033[0m")
        for comando in ctx.bloco().comandos():
            self.visit(comando)

        # Volta para o início
        self.add_instrucao(TAC_Instruction("goto", dest=label_inicio))

        # Marca o fim do laço
        self.add_instrucao(TAC_Instruction("label", dest=label_fim))
        print("\033[95m[DEBUG] Finalizando 'enquanto'\033[0m")


    

    def visitComando_para(self, ctx):
        self.visit(ctx.atribuicao())  # int i = 0

        label_cond = self.nova_label()
        label_fim = self.nova_label()

        self.add_instrucao(TAC_Instruction("label", dest=label_cond))
        cond = self.visit(ctx.condicao())
        self.add_instrucao(TAC_Instruction("if_goto", dest=label_fim, arg1=TAC_Operand("cond_invert", cond.valor)))

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

    def visitComando_escrever(self, ctx):
        print(f"\033[94m[DEBUG] ENTRANDO EM visitComando_escrever\033[0m")

        filho = ctx.getChild(2)  # filho pode ser uma expressão ou um STRING

        if filho.getSymbol().type == ctx.parser.STRING:
            valor = TAC_Operand("const", filho.getText())
            print(f"\033[94m[DEBUG] STRING em escreva: {valor}\033[0m")
        else:
            valor = self.visit(filho)
            print(f"\033[94m[DEBUG] EXPRESSAO em escreva: {valor}\033[0m")

        self.add_instrucao(TAC_Instruction("param", arg1=valor))
        self.add_instrucao(TAC_Instruction("call", dest=None, arg1=TAC_Operand("func", "escreva")))

        print(f"\033[94m[DEBUG] ESCREVA: escreva({valor})\033[0m")


    def visitComando_ler(self, ctx):
        print(f"\033[94m[DEBUG] ENTRANDO EM visitComando_ler\033[0m")

        nome_var = ctx.ID().getText()
        temp = self.novo_temp()

        self.add_instrucao(TAC_Instruction("call", dest=temp, arg1=TAC_Operand("func", "leia")))
        self.add_instrucao(TAC_Instruction("=", dest=TAC_Operand("var", nome_var), arg1=temp))

        print(f"\033[94m[DEBUG] LEIA: {nome_var} = leia() → {temp}\033[0m")
        