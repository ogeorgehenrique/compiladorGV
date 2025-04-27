# Generated from grammar/CompiladorGV.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,236,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,3,2,66,8,2,1,2,1,2,
        1,2,1,3,1,3,1,3,3,3,74,8,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,82,8,4,10,
        4,12,4,85,9,4,1,5,1,5,1,5,1,6,1,6,1,6,5,6,93,8,6,10,6,12,6,96,9,
        6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,112,
        8,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,124,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,3,14,149,8,14,
        1,14,1,14,1,14,1,14,1,14,3,14,156,8,14,1,14,3,14,159,8,14,1,15,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,170,8,16,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,181,8,17,1,17,1,17,1,17,1,
        17,1,17,1,17,5,17,189,8,17,10,17,12,17,192,9,17,1,18,1,18,1,19,1,
        19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,205,8,19,1,19,1,19,1,
        19,1,19,1,19,1,19,5,19,213,8,19,10,19,12,19,216,9,19,1,20,1,20,4,
        20,220,8,20,11,20,12,20,221,1,20,1,20,1,21,1,21,5,21,228,8,21,10,
        21,12,21,231,9,21,1,21,1,21,1,21,1,21,0,2,34,38,22,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,4,1,0,8,9,2,0,
        16,16,23,28,1,0,21,22,1,0,19,20,245,0,45,1,0,0,0,2,59,1,0,0,0,4,
        61,1,0,0,0,6,70,1,0,0,0,8,78,1,0,0,0,10,86,1,0,0,0,12,89,1,0,0,0,
        14,97,1,0,0,0,16,101,1,0,0,0,18,107,1,0,0,0,20,116,1,0,0,0,22,125,
        1,0,0,0,24,135,1,0,0,0,26,141,1,0,0,0,28,158,1,0,0,0,30,160,1,0,
        0,0,32,169,1,0,0,0,34,180,1,0,0,0,36,193,1,0,0,0,38,204,1,0,0,0,
        40,217,1,0,0,0,42,225,1,0,0,0,44,46,3,2,1,0,45,44,1,0,0,0,46,47,
        1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,1,1,0,0,0,49,60,3,4,2,0,50,
        60,3,6,3,0,51,60,3,14,7,0,52,60,3,16,8,0,53,60,3,18,9,0,54,60,3,
        20,10,0,55,60,3,22,11,0,56,60,3,24,12,0,57,60,3,26,13,0,58,60,3,
        28,14,0,59,49,1,0,0,0,59,50,1,0,0,0,59,51,1,0,0,0,59,52,1,0,0,0,
        59,53,1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,59,56,1,0,0,0,59,57,1,
        0,0,0,59,58,1,0,0,0,60,3,1,0,0,0,61,62,7,0,0,0,62,63,5,35,0,0,63,
        65,5,10,0,0,64,66,3,8,4,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,
        0,0,67,68,5,11,0,0,68,69,3,42,21,0,69,5,1,0,0,0,70,71,5,35,0,0,71,
        73,5,10,0,0,72,74,3,12,6,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,
        0,0,75,76,5,11,0,0,76,77,5,15,0,0,77,7,1,0,0,0,78,83,3,10,5,0,79,
        80,5,14,0,0,80,82,3,10,5,0,81,79,1,0,0,0,82,85,1,0,0,0,83,81,1,0,
        0,0,83,84,1,0,0,0,84,9,1,0,0,0,85,83,1,0,0,0,86,87,7,0,0,0,87,88,
        5,35,0,0,88,11,1,0,0,0,89,94,3,38,19,0,90,91,5,14,0,0,91,93,3,38,
        19,0,92,90,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,
        13,1,0,0,0,96,94,1,0,0,0,97,98,5,7,0,0,98,99,3,38,19,0,99,100,5,
        15,0,0,100,15,1,0,0,0,101,102,5,1,0,0,102,103,5,10,0,0,103,104,5,
        35,0,0,104,105,5,11,0,0,105,106,5,15,0,0,106,17,1,0,0,0,107,108,
        5,2,0,0,108,111,5,10,0,0,109,112,5,32,0,0,110,112,3,38,19,0,111,
        109,1,0,0,0,111,110,1,0,0,0,112,113,1,0,0,0,113,114,5,11,0,0,114,
        115,5,15,0,0,115,19,1,0,0,0,116,117,5,3,0,0,117,118,5,10,0,0,118,
        119,3,34,17,0,119,120,5,11,0,0,120,123,3,40,20,0,121,122,5,4,0,0,
        122,124,3,40,20,0,123,121,1,0,0,0,123,124,1,0,0,0,124,21,1,0,0,0,
        125,126,5,5,0,0,126,127,5,10,0,0,127,128,3,30,15,0,128,129,5,15,
        0,0,129,130,3,34,17,0,130,131,5,15,0,0,131,132,3,32,16,0,132,133,
        5,11,0,0,133,134,3,40,20,0,134,23,1,0,0,0,135,136,5,6,0,0,136,137,
        5,10,0,0,137,138,3,34,17,0,138,139,5,11,0,0,139,140,3,40,20,0,140,
        25,1,0,0,0,141,142,3,30,15,0,142,143,5,15,0,0,143,27,1,0,0,0,144,
        145,5,8,0,0,145,148,5,35,0,0,146,147,5,16,0,0,147,149,3,38,19,0,
        148,146,1,0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,159,5,15,0,0,
        151,152,5,9,0,0,152,155,5,35,0,0,153,154,5,16,0,0,154,156,3,38,19,
        0,155,153,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,159,5,15,0,
        0,158,144,1,0,0,0,158,151,1,0,0,0,159,29,1,0,0,0,160,161,5,35,0,
        0,161,162,5,16,0,0,162,163,3,38,19,0,163,31,1,0,0,0,164,165,5,35,
        0,0,165,170,5,17,0,0,166,167,5,35,0,0,167,170,5,18,0,0,168,170,3,
        30,15,0,169,164,1,0,0,0,169,166,1,0,0,0,169,168,1,0,0,0,170,33,1,
        0,0,0,171,172,6,17,-1,0,172,173,3,38,19,0,173,174,3,36,18,0,174,
        175,3,38,19,0,175,181,1,0,0,0,176,177,5,10,0,0,177,178,3,34,17,0,
        178,179,5,11,0,0,179,181,1,0,0,0,180,171,1,0,0,0,180,176,1,0,0,0,
        181,190,1,0,0,0,182,183,10,3,0,0,183,184,5,29,0,0,184,189,3,34,17,
        4,185,186,10,2,0,0,186,187,5,30,0,0,187,189,3,34,17,3,188,182,1,
        0,0,0,188,185,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,
        0,0,0,191,35,1,0,0,0,192,190,1,0,0,0,193,194,7,1,0,0,194,37,1,0,
        0,0,195,196,6,19,-1,0,196,197,5,10,0,0,197,198,3,38,19,0,198,199,
        5,11,0,0,199,205,1,0,0,0,200,205,5,33,0,0,201,205,5,34,0,0,202,205,
        5,32,0,0,203,205,5,35,0,0,204,195,1,0,0,0,204,200,1,0,0,0,204,201,
        1,0,0,0,204,202,1,0,0,0,204,203,1,0,0,0,205,214,1,0,0,0,206,207,
        10,7,0,0,207,208,7,2,0,0,208,213,3,38,19,8,209,210,10,6,0,0,210,
        211,7,3,0,0,211,213,3,38,19,7,212,206,1,0,0,0,212,209,1,0,0,0,213,
        216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,39,1,0,0,0,216,214,
        1,0,0,0,217,219,5,12,0,0,218,220,3,2,1,0,219,218,1,0,0,0,220,221,
        1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,223,1,0,0,0,223,224,
        5,13,0,0,224,41,1,0,0,0,225,229,5,12,0,0,226,228,3,2,1,0,227,226,
        1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,232,
        1,0,0,0,231,229,1,0,0,0,232,233,3,14,7,0,233,234,5,13,0,0,234,43,
        1,0,0,0,20,47,59,65,73,83,94,111,123,148,155,158,169,180,188,190,
        204,212,214,221,229
    ]

class CompiladorGVParser ( Parser ):

    grammarFileName = "CompiladorGV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'leia'", "'escreva'", "'se'", "'senao'", 
                     "'para'", "'enquanto'", "'retorna'", "'int'", "'string'", 
                     "'('", "')'", "'{'", "'}'", "','", "';'", "'='", "'++'", 
                     "'--'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'>'", "'<'", "'<='", "'>='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "LEIA", "ESCREVA", "SE", "SENAO", "PARA", 
                      "ENQUANTO", "RETORNA", "TIPO_INT", "TIPO_STRING", 
                      "ABRE_PAR", "FECHA_PAR", "ABRE_CHAVE", "FECHA_CHAVE", 
                      "VIRGULA", "FINAL", "RECEBE", "INCREMENTO", "DECREMENTO", 
                      "PLUS", "MINUS", "MULT", "DIV", "IGUAL_EXATO", "DIFERENTE", 
                      "MAIOR_Q", "MENOR_Q", "MENOR_IGUAL_Q", "MAIOR_IGUAL_Q", 
                      "AND", "OR", "NOT", "STRING", "INTEIRO", "FLOAT", 
                      "ID", "WS" ]

    RULE_inicio = 0
    RULE_comandos = 1
    RULE_comando_declaracao_funcao = 2
    RULE_comando_chamada_funcao = 3
    RULE_parametros = 4
    RULE_parametro = 5
    RULE_argumentos = 6
    RULE_comando_retorno = 7
    RULE_comando_ler = 8
    RULE_comando_escrever = 9
    RULE_comando_se = 10
    RULE_comando_para = 11
    RULE_comando_enquanto = 12
    RULE_comando_atribuicao = 13
    RULE_comando_declaracao = 14
    RULE_atribuicao = 15
    RULE_incremento = 16
    RULE_condicao = 17
    RULE_operador = 18
    RULE_expressao = 19
    RULE_bloco = 20
    RULE_bloco_funcao = 21

    ruleNames =  [ "inicio", "comandos", "comando_declaracao_funcao", "comando_chamada_funcao", 
                   "parametros", "parametro", "argumentos", "comando_retorno", 
                   "comando_ler", "comando_escrever", "comando_se", "comando_para", 
                   "comando_enquanto", "comando_atribuicao", "comando_declaracao", 
                   "atribuicao", "incremento", "condicao", "operador", "expressao", 
                   "bloco", "bloco_funcao" ]

    EOF = Token.EOF
    LEIA=1
    ESCREVA=2
    SE=3
    SENAO=4
    PARA=5
    ENQUANTO=6
    RETORNA=7
    TIPO_INT=8
    TIPO_STRING=9
    ABRE_PAR=10
    FECHA_PAR=11
    ABRE_CHAVE=12
    FECHA_CHAVE=13
    VIRGULA=14
    FINAL=15
    RECEBE=16
    INCREMENTO=17
    DECREMENTO=18
    PLUS=19
    MINUS=20
    MULT=21
    DIV=22
    IGUAL_EXATO=23
    DIFERENTE=24
    MAIOR_Q=25
    MENOR_Q=26
    MENOR_IGUAL_Q=27
    MAIOR_IGUAL_Q=28
    AND=29
    OR=30
    NOT=31
    STRING=32
    INTEIRO=33
    FLOAT=34
    ID=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.ComandosContext,i)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicio" ):
                return visitor.visitInicio(self)
            else:
                return visitor.visitChildren(self)




    def inicio(self):

        localctx = CompiladorGVParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.comandos()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 34359739374) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando_declaracao_funcao(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_declaracao_funcaoContext,0)


        def comando_chamada_funcao(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_chamada_funcaoContext,0)


        def comando_retorno(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_retornoContext,0)


        def comando_ler(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_lerContext,0)


        def comando_escrever(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_escreverContext,0)


        def comando_se(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_seContext,0)


        def comando_para(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_paraContext,0)


        def comando_enquanto(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_enquantoContext,0)


        def comando_atribuicao(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_atribuicaoContext,0)


        def comando_declaracao(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_declaracaoContext,0)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandos" ):
                return visitor.visitComandos(self)
            else:
                return visitor.visitChildren(self)




    def comandos(self):

        localctx = CompiladorGVParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comandos)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.comando_declaracao_funcao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.comando_chamada_funcao()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.comando_retorno()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.comando_ler()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.comando_escrever()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 54
                self.comando_se()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 55
                self.comando_para()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 56
                self.comando_enquanto()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 57
                self.comando_atribuicao()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 58
                self.comando_declaracao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_declaracao_funcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def bloco_funcao(self):
            return self.getTypedRuleContext(CompiladorGVParser.Bloco_funcaoContext,0)


        def TIPO_INT(self):
            return self.getToken(CompiladorGVParser.TIPO_INT, 0)

        def TIPO_STRING(self):
            return self.getToken(CompiladorGVParser.TIPO_STRING, 0)

        def parametros(self):
            return self.getTypedRuleContext(CompiladorGVParser.ParametrosContext,0)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_declaracao_funcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_declaracao_funcao" ):
                listener.enterComando_declaracao_funcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_declaracao_funcao" ):
                listener.exitComando_declaracao_funcao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_declaracao_funcao" ):
                return visitor.visitComando_declaracao_funcao(self)
            else:
                return visitor.visitChildren(self)




    def comando_declaracao_funcao(self):

        localctx = CompiladorGVParser.Comando_declaracao_funcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comando_declaracao_funcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            self.match(CompiladorGVParser.ID)
            self.state = 63
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 64
                self.parametros()


            self.state = 67
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 68
            self.bloco_funcao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_chamada_funcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def FINAL(self):
            return self.getToken(CompiladorGVParser.FINAL, 0)

        def argumentos(self):
            return self.getTypedRuleContext(CompiladorGVParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_chamada_funcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_chamada_funcao" ):
                listener.enterComando_chamada_funcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_chamada_funcao" ):
                listener.exitComando_chamada_funcao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_chamada_funcao" ):
                return visitor.visitComando_chamada_funcao(self)
            else:
                return visitor.visitChildren(self)




    def comando_chamada_funcao(self):

        localctx = CompiladorGVParser.Comando_chamada_funcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comando_chamada_funcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(CompiladorGVParser.ID)
            self.state = 71
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 64424510464) != 0):
                self.state = 72
                self.argumentos()


            self.state = 75
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 76
            self.match(CompiladorGVParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.ParametroContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.ParametroContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorGVParser.VIRGULA)
            else:
                return self.getToken(CompiladorGVParser.VIRGULA, i)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = CompiladorGVParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.parametro()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 79
                self.match(CompiladorGVParser.VIRGULA)
                self.state = 80
                self.parametro()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def TIPO_INT(self):
            return self.getToken(CompiladorGVParser.TIPO_INT, 0)

        def TIPO_STRING(self):
            return self.getToken(CompiladorGVParser.TIPO_STRING, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = CompiladorGVParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 87
            self.match(CompiladorGVParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.ExpressaoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorGVParser.VIRGULA)
            else:
                return self.getToken(CompiladorGVParser.VIRGULA, i)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = CompiladorGVParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.expressao(0)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 90
                self.match(CompiladorGVParser.VIRGULA)
                self.state = 91
                self.expressao(0)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_retornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNA(self):
            return self.getToken(CompiladorGVParser.RETORNA, 0)

        def expressao(self):
            return self.getTypedRuleContext(CompiladorGVParser.ExpressaoContext,0)


        def FINAL(self):
            return self.getToken(CompiladorGVParser.FINAL, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_retorno" ):
                listener.enterComando_retorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_retorno" ):
                listener.exitComando_retorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_retorno" ):
                return visitor.visitComando_retorno(self)
            else:
                return visitor.visitChildren(self)




    def comando_retorno(self):

        localctx = CompiladorGVParser.Comando_retornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comando_retorno)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(CompiladorGVParser.RETORNA)
            self.state = 98
            self.expressao(0)
            self.state = 99
            self.match(CompiladorGVParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_lerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEIA(self):
            return self.getToken(CompiladorGVParser.LEIA, 0)

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def FINAL(self):
            return self.getToken(CompiladorGVParser.FINAL, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_ler

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_ler" ):
                listener.enterComando_ler(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_ler" ):
                listener.exitComando_ler(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_ler" ):
                return visitor.visitComando_ler(self)
            else:
                return visitor.visitChildren(self)




    def comando_ler(self):

        localctx = CompiladorGVParser.Comando_lerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comando_ler)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(CompiladorGVParser.LEIA)
            self.state = 102
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 103
            self.match(CompiladorGVParser.ID)
            self.state = 104
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 105
            self.match(CompiladorGVParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_escreverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCREVA(self):
            return self.getToken(CompiladorGVParser.ESCREVA, 0)

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def FINAL(self):
            return self.getToken(CompiladorGVParser.FINAL, 0)

        def STRING(self):
            return self.getToken(CompiladorGVParser.STRING, 0)

        def expressao(self):
            return self.getTypedRuleContext(CompiladorGVParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_escrever

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_escrever" ):
                listener.enterComando_escrever(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_escrever" ):
                listener.exitComando_escrever(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_escrever" ):
                return visitor.visitComando_escrever(self)
            else:
                return visitor.visitChildren(self)




    def comando_escrever(self):

        localctx = CompiladorGVParser.Comando_escreverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comando_escrever)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(CompiladorGVParser.ESCREVA)
            self.state = 108
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 109
                self.match(CompiladorGVParser.STRING)
                pass

            elif la_ == 2:
                self.state = 110
                self.expressao(0)
                pass


            self.state = 113
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 114
            self.match(CompiladorGVParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_seContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SE(self):
            return self.getToken(CompiladorGVParser.SE, 0)

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def condicao(self):
            return self.getTypedRuleContext(CompiladorGVParser.CondicaoContext,0)


        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def bloco(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.BlocoContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.BlocoContext,i)


        def SENAO(self):
            return self.getToken(CompiladorGVParser.SENAO, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_se

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_se" ):
                listener.enterComando_se(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_se" ):
                listener.exitComando_se(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_se" ):
                return visitor.visitComando_se(self)
            else:
                return visitor.visitChildren(self)




    def comando_se(self):

        localctx = CompiladorGVParser.Comando_seContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comando_se)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(CompiladorGVParser.SE)
            self.state = 117
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 118
            self.condicao(0)
            self.state = 119
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 120
            self.bloco()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 121
                self.match(CompiladorGVParser.SENAO)
                self.state = 122
                self.bloco()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(CompiladorGVParser.PARA, 0)

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def atribuicao(self):
            return self.getTypedRuleContext(CompiladorGVParser.AtribuicaoContext,0)


        def FINAL(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorGVParser.FINAL)
            else:
                return self.getToken(CompiladorGVParser.FINAL, i)

        def condicao(self):
            return self.getTypedRuleContext(CompiladorGVParser.CondicaoContext,0)


        def incremento(self):
            return self.getTypedRuleContext(CompiladorGVParser.IncrementoContext,0)


        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def bloco(self):
            return self.getTypedRuleContext(CompiladorGVParser.BlocoContext,0)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_para" ):
                listener.enterComando_para(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_para" ):
                listener.exitComando_para(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_para" ):
                return visitor.visitComando_para(self)
            else:
                return visitor.visitChildren(self)




    def comando_para(self):

        localctx = CompiladorGVParser.Comando_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comando_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(CompiladorGVParser.PARA)
            self.state = 126
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 127
            self.atribuicao()
            self.state = 128
            self.match(CompiladorGVParser.FINAL)
            self.state = 129
            self.condicao(0)
            self.state = 130
            self.match(CompiladorGVParser.FINAL)
            self.state = 131
            self.incremento()
            self.state = 132
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 133
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_enquantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENQUANTO(self):
            return self.getToken(CompiladorGVParser.ENQUANTO, 0)

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def condicao(self):
            return self.getTypedRuleContext(CompiladorGVParser.CondicaoContext,0)


        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def bloco(self):
            return self.getTypedRuleContext(CompiladorGVParser.BlocoContext,0)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_enquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_enquanto" ):
                listener.enterComando_enquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_enquanto" ):
                listener.exitComando_enquanto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_enquanto" ):
                return visitor.visitComando_enquanto(self)
            else:
                return visitor.visitChildren(self)




    def comando_enquanto(self):

        localctx = CompiladorGVParser.Comando_enquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comando_enquanto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(CompiladorGVParser.ENQUANTO)
            self.state = 136
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 137
            self.condicao(0)
            self.state = 138
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 139
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_atribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(CompiladorGVParser.AtribuicaoContext,0)


        def FINAL(self):
            return self.getToken(CompiladorGVParser.FINAL, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_atribuicao" ):
                listener.enterComando_atribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_atribuicao" ):
                listener.exitComando_atribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_atribuicao" ):
                return visitor.visitComando_atribuicao(self)
            else:
                return visitor.visitChildren(self)




    def comando_atribuicao(self):

        localctx = CompiladorGVParser.Comando_atribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comando_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.atribuicao()
            self.state = 142
            self.match(CompiladorGVParser.FINAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_declaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_INT(self):
            return self.getToken(CompiladorGVParser.TIPO_INT, 0)

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def FINAL(self):
            return self.getToken(CompiladorGVParser.FINAL, 0)

        def RECEBE(self):
            return self.getToken(CompiladorGVParser.RECEBE, 0)

        def expressao(self):
            return self.getTypedRuleContext(CompiladorGVParser.ExpressaoContext,0)


        def TIPO_STRING(self):
            return self.getToken(CompiladorGVParser.TIPO_STRING, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_comando_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_declaracao" ):
                listener.enterComando_declaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_declaracao" ):
                listener.exitComando_declaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_declaracao" ):
                return visitor.visitComando_declaracao(self)
            else:
                return visitor.visitChildren(self)




    def comando_declaracao(self):

        localctx = CompiladorGVParser.Comando_declaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_comando_declaracao)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(CompiladorGVParser.TIPO_INT)
                self.state = 145
                self.match(CompiladorGVParser.ID)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 146
                    self.match(CompiladorGVParser.RECEBE)
                    self.state = 147
                    self.expressao(0)


                self.state = 150
                self.match(CompiladorGVParser.FINAL)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(CompiladorGVParser.TIPO_STRING)
                self.state = 152
                self.match(CompiladorGVParser.ID)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 153
                    self.match(CompiladorGVParser.RECEBE)
                    self.state = 154
                    self.expressao(0)


                self.state = 157
                self.match(CompiladorGVParser.FINAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def RECEBE(self):
            return self.getToken(CompiladorGVParser.RECEBE, 0)

        def expressao(self):
            return self.getTypedRuleContext(CompiladorGVParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = CompiladorGVParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(CompiladorGVParser.ID)
            self.state = 161
            self.match(CompiladorGVParser.RECEBE)
            self.state = 162
            self.expressao(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncrementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def INCREMENTO(self):
            return self.getToken(CompiladorGVParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(CompiladorGVParser.DECREMENTO, 0)

        def atribuicao(self):
            return self.getTypedRuleContext(CompiladorGVParser.AtribuicaoContext,0)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_incremento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncremento" ):
                listener.enterIncremento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncremento" ):
                listener.exitIncremento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncremento" ):
                return visitor.visitIncremento(self)
            else:
                return visitor.visitChildren(self)




    def incremento(self):

        localctx = CompiladorGVParser.IncrementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_incremento)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(CompiladorGVParser.ID)
                self.state = 165
                self.match(CompiladorGVParser.INCREMENTO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(CompiladorGVParser.ID)
                self.state = 167
                self.match(CompiladorGVParser.DECREMENTO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.atribuicao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.ExpressaoContext,i)


        def operador(self):
            return self.getTypedRuleContext(CompiladorGVParser.OperadorContext,0)


        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def condicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.CondicaoContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.CondicaoContext,i)


        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def AND(self):
            return self.getToken(CompiladorGVParser.AND, 0)

        def OR(self):
            return self.getToken(CompiladorGVParser.OR, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicao" ):
                return visitor.visitCondicao(self)
            else:
                return visitor.visitChildren(self)



    def condicao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorGVParser.CondicaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_condicao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 172
                self.expressao(0)
                self.state = 173
                self.operador()
                self.state = 174
                self.expressao(0)
                pass

            elif la_ == 2:
                self.state = 176
                self.match(CompiladorGVParser.ABRE_PAR)
                self.state = 177
                self.condicao(0)
                self.state = 178
                self.match(CompiladorGVParser.FECHA_PAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 188
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = CompiladorGVParser.CondicaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicao)
                        self.state = 182
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 183
                        self.match(CompiladorGVParser.AND)
                        self.state = 184
                        self.condicao(4)
                        pass

                    elif la_ == 2:
                        localctx = CompiladorGVParser.CondicaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicao)
                        self.state = 185
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 186
                        self.match(CompiladorGVParser.OR)
                        self.state = 187
                        self.condicao(3)
                        pass

             
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL_EXATO(self):
            return self.getToken(CompiladorGVParser.IGUAL_EXATO, 0)

        def DIFERENTE(self):
            return self.getToken(CompiladorGVParser.DIFERENTE, 0)

        def MAIOR_Q(self):
            return self.getToken(CompiladorGVParser.MAIOR_Q, 0)

        def MENOR_Q(self):
            return self.getToken(CompiladorGVParser.MENOR_Q, 0)

        def MAIOR_IGUAL_Q(self):
            return self.getToken(CompiladorGVParser.MAIOR_IGUAL_Q, 0)

        def MENOR_IGUAL_Q(self):
            return self.getToken(CompiladorGVParser.MENOR_IGUAL_Q, 0)

        def RECEBE(self):
            return self.getToken(CompiladorGVParser.RECEBE, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_operador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador" ):
                listener.enterOperador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador" ):
                listener.exitOperador(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperador" ):
                return visitor.visitOperador(self)
            else:
                return visitor.visitChildren(self)




    def operador(self):

        localctx = CompiladorGVParser.OperadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 528547840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.ExpressaoContext,i)


        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def INTEIRO(self):
            return self.getToken(CompiladorGVParser.INTEIRO, 0)

        def FLOAT(self):
            return self.getToken(CompiladorGVParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CompiladorGVParser.STRING, 0)

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def MULT(self):
            return self.getToken(CompiladorGVParser.MULT, 0)

        def DIV(self):
            return self.getToken(CompiladorGVParser.DIV, 0)

        def PLUS(self):
            return self.getToken(CompiladorGVParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CompiladorGVParser.MINUS, 0)

        def getRuleIndex(self):
            return CompiladorGVParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompiladorGVParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expressao, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 196
                self.match(CompiladorGVParser.ABRE_PAR)
                self.state = 197
                self.expressao(0)
                self.state = 198
                self.match(CompiladorGVParser.FECHA_PAR)
                pass
            elif token in [33]:
                self.state = 200
                self.match(CompiladorGVParser.INTEIRO)
                pass
            elif token in [34]:
                self.state = 201
                self.match(CompiladorGVParser.FLOAT)
                pass
            elif token in [32]:
                self.state = 202
                self.match(CompiladorGVParser.STRING)
                pass
            elif token in [35]:
                self.state = 203
                self.match(CompiladorGVParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 212
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = CompiladorGVParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 206
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 207
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 208
                        self.expressao(8)
                        pass

                    elif la_ == 2:
                        localctx = CompiladorGVParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 209
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 210
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 211
                        self.expressao(7)
                        pass

             
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_CHAVE(self):
            return self.getToken(CompiladorGVParser.ABRE_CHAVE, 0)

        def FECHA_CHAVE(self):
            return self.getToken(CompiladorGVParser.FECHA_CHAVE, 0)

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.ComandosContext,i)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco" ):
                return visitor.visitBloco(self)
            else:
                return visitor.visitChildren(self)




    def bloco(self):

        localctx = CompiladorGVParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(CompiladorGVParser.ABRE_CHAVE)
            self.state = 219 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 218
                self.comandos()
                self.state = 221 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 34359739374) != 0)):
                    break

            self.state = 223
            self.match(CompiladorGVParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bloco_funcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_CHAVE(self):
            return self.getToken(CompiladorGVParser.ABRE_CHAVE, 0)

        def comando_retorno(self):
            return self.getTypedRuleContext(CompiladorGVParser.Comando_retornoContext,0)


        def FECHA_CHAVE(self):
            return self.getToken(CompiladorGVParser.FECHA_CHAVE, 0)

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.ComandosContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.ComandosContext,i)


        def getRuleIndex(self):
            return CompiladorGVParser.RULE_bloco_funcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco_funcao" ):
                listener.enterBloco_funcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco_funcao" ):
                listener.exitBloco_funcao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco_funcao" ):
                return visitor.visitBloco_funcao(self)
            else:
                return visitor.visitChildren(self)




    def bloco_funcao(self):

        localctx = CompiladorGVParser.Bloco_funcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_bloco_funcao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(CompiladorGVParser.ABRE_CHAVE)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 226
                    self.comandos() 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 232
            self.comando_retorno()
            self.state = 233
            self.match(CompiladorGVParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.condicao_sempred
        self._predicates[19] = self.expressao_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condicao_sempred(self, localctx:CondicaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




