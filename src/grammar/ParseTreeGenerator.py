##gera uma Árvore de Derivação (Parse Tree)

from antlr4 import *

class ParseTreeGenerator:
    def __init__(self):
        self.node_counter = 0
        self.output = []

    # def new_node(self, label):
    #     node_name = f"n{self.node_counter}"
    #     self.output.append(f'{node_name} [label="{label}"];')
    #     self.node_counter += 1
    #     return node_name

    def new_node(self, label):
        node_name = f"n{self.node_counter}"
        # Corrige problema de aspas internas no label
        label = label.replace('"', r'\"')
        self.output.append(f'{node_name} [label="{label}"];')
        self.node_counter += 1
        return node_name


    def add_edge(self, parent, child):
        self.output.append(f"{parent} -> {child};")

    def visit(self, ctx):
        if ctx is None:
            return self.new_node("null")

        if isinstance(ctx, TerminalNode):
            # Para tokens terminais (ex: palavras-chave, símbolos)
            return self.new_node(f"'{ctx.getText()}'")

        # Para regras da gramática
        rule_name = type(ctx).__name__.replace("Context", "")
        node = self.new_node(rule_name)

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            child_node = self.visit(child)
            self.add_edge(node, child_node)

        return node