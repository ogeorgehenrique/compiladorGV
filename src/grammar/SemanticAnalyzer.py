from symbol_table import SymbolTable

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.current_function_return_type = None  # novo atributo

    def error(self, message):
        self.errors.append(message)

    def visit(self, node):
        if not node:
            return None
        method_name = f"visit_{node['type']}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        print(f"[Aviso] Visitador genérico para tipo desconhecido: {node}")

    def visit_Program(self, node):
        for stmt in node["body"]:
            self.visit(stmt)

    def visit_FunctionDeclaration(self, node):
        if self.symbol_table.lookup(node["name"]):
            self.error(f"Função '{node['name']}' já declarada.")
        else:
            self.symbol_table.define(node["name"], {
                "type": "function",
                "returnType": node["returnType"],
                "params": node["params"]
            })

        self.symbol_table.push_scope()
        for param in node["params"]:
            if self.symbol_table.lookup(param["name"]):
                self.error(f"Parâmetro '{param['name']}' já declarado na função '{node['name']}'.")
            self.symbol_table.define(param["name"], {"type": param["paramType"]})

        self.current_function_return_type = node["returnType"]
        self.visit(node["body"])
        self.symbol_table.pop_scope()

    def visit_Block(self, node):
        self.symbol_table.push_scope()
        for stmt in node["statements"]:
            self.visit(stmt)
        self.symbol_table.pop_scope()

    def visit_VariableDeclaration(self, node):
        if self.symbol_table.lookup(node["name"]):
            self.error(f"Variável '{node['name']}' já declarada.")
        else:
            self.symbol_table.define(node["name"], {
                "type": "variable",
                "varType": node["varType"]
            })
        if node["value"]:
            value_type = self.visit(node["value"])
            if value_type and value_type != node["varType"]:
                self.error(f"Tipo incompatível em atribuição à variável '{node['name']}': esperado {node['varType']}, encontrado {value_type}")

    def visit_Assignment(self, node):
        var_info = self.symbol_table.lookup(node["target"])
        if not var_info:
            self.error(f"Variável '{node['target']}' não declarada.")
        else:
            if var_info["type"] != "variable":
                self.error(f"'{node['target']}' não é uma variável.")
            value_type = self.visit(node["value"])
            if value_type and value_type != var_info["varType"]:
                self.error(f"Tipo incompatível em atribuição a '{node['target']}': esperado {var_info['varType']}, encontrado {value_type}")

    def visit_Return(self, node):
        value_type = self.visit(node["value"])
        if value_type is None:
            self.error(f"Tipo de retorno inválido: expressão não reconhecida.")
        elif self.current_function_return_type != value_type:
            self.error(f"Tipo de retorno incompatível: esperado {self.current_function_return_type}, encontrado {value_type}")
            
    def visit_IfStatement(self, node):
        self.visit(node["condition"])
        self.visit(node["then"])
        if node["else"]:
            self.visit(node["else"])

    def visit_ForStatement(self, node):
        self.symbol_table.push_scope()
        self.visit(node["init"])
        self.visit(node["condition"])
        self.visit(node["increment"])
        self.visit(node["body"])
        self.symbol_table.pop_scope()

    def visit_WhileStatement(self, node):
        self.visit(node["condition"])
        self.visit(node["body"])

    def visit_Read(self, node):
        var_info = self.symbol_table.lookup(node["identifier"])
        if not var_info:
            self.error(f"Variável '{node['identifier']}' não declarada para leitura.")

    def visit_Write(self, node):
        if isinstance(node["value"], dict):
            self.visit(node["value"])

    def visit_Increment(self, node):
        var_info = self.symbol_table.lookup(node["target"])
        if not var_info:
            self.error(f"Variável '{node['target']}' não declarada para incremento.")

    def visit_Decrement(self, node):
        var_info = self.symbol_table.lookup(node["target"])
        if not var_info:
            self.error(f"Variável '{node['target']}' não declarada para decremento.")

    def visit_condicao_binaria(self, node):
        self.visit(node["left"])
        self.visit(node["right"])

    def visit_condicao_logica(self, node):
        self.visit(node["left"])
        self.visit(node["right"])

    def visit_BinaryExpression(self, node):
        left_type = self.visit(node["left"])
        right_type = self.visit(node["right"])
        if left_type != right_type:
            self.error(f"Expressão binária com tipos incompatíveis: {left_type} e {right_type}")
            return None
        return left_type  # tipo do resultado da expressão binária

    def visit_FunctionCall(self, node):
        func_info = self.symbol_table.lookup(node["name"])
        if not func_info:
            self.error(f"Função '{node['name']}' não declarada.")
        else:
            if func_info["type"] != "function":
                self.error(f"'{node['name']}' não é uma função.")
            else:
                expected = len(func_info["params"])
                given = len(node["arguments"])
                if expected != given:
                    self.error(f"Função '{node['name']}' chamada com {given} argumentos, mas espera {expected}.")
        for arg in node["arguments"]:
            self.visit(arg)

    def visit_Identifier(self, node):
        var_info = self.symbol_table.lookup(node["name"])
        if not var_info:
            self.error(f"Identificador '{node['name']}' não declarado.")
            return None
        return var_info.get("varType") or var_info.get("type")

    def visit_IntLiteral(self, node):
        return "int"

    def visit_FloatLiteral(self, node):
        return "float"

    def visit_StringLiteral(self, node):
        return "string"

    def visit_Parameter(self, node):
        pass

    def analyze(self, ast):
        self.visit(ast)
