#classe querepresenta qualquer operando de uma instrução TAC:
# var: nome de variável (ex: x)
# temp: temporário gerado automaticamente (_t0, _t1, …)
# const: constantes literais (5, "texto")
# label: etiquetas de desvio (L0, L1, …)

class TAC_Operand:
    def __init__(self, tipo, valor):
        self.tipo = tipo  # 'var', 'temp', 'const', 'label'
        self.valor = valor

    def __str__(self):
        return str(self.valor)