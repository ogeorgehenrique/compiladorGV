class TAC_Instruction:
    def __init__(self, op, dest=None, arg1=None, arg2=None):
        self.op = op            # operador (ex: '+', '-', '=', 'if_goto')
        self.dest = dest        # destino (pode ser um temp, var ou label)
        self.arg1 = arg1        # primeiro argumento
        self.arg2 = arg2        # segundo argumento (pode ser None)

    # def __str__(self):
    #     if self.op == "label":
    #         return f"{self.dest}:"
    #     elif self.op == "goto":
    #         return f"goto {self.dest}"
    #     elif self.op == "if_goto":
    #         return f"if {self.arg1} goto {self.dest}"
    #     elif self.op == "return":
    #         return f"return {self.arg1}" if self.arg1 else "return"
    #     elif self.op == "=":
    #         return f"{self.dest} = {self.arg1}"
    #     elif self.arg1 and self.arg2:
    #         return f"{self.dest} = {self.arg1} {self.op} {self.arg2}"
    #     elif self.arg1 and self.dest:
    #         return f"{self.dest} = {self.op} {self.arg1}"
    #     elif self.dest and not self.arg1 and not self.arg2:
    #         return f"{self.op} {self.dest}"
    #     else:
    #         return f"{self.op}"
    
    def __str__(self):
        if self.op == "label":
            return f"{self.dest}:"
        elif self.op == "goto":
            return f"goto {self.dest}"
        elif self.op == "if_goto":
            return f"if {self.arg1} goto {self.dest}"
        elif self.op == "return":
            return f"return {self.arg1}" if self.arg1 else "return"
        elif self.op == "call":
            # Caso com retorno: _t0 = call func
            if self.dest:
                return f"{self.dest} = call {self.arg1}"
            # Caso sem retorno: call func
            else:
                return f"call {self.arg1}"
        elif self.op == "param":
            return f"param {self.arg1}"
        elif self.op == "=":
            return f"{self.dest} = {self.arg1}"
        elif self.arg1 and self.arg2:
            return f"{self.dest} = {self.arg1} {self.op} {self.arg2}"
        elif self.arg1 and self.dest:
            return f"{self.dest} = {self.op} {self.arg1}"
        elif self.dest and not self.arg1 and not self.arg2:
            return f"{self.op} {self.dest}"
        else:
            return f"{self.op}"

# class TAC_Instruction:
#     def __init__(self, opcode, dest=None, arg1=None, arg2=None):
#         self.opcode = opcode
#         self.dest = dest
#         self.arg1 = arg1
#         self.arg2 = arg2

#     def __str__(self):
#         if self.opcode == "label":
#             return f"{self.dest}:"
#         elif self.opcode == "goto":
#             return f"goto {self.dest}"
#         elif self.opcode == "if_goto":
#             return f"if {self.arg1} goto {self.dest}"
#         elif self.opcode == "param":
#             return f"param {self.arg1}"
#         elif self.opcode == "call":
#             return f"{self.dest} = call {self.arg1}"
#         elif self.opcode == "return":
#             return f"return {self.arg1}" if self.arg1 else "return"
#         elif self.arg2:
#             return f"{self.dest} = {self.arg1} {self.opcode} {self.arg2}"
#         elif self.arg1:
#             return f"{self.dest} = {self.opcode} {self.arg1}"
#         else:
#             return f"{self.dest} = {self.opcode}"