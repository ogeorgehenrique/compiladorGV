from TAC_Instruction import TAC_Instruction
from TAC_Operand import TAC_Operand
import re

def parse_operand(texto: str) -> TAC_Operand:
    texto = texto.strip()

    if texto.startswith("_t"):
        return TAC_Operand("temp", texto)
    if texto.startswith("L") and texto[1:].isdigit():
        return TAC_Operand("label", texto)
    if texto.startswith('"') and texto.endswith('"'):
        return TAC_Operand("const", texto)

    try:
        int(texto)
        return TAC_Operand("const", texto)
    except ValueError:
        pass

    if texto.isidentifier():
        return TAC_Operand("var", texto)

    raise ValueError(f"Formato de operando não reconhecido: '{texto}'")


def carregar_tac_de_arquivo(conteudo: str) -> list:
    instrucoes = []
    linhas = conteudo.strip().splitlines()

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue

        partes = linha.split()

        if partes[0] == "if_false" and partes[2] == "goto":
            cond = parse_operand(partes[1])
            dest = parse_operand(partes[3])
            instrucoes.append(TAC_Instruction("if_false", dest=dest, arg1=cond))

        elif partes[0] == "if" and partes[2] == "goto":
            cond = parse_operand(partes[1])
            dest = parse_operand(partes[3])
            instrucoes.append(TAC_Instruction("if_goto", dest=dest, arg1=cond))

        elif partes[0] == "goto":
            dest = parse_operand(partes[1])
            instrucoes.append(TAC_Instruction("goto", dest=dest))

        elif len(partes) == 1 and linha.endswith(":"):
            label = linha[:-1]
            instrucoes.append(TAC_Instruction("label", dest=TAC_Operand("label", label)))

        elif partes[0] == "print":
            operando_str = " ".join(partes[1:])
            arg1 = parse_operand(operando_str)
            instrucoes.append(TAC_Instruction("print", arg1=arg1))

        elif partes[0] == "return":
            arg1 = parse_operand(partes[1]) if len(partes) > 1 else None
            instrucoes.append(TAC_Instruction("return", arg1=arg1))

        elif partes[0] == "func":
            dest = TAC_Operand("label", partes[1])
            instrucoes.append(TAC_Instruction("func", dest=dest))

        elif partes[0] == "endfunc":
            instrucoes.append(TAC_Instruction("endfunc"))

        elif "=" in linha:
            try:
                dest_str, expr_str = linha.split("=", 1)
                dest = parse_operand(dest_str)
                expr_str = expr_str.strip()

                # Expressões como: a + b > c (com dois operadores)
                m = re.match(r"(\w+)\s*([\+\-\*/])\s*(\w+)\s*([<>=!]=?|&&|\|\|)\s*(\w+)", expr_str)
                if m:
                    # Ex: a + b > c  → arg1 = a + b, depois op relacional com c
                    tmp1 = TAC_Operand("temp", "_tmp1")
                    instr1 = TAC_Instruction(m.group(2), dest=tmp1,
                                             arg1=parse_operand(m.group(1)),
                                             arg2=parse_operand(m.group(3)))
                    instr2 = TAC_Instruction(m.group(4), dest=dest,
                                             arg1=tmp1,
                                             arg2=parse_operand(m.group(5)))
                    instrucoes.append(instr1)
                    instrucoes.append(instr2)
                    continue

                # Expressões como: a > b
                m = re.match(r"(\w+)\s*([<>=!]=?|&&|\|\|)\s*(\w+)", expr_str)
                if m:
                    arg1 = parse_operand(m.group(1))
                    op = m.group(2)
                    arg2 = parse_operand(m.group(3))
                    instrucoes.append(TAC_Instruction(op, dest=dest, arg1=arg1, arg2=arg2))
                    continue

                # Expressões simples: a + b
                partes_expr = expr_str.split()
                if len(partes_expr) == 1:
                    arg1 = parse_operand(partes_expr[0])
                    instrucoes.append(TAC_Instruction("=", dest=dest, arg1=arg1))
                elif len(partes_expr) == 3:
                    arg1 = parse_operand(partes_expr[0])
                    op = partes_expr[1]
                    arg2 = parse_operand(partes_expr[2])
                    instrucoes.append(TAC_Instruction(op, dest=dest, arg1=arg1, arg2=arg2))
                else:
                    print(f"[AVISO] Parser encontrou uma expressão de atribuição mal formada: {linha}")
            except Exception as e:
                print(f"[ERRO] Erro ao analisar linha: {linha}")
                print("       →", e)

        else:
            print(f"[AVISO] Parser não reconheceu a linha TAC: {linha}")

    return instrucoes
