# Generated from CompiladorGV.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CompiladorGVParser import CompiladorGVParser
else:
    from CompiladorGVParser import CompiladorGVParser

# This class defines a complete generic visitor for a parse tree produced by CompiladorGVParser.

class CompiladorGVVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CompiladorGVParser#inicio.
    def visitInicio(self, ctx:CompiladorGVParser.InicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comandos.
    def visitComandos(self, ctx:CompiladorGVParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_declaracao_funcao.
    def visitComando_declaracao_funcao(self, ctx:CompiladorGVParser.Comando_declaracao_funcaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_chamada_funcao.
    def visitComando_chamada_funcao(self, ctx:CompiladorGVParser.Comando_chamada_funcaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#parametros.
    def visitParametros(self, ctx:CompiladorGVParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#parametro.
    def visitParametro(self, ctx:CompiladorGVParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#argumentos.
    def visitArgumentos(self, ctx:CompiladorGVParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_retorno.
    def visitComando_retorno(self, ctx:CompiladorGVParser.Comando_retornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_ler.
    def visitComando_ler(self, ctx:CompiladorGVParser.Comando_lerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_escrever.
    def visitComando_escrever(self, ctx:CompiladorGVParser.Comando_escreverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_se.
    def visitComando_se(self, ctx:CompiladorGVParser.Comando_seContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_para.
    def visitComando_para(self, ctx:CompiladorGVParser.Comando_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_enquanto.
    def visitComando_enquanto(self, ctx:CompiladorGVParser.Comando_enquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_atribuicao.
    def visitComando_atribuicao(self, ctx:CompiladorGVParser.Comando_atribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#comando_declaracao.
    def visitComando_declaracao(self, ctx:CompiladorGVParser.Comando_declaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#atribuicao.
    def visitAtribuicao(self, ctx:CompiladorGVParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#incremento.
    def visitIncremento(self, ctx:CompiladorGVParser.IncrementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#condicao.
    def visitCondicao(self, ctx:CompiladorGVParser.CondicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#operador.
    def visitOperador(self, ctx:CompiladorGVParser.OperadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#lista_argumentos.
    def visitLista_argumentos(self, ctx:CompiladorGVParser.Lista_argumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#expressao.
    def visitExpressao(self, ctx:CompiladorGVParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#bloco.
    def visitBloco(self, ctx:CompiladorGVParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorGVParser#bloco_funcao.
    def visitBloco_funcao(self, ctx:CompiladorGVParser.Bloco_funcaoContext):
        return self.visitChildren(ctx)



del CompiladorGVParser