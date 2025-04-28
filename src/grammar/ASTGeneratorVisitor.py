# # ✅ Esse Visitor visita cada parte do seu programa e gera as linhas de um arquivo .dot.


# from CompiladorGVVisitor import CompiladorGVVisitor
# from CompiladorGVParser import *

# class ASTGeneratorVisitor(CompiladorGVVisitor):
#     def __init__(self):
#         self.node_counter = 0
#         self.output = []

#     def new_node(self, label):
#         node_name = f"n{self.node_counter}"
#         self.output.append(f'{node_name} [label="{label}"];')
#         self.node_counter += 1
#         return node_name

#     def add_edge(self, parent, child):
#         self.output.append(f"{parent} -> {child};")

#     def visitInicio(self, ctx:CompiladorGVParser.InicioContext):
#         root = self.new_node("inicio")
#         for comando in ctx.comandos():
#             child = self.visit(comando)
#             self.add_edge(root, child)
#         return root

#     def visitComando_declaracao_funcao(self, ctx:CompiladorGVParser.Comando_declaracao_funcaoContext):
#         node = self.new_node("funcao")
#         tipo = self.new_node(ctx.children[0].getText())
#         id_funcao = self.new_node(ctx.children[1].getText())
#         self.add_edge(node, tipo)
#         self.add_edge(node, id_funcao)
#         bloco = self.visit(ctx.bloco_funcao())
#         self.add_edge(node, bloco)
#         return node

#     def visitComando_escrever(self, ctx:CompiladorGVParser.Comando_escreverContext):
#         node = self.new_node("escreva")
#         return node

#     def visitComando_retorno(self, ctx:CompiladorGVParser.Comando_retornoContext):
#         node = self.new_node("retorna")
#         return node

#     def genericVisit(self, ctx):
#         if ctx.getChildCount() == 0:
#             return self.new_node(ctx.getText())
#         else:
#             node = self.new_node(type(ctx).__name__)
#             for child in ctx.getChildren():
#                 child_node = self.visit(child)
#                 self.add_edge(node, child_node)
#             return node

# from CompiladorGVVisitor import CompiladorGVVisitor
# from CompiladorGVParser import *

# class ASTGeneratorVisitor(CompiladorGVVisitor):
#     def __init__(self):
#         self.node_counter = 0
#         self.output = []

#     def new_node(self, label):
#         node_name = f"n{self.node_counter}"
#         self.output.append(f'{node_name} [label="{label}"];')
#         self.node_counter += 1
#         return node_name

#     def add_edge(self, parent, child):
#         self.output.append(f"{parent} -> {child};")

#     def visitInicio(self, ctx:CompiladorGVParser.InicioContext):
#         root = self.new_node("inicio")
#         for comando in ctx.comandos():
#             child = self.visit(comando)
#             self.add_edge(root, child)
#         return root

#     def visitComando_declaracao_funcao(self, ctx:CompiladorGVParser.Comando_declaracao_funcaoContext):
#         node = self.new_node("funcao")
        
#         tipo = self.new_node(ctx.getChild(0).getText())
#         nome = self.new_node(ctx.getChild(1).getText())
        
#         self.add_edge(node, tipo)
#         self.add_edge(node, nome)

#         # Visitar o bloco da função
#         bloco = self.visit(ctx.bloco_funcao())
#         self.add_edge(node, bloco)
        
#         return node

#     def visitComando_escrever(self, ctx:CompiladorGVParser.Comando_escreverContext):
#         node = self.new_node("escreva")
#         return node

#     def visitComando_retorno(self, ctx:CompiladorGVParser.Comando_retornoContext):
#         node = self.new_node("retorna")
#         return node

#     def genericVisit(self, ctx):
#         if ctx.getChildCount() == 0:
#             return self.new_node(ctx.getText())
#         else:
#             node = self.new_node(type(ctx).__name__)
#             for child in ctx.getChildren():
#                 child_node = self.visit(child)
#                 self.add_edge(node, child_node)
#             return node
        

# from CompiladorGVVisitor import CompiladorGVVisitor
# from CompiladorGVParser import *

# class ASTGeneratorVisitor(CompiladorGVVisitor):
#     def __init__(self):
#         self.node_counter = 0
#         self.output = []

#     def new_node(self, label):
#         node_name = f"n{self.node_counter}"
#         self.output.append(f'{node_name} [label="{label}"];')
#         self.node_counter += 1
#         return node_name

#     def add_edge(self, parent, child):
#         self.output.append(f"{parent} -> {child};")

#     def visitInicio(self, ctx:CompiladorGVParser.InicioContext):
#         root = self.new_node("inicio")
#         for comando in ctx.comandos():
#             child = self.visit(comando)
#             self.add_edge(root, child)
#         return root

#     def visitComando_declaracao_funcao(self, ctx:CompiladorGVParser.Comando_declaracao_funcaoContext):
#         node = self.new_node("funcao")
        
#         tipo = self.new_node(ctx.TIPO_INT().getText() if ctx.TIPO_INT() else ctx.TIPO_STRING().getText())
#         nome = self.new_node(ctx.ID().getText())

#         self.add_edge(node, tipo)
#         self.add_edge(node, nome)

#         bloco = self.visit(ctx.bloco_funcao())
#         self.add_edge(node, bloco)

#         return node

#     def visitComando_escrever(self, ctx:CompiladorGVParser.Comando_escreverContext):
#         node = self.new_node("escreva")
#         return node

#     def visitComando_retorno(self, ctx:CompiladorGVParser.Comando_retornoContext):
#         node = self.new_node("retorna")
#         return node

#     def genericVisit(self, ctx):
#         if ctx is None:
#             return self.new_node("null")

#         # Trata se for terminal node (Token)
#         if hasattr(ctx, 'getText'):
#             return self.new_node(ctx.getText())

#         node = self.new_node(type(ctx).__name__)

#         for child in ctx.getChildren():
#             child_node = self.visit(child)
#             self.add_edge(node, child_node)

#         return node

from CompiladorGVVisitor import CompiladorGVVisitor
from CompiladorGVParser import *

class ASTGeneratorVisitor(CompiladorGVVisitor):
    def __init__(self):
        self.node_counter = 0
        self.output = []

    def new_node(self, label):
        node_name = f"n{self.node_counter}"
        self.output.append(f'{node_name} [label="{label}"];')
        self.node_counter += 1
        return node_name

    def add_edge(self, parent, child):
        self.output.append(f"{parent} -> {child};")

    def visitInicio(self, ctx: CompiladorGVParser.InicioContext):
        root = self.new_node("inicio")
        for comando in ctx.comandos():
            child = self.visit(comando)
            self.add_edge(root, child)
        return root

    def visitComando_declaracao_funcao(self, ctx: CompiladorGVParser.Comando_declaracao_funcaoContext):
        node = self.new_node("funcao")

        tipo_node = self.new_node(ctx.getChild(0).getText())  # TIPO_INT ou TIPO_STRING
        id_node = self.new_node(ctx.getChild(1).getText())    # Nome da função
        params_node = self.new_node("parametros")
        bloco_node = self.visit(ctx.bloco_funcao())

        self.add_edge(node, tipo_node)
        self.add_edge(node, id_node)
        self.add_edge(node, params_node)
        self.add_edge(node, bloco_node)

        return node

    def visitBloco_funcao(self, ctx:CompiladorGVParser.Bloco_funcaoContext):
        node = self.new_node("bloco")
        for comando in ctx.comandos():
            child = self.visit(comando)
            self.add_edge(node, child)
        return node

    def visitComando_escrever(self, ctx:CompiladorGVParser.Comando_escreverContext):
        node = self.new_node("escreva")
        return node

    def visitComando_retorno(self, ctx:CompiladorGVParser.Comando_retornoContext):
        node = self.new_node("retorna")
        return node

    def genericVisit(self, ctx):
        # Para qualquer coisa que não tenha visit específico
        if ctx is None:
            return self.new_node("null")

        if hasattr(ctx, 'getText'):
            return self.new_node(ctx.getText())

        node = self.new_node(type(ctx).__name__)
        for child in ctx.getChildren():
            child_node = self.visit(child)
            self.add_edge(node, child_node)

        return node