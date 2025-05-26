class SemanticAnalyzerVisitor:
    def __init__(self):
        self.symbol_table = {}  # Armazena variáveis e seus tipos

    def visit(self, node):
        method_name = f'visit_{node["type"]}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        for child in node.get("children", []):
            self.visit(child)

    def visit_VarDecl(self, node):
        var_name = node["value"]
        var_type = node["var_type"]
        if var_name in self.symbol_table:
            print(f"Erro: Variável '{var_name}' já declarada.")
        else:
            self.symbol_table[var_name] = var_type

    def visit_Assign(self, node):
        var_name = node["left"]["value"]
        expr_type = self.visit(node["right"])
        if var_name not in self.symbol_table:
            print(f"Erro: Variável '{var_name}' não foi declarada.")
        elif self.symbol_table[var_name] != expr_type:
            print(f"Erro: Tipo incompatível em '{var_name}': esperado {self.symbol_table[var_name]}, obtido {expr_type}")

    def visit_IntLiteral(self, node):
        return "int"

    def visit_BoolLiteral(self, node):
        return "bool"

    def visit_BinaryOp(self, node):
        left_type = self.visit(node["left"])
        right_type = self.visit(node["right"])
        if left_type != right_type:
            print(f"Erro: Tipos incompatíveis na operação binária: {left_type} e {right_type}")
        return left_type
