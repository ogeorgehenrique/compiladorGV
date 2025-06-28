# Generated from CompiladorGV.g4 by ANTLR 4.13.1
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
        4,1,37,258,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,3,2,68,8,
        2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,76,8,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,
        84,8,4,10,4,12,4,87,9,4,1,5,1,5,1,5,1,6,1,6,1,6,5,6,95,8,6,10,6,
        12,6,98,9,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,3,9,114,8,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,
        10,126,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,3,
        14,151,8,14,1,14,1,14,1,14,1,14,1,14,3,14,158,8,14,1,14,3,14,161,
        8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,172,8,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,183,8,17,1,17,
        1,17,1,17,1,17,1,17,1,17,5,17,191,8,17,10,17,12,17,194,9,17,1,18,
        1,18,1,19,1,19,1,19,5,19,201,8,19,10,19,12,19,204,9,19,1,20,1,20,
        1,20,1,20,1,20,1,20,5,20,212,8,20,10,20,12,20,215,9,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,227,8,20,1,20,1,20,
        1,20,1,20,1,20,1,20,5,20,235,8,20,10,20,12,20,238,9,20,1,21,1,21,
        4,21,242,8,21,11,21,12,21,243,1,21,1,21,1,22,1,22,5,22,250,8,22,
        10,22,12,22,253,9,22,1,22,1,22,1,22,1,22,0,2,34,40,23,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,4,1,0,8,
        9,2,0,16,16,23,28,1,0,21,22,1,0,19,20,269,0,47,1,0,0,0,2,61,1,0,
        0,0,4,63,1,0,0,0,6,72,1,0,0,0,8,80,1,0,0,0,10,88,1,0,0,0,12,91,1,
        0,0,0,14,99,1,0,0,0,16,103,1,0,0,0,18,109,1,0,0,0,20,118,1,0,0,0,
        22,127,1,0,0,0,24,137,1,0,0,0,26,143,1,0,0,0,28,160,1,0,0,0,30,162,
        1,0,0,0,32,171,1,0,0,0,34,182,1,0,0,0,36,195,1,0,0,0,38,197,1,0,
        0,0,40,226,1,0,0,0,42,239,1,0,0,0,44,247,1,0,0,0,46,48,3,2,1,0,47,
        46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,1,1,0,0,
        0,51,62,3,4,2,0,52,62,3,6,3,0,53,62,3,14,7,0,54,62,3,16,8,0,55,62,
        3,18,9,0,56,62,3,20,10,0,57,62,3,22,11,0,58,62,3,24,12,0,59,62,3,
        26,13,0,60,62,3,28,14,0,61,51,1,0,0,0,61,52,1,0,0,0,61,53,1,0,0,
        0,61,54,1,0,0,0,61,55,1,0,0,0,61,56,1,0,0,0,61,57,1,0,0,0,61,58,
        1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,3,1,0,0,0,63,64,7,0,0,0,64,
        65,5,35,0,0,65,67,5,10,0,0,66,68,3,8,4,0,67,66,1,0,0,0,67,68,1,0,
        0,0,68,69,1,0,0,0,69,70,5,11,0,0,70,71,3,44,22,0,71,5,1,0,0,0,72,
        73,5,35,0,0,73,75,5,10,0,0,74,76,3,12,6,0,75,74,1,0,0,0,75,76,1,
        0,0,0,76,77,1,0,0,0,77,78,5,11,0,0,78,79,5,15,0,0,79,7,1,0,0,0,80,
        85,3,10,5,0,81,82,5,14,0,0,82,84,3,10,5,0,83,81,1,0,0,0,84,87,1,
        0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,9,1,0,0,0,87,85,1,0,0,0,88,
        89,7,0,0,0,89,90,5,35,0,0,90,11,1,0,0,0,91,96,3,40,20,0,92,93,5,
        14,0,0,93,95,3,40,20,0,94,92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,
        96,97,1,0,0,0,97,13,1,0,0,0,98,96,1,0,0,0,99,100,5,7,0,0,100,101,
        3,40,20,0,101,102,5,15,0,0,102,15,1,0,0,0,103,104,5,1,0,0,104,105,
        5,10,0,0,105,106,5,35,0,0,106,107,5,11,0,0,107,108,5,15,0,0,108,
        17,1,0,0,0,109,110,5,2,0,0,110,113,5,10,0,0,111,114,5,32,0,0,112,
        114,3,40,20,0,113,111,1,0,0,0,113,112,1,0,0,0,114,115,1,0,0,0,115,
        116,5,11,0,0,116,117,5,15,0,0,117,19,1,0,0,0,118,119,5,3,0,0,119,
        120,5,10,0,0,120,121,3,34,17,0,121,122,5,11,0,0,122,125,3,42,21,
        0,123,124,5,4,0,0,124,126,3,42,21,0,125,123,1,0,0,0,125,126,1,0,
        0,0,126,21,1,0,0,0,127,128,5,5,0,0,128,129,5,10,0,0,129,130,3,30,
        15,0,130,131,5,15,0,0,131,132,3,34,17,0,132,133,5,15,0,0,133,134,
        3,32,16,0,134,135,5,11,0,0,135,136,3,42,21,0,136,23,1,0,0,0,137,
        138,5,6,0,0,138,139,5,10,0,0,139,140,3,34,17,0,140,141,5,11,0,0,
        141,142,3,42,21,0,142,25,1,0,0,0,143,144,3,30,15,0,144,145,5,15,
        0,0,145,27,1,0,0,0,146,147,5,8,0,0,147,150,5,35,0,0,148,149,5,16,
        0,0,149,151,3,40,20,0,150,148,1,0,0,0,150,151,1,0,0,0,151,152,1,
        0,0,0,152,161,5,15,0,0,153,154,5,9,0,0,154,157,5,35,0,0,155,156,
        5,16,0,0,156,158,3,40,20,0,157,155,1,0,0,0,157,158,1,0,0,0,158,159,
        1,0,0,0,159,161,5,15,0,0,160,146,1,0,0,0,160,153,1,0,0,0,161,29,
        1,0,0,0,162,163,5,35,0,0,163,164,5,16,0,0,164,165,3,40,20,0,165,
        31,1,0,0,0,166,167,5,35,0,0,167,172,5,17,0,0,168,169,5,35,0,0,169,
        172,5,18,0,0,170,172,3,30,15,0,171,166,1,0,0,0,171,168,1,0,0,0,171,
        170,1,0,0,0,172,33,1,0,0,0,173,174,6,17,-1,0,174,175,3,40,20,0,175,
        176,3,36,18,0,176,177,3,40,20,0,177,183,1,0,0,0,178,179,5,10,0,0,
        179,180,3,34,17,0,180,181,5,11,0,0,181,183,1,0,0,0,182,173,1,0,0,
        0,182,178,1,0,0,0,183,192,1,0,0,0,184,185,10,3,0,0,185,186,5,29,
        0,0,186,191,3,34,17,4,187,188,10,2,0,0,188,189,5,30,0,0,189,191,
        3,34,17,3,190,184,1,0,0,0,190,187,1,0,0,0,191,194,1,0,0,0,192,190,
        1,0,0,0,192,193,1,0,0,0,193,35,1,0,0,0,194,192,1,0,0,0,195,196,7,
        1,0,0,196,37,1,0,0,0,197,202,3,40,20,0,198,199,5,14,0,0,199,201,
        3,40,20,0,200,198,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,
        1,0,0,0,203,39,1,0,0,0,204,202,1,0,0,0,205,206,6,20,-1,0,206,207,
        5,35,0,0,207,208,5,10,0,0,208,213,3,40,20,0,209,210,5,14,0,0,210,
        212,3,40,20,0,211,209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,
        214,1,0,0,0,214,216,1,0,0,0,215,213,1,0,0,0,216,217,5,11,0,0,217,
        227,1,0,0,0,218,219,5,10,0,0,219,220,3,40,20,0,220,221,5,11,0,0,
        221,227,1,0,0,0,222,227,5,33,0,0,223,227,5,34,0,0,224,227,5,32,0,
        0,225,227,5,35,0,0,226,205,1,0,0,0,226,218,1,0,0,0,226,222,1,0,0,
        0,226,223,1,0,0,0,226,224,1,0,0,0,226,225,1,0,0,0,227,236,1,0,0,
        0,228,229,10,8,0,0,229,230,7,2,0,0,230,235,3,40,20,9,231,232,10,
        7,0,0,232,233,7,3,0,0,233,235,3,40,20,8,234,228,1,0,0,0,234,231,
        1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,41,1,
        0,0,0,238,236,1,0,0,0,239,241,5,12,0,0,240,242,3,2,1,0,241,240,1,
        0,0,0,242,243,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,245,1,
        0,0,0,245,246,5,13,0,0,246,43,1,0,0,0,247,251,5,12,0,0,248,250,3,
        2,1,0,249,248,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,
        0,0,0,252,254,1,0,0,0,253,251,1,0,0,0,254,255,3,14,7,0,255,256,5,
        13,0,0,256,45,1,0,0,0,22,49,61,67,75,85,96,113,125,150,157,160,171,
        182,190,192,202,213,226,234,236,243,251
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
                      "ID", "WS", "ERRO" ]

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
    RULE_lista_argumentos = 19
    RULE_expressao = 20
    RULE_bloco = 21
    RULE_bloco_funcao = 22

    ruleNames =  [ "inicio", "comandos", "comando_declaracao_funcao", "comando_chamada_funcao", 
                   "parametros", "parametro", "argumentos", "comando_retorno", 
                   "comando_ler", "comando_escrever", "comando_se", "comando_para", 
                   "comando_enquanto", "comando_atribuicao", "comando_declaracao", 
                   "atribuicao", "incremento", "condicao", "operador", "lista_argumentos", 
                   "expressao", "bloco", "bloco_funcao" ]

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
    ERRO=37

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
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.comandos()
                self.state = 49 
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
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.comando_declaracao_funcao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.comando_chamada_funcao()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.comando_retorno()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.comando_ler()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.comando_escrever()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.comando_se()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.comando_para()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 58
                self.comando_enquanto()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 59
                self.comando_atribuicao()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 60
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
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 64
            self.match(CompiladorGVParser.ID)
            self.state = 65
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 66
                self.parametros()


            self.state = 69
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 70
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
            self.state = 72
            self.match(CompiladorGVParser.ID)
            self.state = 73
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 64424510464) != 0):
                self.state = 74
                self.argumentos()


            self.state = 77
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 78
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
            self.state = 80
            self.parametro()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 81
                self.match(CompiladorGVParser.VIRGULA)
                self.state = 82
                self.parametro()
                self.state = 87
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
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 89
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
            self.state = 91
            self.expressao(0)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 92
                self.match(CompiladorGVParser.VIRGULA)
                self.state = 93
                self.expressao(0)
                self.state = 98
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
            self.state = 99
            self.match(CompiladorGVParser.RETORNA)
            self.state = 100
            self.expressao(0)
            self.state = 101
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
            self.state = 103
            self.match(CompiladorGVParser.LEIA)
            self.state = 104
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 105
            self.match(CompiladorGVParser.ID)
            self.state = 106
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 107
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
            self.state = 109
            self.match(CompiladorGVParser.ESCREVA)
            self.state = 110
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(CompiladorGVParser.STRING)
                pass

            elif la_ == 2:
                self.state = 112
                self.expressao(0)
                pass


            self.state = 115
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 116
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
            self.state = 118
            self.match(CompiladorGVParser.SE)
            self.state = 119
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 120
            self.condicao(0)
            self.state = 121
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 122
            self.bloco()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 123
                self.match(CompiladorGVParser.SENAO)
                self.state = 124
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
            self.state = 127
            self.match(CompiladorGVParser.PARA)
            self.state = 128
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 129
            self.atribuicao()
            self.state = 130
            self.match(CompiladorGVParser.FINAL)
            self.state = 131
            self.condicao(0)
            self.state = 132
            self.match(CompiladorGVParser.FINAL)
            self.state = 133
            self.incremento()
            self.state = 134
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 135
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
            self.state = 137
            self.match(CompiladorGVParser.ENQUANTO)
            self.state = 138
            self.match(CompiladorGVParser.ABRE_PAR)
            self.state = 139
            self.condicao(0)
            self.state = 140
            self.match(CompiladorGVParser.FECHA_PAR)
            self.state = 141
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
            self.state = 143
            self.atribuicao()
            self.state = 144
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
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(CompiladorGVParser.TIPO_INT)
                self.state = 147
                self.match(CompiladorGVParser.ID)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 148
                    self.match(CompiladorGVParser.RECEBE)
                    self.state = 149
                    self.expressao(0)


                self.state = 152
                self.match(CompiladorGVParser.FINAL)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(CompiladorGVParser.TIPO_STRING)
                self.state = 154
                self.match(CompiladorGVParser.ID)
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 155
                    self.match(CompiladorGVParser.RECEBE)
                    self.state = 156
                    self.expressao(0)


                self.state = 159
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
            self.state = 162
            self.match(CompiladorGVParser.ID)
            self.state = 163
            self.match(CompiladorGVParser.RECEBE)
            self.state = 164
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
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(CompiladorGVParser.ID)
                self.state = 167
                self.match(CompiladorGVParser.INCREMENTO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(CompiladorGVParser.ID)
                self.state = 169
                self.match(CompiladorGVParser.DECREMENTO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
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
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 174
                self.expressao(0)
                self.state = 175
                self.operador()
                self.state = 176
                self.expressao(0)
                pass

            elif la_ == 2:
                self.state = 178
                self.match(CompiladorGVParser.ABRE_PAR)
                self.state = 179
                self.condicao(0)
                self.state = 180
                self.match(CompiladorGVParser.FECHA_PAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 192
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 190
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = CompiladorGVParser.CondicaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicao)
                        self.state = 184
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 185
                        self.match(CompiladorGVParser.AND)
                        self.state = 186
                        self.condicao(4)
                        pass

                    elif la_ == 2:
                        localctx = CompiladorGVParser.CondicaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_condicao)
                        self.state = 187
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 188
                        self.match(CompiladorGVParser.OR)
                        self.state = 189
                        self.condicao(3)
                        pass

             
                self.state = 194
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
            self.state = 195
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


    class Lista_argumentosContext(ParserRuleContext):
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
            return CompiladorGVParser.RULE_lista_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_argumentos" ):
                listener.enterLista_argumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_argumentos" ):
                listener.exitLista_argumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_argumentos" ):
                return visitor.visitLista_argumentos(self)
            else:
                return visitor.visitChildren(self)




    def lista_argumentos(self):

        localctx = CompiladorGVParser.Lista_argumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lista_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.expressao(0)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 198
                self.match(CompiladorGVParser.VIRGULA)
                self.state = 199
                self.expressao(0)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ID(self):
            return self.getToken(CompiladorGVParser.ID, 0)

        def ABRE_PAR(self):
            return self.getToken(CompiladorGVParser.ABRE_PAR, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiladorGVParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(CompiladorGVParser.ExpressaoContext,i)


        def FECHA_PAR(self):
            return self.getToken(CompiladorGVParser.FECHA_PAR, 0)

        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(CompiladorGVParser.VIRGULA)
            else:
                return self.getToken(CompiladorGVParser.VIRGULA, i)

        def INTEIRO(self):
            return self.getToken(CompiladorGVParser.INTEIRO, 0)

        def FLOAT(self):
            return self.getToken(CompiladorGVParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CompiladorGVParser.STRING, 0)

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
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expressao, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 206
                self.match(CompiladorGVParser.ID)
                self.state = 207
                self.match(CompiladorGVParser.ABRE_PAR)
                self.state = 208
                self.expressao(0)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 209
                    self.match(CompiladorGVParser.VIRGULA)
                    self.state = 210
                    self.expressao(0)
                    self.state = 215
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 216
                self.match(CompiladorGVParser.FECHA_PAR)
                pass

            elif la_ == 2:
                self.state = 218
                self.match(CompiladorGVParser.ABRE_PAR)
                self.state = 219
                self.expressao(0)
                self.state = 220
                self.match(CompiladorGVParser.FECHA_PAR)
                pass

            elif la_ == 3:
                self.state = 222
                self.match(CompiladorGVParser.INTEIRO)
                pass

            elif la_ == 4:
                self.state = 223
                self.match(CompiladorGVParser.FLOAT)
                pass

            elif la_ == 5:
                self.state = 224
                self.match(CompiladorGVParser.STRING)
                pass

            elif la_ == 6:
                self.state = 225
                self.match(CompiladorGVParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 234
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = CompiladorGVParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 228
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 229
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 230
                        self.expressao(9)
                        pass

                    elif la_ == 2:
                        localctx = CompiladorGVParser.ExpressaoContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 231
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 232
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 233
                        self.expressao(8)
                        pass

             
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 42, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(CompiladorGVParser.ABRE_CHAVE)
            self.state = 241 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 240
                self.comandos()
                self.state = 243 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 34359739374) != 0)):
                    break

            self.state = 245
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
        self.enterRule(localctx, 44, self.RULE_bloco_funcao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(CompiladorGVParser.ABRE_CHAVE)
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 248
                    self.comandos() 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 254
            self.comando_retorno()
            self.state = 255
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
        self._predicates[20] = self.expressao_sempred
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
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         




