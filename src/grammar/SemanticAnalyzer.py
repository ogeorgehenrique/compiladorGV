class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def analyze(self, ast):
        if ast["type"] != "Program":
            raise Exception("AST root must be Program")
        for stmt in ast["body"]:
            self.visit(stmt)

    def visit(self, node):
        if node is None:
            print("[Erro Semântico] Nó da AST é None. Verifique o ASTBuilder.")
            return
        method_name = f'visit_{node["type"]}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def visit_FunctionDeclaration(self, node):
        if node["name"] in self.symbol_table:
            print(f"[Erro Semântico] Função '{node['name']}' já declarada.")
        else:
            self.symbol_table[node["name"]] = node
        self.visit(node["body"])  # node["body"] é um bloco

    def visit_Block(self, node):
        for stmt in node["statements"]:
            self.visit(stmt)

    def visit_VariableDeclaration(self, node):
        if "value" in node and node["value"] is not None:
            self.visit(node["value"])

    def visit_Return(self, node):
        if "value" in node and node["value"] is not None:
            self.visit(node["value"])

    def visit_BinaryExpression(self, node):
        self.visit(node["left"])
        self.visit(node["right"])

    def visit_Identifier(self, node):
        pass  # Poderia verificar se variável está declarada

    def visit_IntLiteral(self, node):
        pass  # Literal, nada a fazer

    def visit_WhileStatement(self, node):
        self.visit(node["condition"])
        self.visit(node["body"])

    def visit_IfStatement(self, node):
        self.visit(node["condition"])
        self.visit(node["then"])
        if "else" in node and node["else"] is not None:
            self.visit(node["else"])

    def visit_FunctionCall(self, node):
        # Verifica se função existe
        if node["name"] not in self.symbol_table:
            print(f"[Erro Semântico] Função '{node['name']}' não declarada.")
        for arg in node.get("arguments", []):
            self.visit(arg)

    def visit_Write(self, node):
        # Apenas para demonstração, você pode validar se a string está correta
        if not isinstance(node["value"], str):
            print(f"[Erro Semântico] Valor de escrita inválido: {node['value']}")

    def generic_visit(self, node):
        print(f"[Aviso] Visitador genérico para tipo desconhecido: {node}")

    def visit_condicao_binaria(self, node):
        self.visit(node['left'])
        self.visit(node['right'])

    def visit_Assignment(self, node):
        self.visit(node['value'])
