# Generated from grammar/CompiladorGV.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CompiladorGVParser import CompiladorGVParser
else:
    from CompiladorGVParser import CompiladorGVParser

# This class defines a complete listener for a parse tree produced by CompiladorGVParser.
class CompiladorGVListener(ParseTreeListener):

    # Enter a parse tree produced by CompiladorGVParser#inicio.
    def enterInicio(self, ctx:CompiladorGVParser.InicioContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#inicio.
    def exitInicio(self, ctx:CompiladorGVParser.InicioContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comandos.
    def enterComandos(self, ctx:CompiladorGVParser.ComandosContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comandos.
    def exitComandos(self, ctx:CompiladorGVParser.ComandosContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_declaracao_funcao.
    def enterComando_declaracao_funcao(self, ctx:CompiladorGVParser.Comando_declaracao_funcaoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_declaracao_funcao.
    def exitComando_declaracao_funcao(self, ctx:CompiladorGVParser.Comando_declaracao_funcaoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_chamada_funcao.
    def enterComando_chamada_funcao(self, ctx:CompiladorGVParser.Comando_chamada_funcaoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_chamada_funcao.
    def exitComando_chamada_funcao(self, ctx:CompiladorGVParser.Comando_chamada_funcaoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#parametros.
    def enterParametros(self, ctx:CompiladorGVParser.ParametrosContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#parametros.
    def exitParametros(self, ctx:CompiladorGVParser.ParametrosContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#parametro.
    def enterParametro(self, ctx:CompiladorGVParser.ParametroContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#parametro.
    def exitParametro(self, ctx:CompiladorGVParser.ParametroContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#argumentos.
    def enterArgumentos(self, ctx:CompiladorGVParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#argumentos.
    def exitArgumentos(self, ctx:CompiladorGVParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_retorno.
    def enterComando_retorno(self, ctx:CompiladorGVParser.Comando_retornoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_retorno.
    def exitComando_retorno(self, ctx:CompiladorGVParser.Comando_retornoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_ler.
    def enterComando_ler(self, ctx:CompiladorGVParser.Comando_lerContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_ler.
    def exitComando_ler(self, ctx:CompiladorGVParser.Comando_lerContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_escrever.
    def enterComando_escrever(self, ctx:CompiladorGVParser.Comando_escreverContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_escrever.
    def exitComando_escrever(self, ctx:CompiladorGVParser.Comando_escreverContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_se.
    def enterComando_se(self, ctx:CompiladorGVParser.Comando_seContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_se.
    def exitComando_se(self, ctx:CompiladorGVParser.Comando_seContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_para.
    def enterComando_para(self, ctx:CompiladorGVParser.Comando_paraContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_para.
    def exitComando_para(self, ctx:CompiladorGVParser.Comando_paraContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_enquanto.
    def enterComando_enquanto(self, ctx:CompiladorGVParser.Comando_enquantoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_enquanto.
    def exitComando_enquanto(self, ctx:CompiladorGVParser.Comando_enquantoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_atribuicao.
    def enterComando_atribuicao(self, ctx:CompiladorGVParser.Comando_atribuicaoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_atribuicao.
    def exitComando_atribuicao(self, ctx:CompiladorGVParser.Comando_atribuicaoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#comando_declaracao.
    def enterComando_declaracao(self, ctx:CompiladorGVParser.Comando_declaracaoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#comando_declaracao.
    def exitComando_declaracao(self, ctx:CompiladorGVParser.Comando_declaracaoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#atribuicao.
    def enterAtribuicao(self, ctx:CompiladorGVParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#atribuicao.
    def exitAtribuicao(self, ctx:CompiladorGVParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#incremento.
    def enterIncremento(self, ctx:CompiladorGVParser.IncrementoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#incremento.
    def exitIncremento(self, ctx:CompiladorGVParser.IncrementoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#condicao.
    def enterCondicao(self, ctx:CompiladorGVParser.CondicaoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#condicao.
    def exitCondicao(self, ctx:CompiladorGVParser.CondicaoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#operador.
    def enterOperador(self, ctx:CompiladorGVParser.OperadorContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#operador.
    def exitOperador(self, ctx:CompiladorGVParser.OperadorContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#expressao.
    def enterExpressao(self, ctx:CompiladorGVParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#expressao.
    def exitExpressao(self, ctx:CompiladorGVParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#bloco.
    def enterBloco(self, ctx:CompiladorGVParser.BlocoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#bloco.
    def exitBloco(self, ctx:CompiladorGVParser.BlocoContext):
        pass


    # Enter a parse tree produced by CompiladorGVParser#bloco_funcao.
    def enterBloco_funcao(self, ctx:CompiladorGVParser.Bloco_funcaoContext):
        pass

    # Exit a parse tree produced by CompiladorGVParser#bloco_funcao.
    def exitBloco_funcao(self, ctx:CompiladorGVParser.Bloco_funcaoContext):
        pass



del CompiladorGVParser