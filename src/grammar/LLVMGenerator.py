from llvmlite import ir
from TAC_Instruction import TAC_Instruction
from TAC_Operand import TAC_Operand

class LLVMGenerator:
    def __init__(self, tac_instrucoes):
        self.tac = tac_instrucoes
        self.module = ir.Module(name="meu_modulo")
        self.func_type = ir.FunctionType(ir.IntType(32), [])
        self.main_func = ir.Function(self.module, self.func_type, name="main")
        self.entry_block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(self.entry_block)
        self.vars = {}
        self.labels = {}
        self.string_counter = 0
    
    def obter_valor(self, op):
        if op is None:
            raise ValueError("[ERRO] Operando é None - possivelmente uma instrução malformada no TAC.")

        if op.tipo == "const":
            return ir.Constant(ir.IntType(32), int(op.valor))
        elif op.tipo == "var":
            return self.builder.load(self.vars[op.valor])
        elif op.tipo == "temp":
            return self.builder.load(self.vars[op.valor])


    def gerar(self):
        for instr in self.tac:
            op = instr.op

            if op == "label":
                nome = instr.dest.valor
                block = self.labels.get(nome)
                if not block:
                    block = self.main_func.append_basic_block(name=nome)
                    self.labels[nome] = block

                if not self.builder.block.is_terminated:
                    self.builder.branch(block)

                self.builder.position_at_start(block)

            elif op == "goto":
                nome = instr.dest.valor
                block = self.labels.get(nome)
                if not block:
                    block = self.main_func.append_basic_block(name=nome)
                    self.labels[nome] = block

                self.builder.branch(block)

            elif op == "if_goto":
                cond_val = self.obter_valor(instr.arg1)
                cond_bool = self.builder.icmp_signed("!=", cond_val, ir.Constant(ir.IntType(32), 0), "ifcond")

                then_block = self.labels.get(instr.dest.valor)
                if not then_block:
                    then_block = self.main_func.append_basic_block(name=instr.dest.valor)
                    self.labels[instr.dest.valor] = then_block

                else_block = self.main_func.append_basic_block(name=f"cont_{len(self.labels)}")
                self.builder.cbranch(cond_bool, then_block, else_block)
                self.builder.position_at_start(else_block)

            elif op == "if_false":
                cond_val = self.obter_valor(instr.arg1)
                cond_bool = self.builder.icmp_signed("==", cond_val, ir.Constant(ir.IntType(32), 0), "iffalse")

                then_block = self.labels.get(instr.dest.valor)
                if not then_block:
                    then_block = self.main_func.append_basic_block(name=instr.dest.valor)
                    self.labels[instr.dest.valor] = then_block

                else_block = self.main_func.append_basic_block(name=f"cont_{len(self.labels)}")
                self.builder.cbranch(cond_bool, then_block, else_block)
                self.builder.position_at_start(else_block)

            elif op == "=":
                valor = self.obter_valor(instr.arg1)
                aloc = self._obter_ou_criar_var(instr.dest.valor)
                self.builder.store(valor, aloc)

            elif op in ["+", "-", "*", "/"]:
                lhs = self.obter_valor(instr.arg1)
                rhs = self.obter_valor(instr.arg2)

                if op == "+":
                    result = self.builder.add(lhs, rhs, name=instr.dest.valor)
                elif op == "-":
                    result = self.builder.sub(lhs, rhs, name=instr.dest.valor)
                elif op == "*":
                    result = self.builder.mul(lhs, rhs, name=instr.dest.valor)
                elif op == "/":
                    result = self.builder.sdiv(lhs, rhs, name=instr.dest.valor)

                aloc = self._obter_ou_criar_var(instr.dest.valor)
                self.builder.store(result, aloc)

            elif op in [">", "<", ">=", "<=", "==", "!="]:
                lhs = self.obter_valor(instr.arg1)
                rhs = self.obter_valor(instr.arg2)

                result_i1 = self.builder.icmp_signed(op, lhs, rhs, name="cmptmp")
                result_i32 = self.builder.zext(result_i1, ir.IntType(32), name="bool_to_int")

                ponteiro_dest = self._obter_ou_criar_var(instr.dest.valor)
                self.builder.store(result_i32, ponteiro_dest)

            elif op in ["&&", "||"]:
                lhs = self.obter_valor(instr.arg1)
                rhs = self.obter_valor(instr.arg2)

                if op == "&&":
                    result = self.builder.and_(lhs, rhs, name="andtmp")
                elif op == "||":
                    result = self.builder.or_(lhs, rhs, name="ortmp")

                ponteiro_dest = self._obter_ou_criar_var(instr.dest.valor)
                self.builder.store(result, ponteiro_dest)

            elif op == "return":
                val = self.obter_valor(instr.arg1)
                self.builder.ret(val)

            elif op == "print":
                self.gerar_printf(instr.arg1)

            elif op == "call":
                func = self.module.globals.get(instr.arg1.valor)
                if not func:
                    func_type = ir.FunctionType(ir.IntType(32), [])
                    func = ir.Function(self.module, func_type, name=instr.arg1.valor)

                call = self.builder.call(func, [], name=instr.dest.valor if instr.dest else "")
                if instr.dest:
                    aloc = self._obter_ou_criar_var(instr.dest.valor)
                    self.builder.store(call, aloc)

        return str(self.module)

    def obter_valor(self, op: TAC_Operand):
        if op.tipo == "const":
            return ir.Constant(ir.IntType(32), int(op.valor))
        elif op.tipo in ["var", "temp"]:
            return self.builder.load(self.vars[op.valor])
        else:
            raise Exception(f"Operando não suportado: {op.tipo}")

    def _obter_ou_criar_var(self, nome: str):
        if nome not in self.vars:
            self.vars[nome] = self.builder.alloca(ir.IntType(32), name=nome)
        return self.vars[nome]

    def gerar_printf(self, arg: TAC_Operand):
        printf_ty = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()], var_arg=True)
        printf = self.module.globals.get("printf")
        if printf is None:
            printf = ir.Function(self.module, printf_ty, name="printf")

        if arg.tipo == "const" and arg.valor.startswith('"'):
            texto = arg.valor.strip('"') + "\n"
            texto_bytes = bytearray(texto.encode("utf8")) + b"\00"
            texto_len = len(texto_bytes)

            str_name = f"str{self.string_counter}"
            self.string_counter += 1

            str_type = ir.ArrayType(ir.IntType(8), texto_len)
            global_str = ir.GlobalVariable(self.module, str_type, name=str_name)
            global_str.linkage = 'internal'
            global_str.global_constant = True
            global_str.initializer = ir.Constant(str_type, texto_bytes)

            str_ptr = self.builder.bitcast(global_str, ir.IntType(8).as_pointer())
            self.builder.call(printf, [str_ptr])

        elif arg.tipo in ["var", "temp"]:
            valor = self.builder.load(self.vars[arg.valor], name=f"tmp_{arg.valor}")

            if not hasattr(self, "fmt_int"):
                fmt_str = "%d\n\00"
                fmt_bytes = bytearray(fmt_str.encode("utf8"))
                fmt_type = ir.ArrayType(ir.IntType(8), len(fmt_bytes))
                self.fmt_int = ir.GlobalVariable(self.module, fmt_type, name="fmt_int")
                self.fmt_int.linkage = 'internal'
                self.fmt_int.global_constant = True
                self.fmt_int.initializer = ir.Constant(fmt_type, fmt_bytes)

            fmt_ptr = self.builder.bitcast(self.fmt_int, ir.IntType(8).as_pointer())
            self.builder.call(printf, [fmt_ptr, valor])

        else:
            raise Exception(f"Tipo de argumento não suportado em print: {arg.tipo}")
