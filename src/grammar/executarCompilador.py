# main.py (ou onde você processa a entrada do compilador)

from antlr4 import *
from CompiladorGVLexer import CompiladorGVLexer
from CompiladorGVParser import CompiladorGVParser

from ASTBuilderVisitor import ASTBuilderVisitor
from SemanticAnalyzer import SemanticAnalyzer

input_stream = FileStream("exemplo.gv", encoding="utf-8")  # entrada do código fonte
lexer = CompiladorGVLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = CompiladorGVParser(token_stream)
tree = parser.inicio()

# Gera AST como estrutura Python
builder = ASTBuilderVisitor()
ast = builder.visit(tree)

# Mostra AST (opcional)
import pprint
pprint.pprint(ast)

# Faz análise semântica
analyzer = SemanticAnalyzer()
analyzer.analyze(ast)
