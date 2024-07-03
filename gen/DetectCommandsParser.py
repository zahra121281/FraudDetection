# Generated from C:/Term 6/Compiler design project/FraudDetection/grammar/DetectCommands.g4 by ANTLR 4.13.1
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
        4,1,24,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,56,
        8,1,10,1,12,1,59,9,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,
        1,5,1,6,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,7,1,7,1,7,5,7,84,8,
        7,10,7,12,7,87,9,7,1,8,1,8,1,8,5,8,92,8,8,10,8,12,8,95,9,8,1,9,1,
        9,1,10,4,10,100,8,10,11,10,12,10,101,1,11,1,11,1,11,1,11,1,11,3,
        11,109,8,11,1,11,5,11,112,8,11,10,11,12,11,115,9,11,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,
        18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,0,0,139,0,42,1,0,0,0,2,49,
        1,0,0,0,4,60,1,0,0,0,6,63,1,0,0,0,8,66,1,0,0,0,10,69,1,0,0,0,12,
        72,1,0,0,0,14,80,1,0,0,0,16,88,1,0,0,0,18,96,1,0,0,0,20,99,1,0,0,
        0,22,103,1,0,0,0,24,116,1,0,0,0,26,121,1,0,0,0,28,126,1,0,0,0,30,
        130,1,0,0,0,32,134,1,0,0,0,34,139,1,0,0,0,36,142,1,0,0,0,38,145,
        1,0,0,0,40,148,1,0,0,0,42,43,3,2,1,0,43,44,3,12,6,0,44,45,3,14,7,
        0,45,46,3,16,8,0,46,47,3,20,10,0,47,48,5,0,0,1,48,1,1,0,0,0,49,50,
        5,1,0,0,50,51,3,4,2,0,51,52,3,6,3,0,52,53,3,8,4,0,53,57,3,10,5,0,
        54,56,5,24,0,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,
        0,0,0,58,3,1,0,0,0,59,57,1,0,0,0,60,61,5,2,0,0,61,62,5,19,0,0,62,
        5,1,0,0,0,63,64,5,3,0,0,64,65,5,19,0,0,65,7,1,0,0,0,66,67,5,4,0,
        0,67,68,5,22,0,0,68,9,1,0,0,0,69,70,5,5,0,0,70,71,5,19,0,0,71,11,
        1,0,0,0,72,73,5,6,0,0,73,77,3,18,9,0,74,76,5,24,0,0,75,74,1,0,0,
        0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,13,1,0,0,0,79,77,
        1,0,0,0,80,81,5,7,0,0,81,85,3,18,9,0,82,84,5,24,0,0,83,82,1,0,0,
        0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,15,1,0,0,0,87,85,
        1,0,0,0,88,89,5,8,0,0,89,93,3,18,9,0,90,92,5,24,0,0,91,90,1,0,0,
        0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,17,1,0,0,0,95,93,
        1,0,0,0,96,97,5,19,0,0,97,19,1,0,0,0,98,100,3,22,11,0,99,98,1,0,
        0,0,100,101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,21,1,0,0,
        0,103,108,5,9,0,0,104,109,3,24,12,0,105,109,3,26,13,0,106,109,3,
        28,14,0,107,109,3,30,15,0,108,104,1,0,0,0,108,105,1,0,0,0,108,106,
        1,0,0,0,108,107,1,0,0,0,109,113,1,0,0,0,110,112,5,24,0,0,111,110,
        1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,23,1,
        0,0,0,115,113,1,0,0,0,116,117,5,10,0,0,117,118,3,34,17,0,118,119,
        3,36,18,0,119,120,3,38,19,0,120,25,1,0,0,0,121,122,5,11,0,0,122,
        123,3,34,17,0,123,124,3,36,18,0,124,125,3,38,19,0,125,27,1,0,0,0,
        126,127,5,12,0,0,127,128,3,34,17,0,128,129,3,36,18,0,129,29,1,0,
        0,0,130,131,5,13,0,0,131,132,3,40,20,0,132,133,3,38,19,0,133,31,
        1,0,0,0,134,135,5,14,0,0,135,136,3,34,17,0,136,137,3,36,18,0,137,
        138,3,38,19,0,138,33,1,0,0,0,139,140,5,15,0,0,140,141,5,21,0,0,141,
        35,1,0,0,0,142,143,5,16,0,0,143,144,5,21,0,0,144,37,1,0,0,0,145,
        146,5,17,0,0,146,147,5,20,0,0,147,39,1,0,0,0,148,149,5,18,0,0,149,
        150,5,20,0,0,150,41,1,0,0,0,7,57,77,85,93,101,108,113
    ]

class DetectCommandsParser ( Parser ):

    grammarFileName = "DetectCommands.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Setting'", "'url='", "'username='", 
                     "'pass='", "'Databasename='", "'LoadTerminal'", "'LoadCustomer'", 
                     "'LoadTransaction'", "'Detect'", "'customer'", "'terminal'", 
                     "'transactions_of_each_period'", "'cc_relationship_with_degree'", 
                     "'structured_transactions'", "'startdate='", "'enddate='", 
                     "'limit='", "'degree='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "NUMBER", 
                      "DATE", "Pass", "WS", "NewLine" ]

    RULE_start = 0
    RULE_setting = 1
    RULE_url = 2
    RULE_username = 3
    RULE_pass = 4
    RULE_dbname = 5
    RULE_load_terminal = 6
    RULE_load_customer = 7
    RULE_load_transaction = 8
    RULE_path = 9
    RULE_commands = 10
    RULE_command = 11
    RULE_detect_customer = 12
    RULE_detect_terminal = 13
    RULE_detect_date_range = 14
    RULE_detect_degree_limit = 15
    RULE_detect_structured_transactions = 16
    RULE_start_date = 17
    RULE_end_date = 18
    RULE_limit = 19
    RULE_degree = 20

    ruleNames =  [ "start", "setting", "url", "username", "pass", "dbname", 
                   "load_terminal", "load_customer", "load_transaction", 
                   "path", "commands", "command", "detect_customer", "detect_terminal", 
                   "detect_date_range", "detect_degree_limit", "detect_structured_transactions", 
                   "start_date", "end_date", "limit", "degree" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    STRING=19
    NUMBER=20
    DATE=21
    Pass=22
    WS=23
    NewLine=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def setting(self):
            return self.getTypedRuleContext(DetectCommandsParser.SettingContext,0)


        def load_terminal(self):
            return self.getTypedRuleContext(DetectCommandsParser.Load_terminalContext,0)


        def load_customer(self):
            return self.getTypedRuleContext(DetectCommandsParser.Load_customerContext,0)


        def load_transaction(self):
            return self.getTypedRuleContext(DetectCommandsParser.Load_transactionContext,0)


        def commands(self):
            return self.getTypedRuleContext(DetectCommandsParser.CommandsContext,0)


        def EOF(self):
            return self.getToken(DetectCommandsParser.EOF, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = DetectCommandsParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.setting()
            self.state = 43
            self.load_terminal()
            self.state = 44
            self.load_customer()
            self.state = 45
            self.load_transaction()
            self.state = 46
            self.commands()
            self.state = 47
            self.match(DetectCommandsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SettingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def url(self):
            return self.getTypedRuleContext(DetectCommandsParser.UrlContext,0)


        def username(self):
            return self.getTypedRuleContext(DetectCommandsParser.UsernameContext,0)


        def pass_(self):
            return self.getTypedRuleContext(DetectCommandsParser.PassContext,0)


        def dbname(self):
            return self.getTypedRuleContext(DetectCommandsParser.DbnameContext,0)


        def NewLine(self, i:int=None):
            if i is None:
                return self.getTokens(DetectCommandsParser.NewLine)
            else:
                return self.getToken(DetectCommandsParser.NewLine, i)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_setting

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetting" ):
                listener.enterSetting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetting" ):
                listener.exitSetting(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetting" ):
                return visitor.visitSetting(self)
            else:
                return visitor.visitChildren(self)




    def setting(self):

        localctx = DetectCommandsParser.SettingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_setting)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(DetectCommandsParser.T__0)
            self.state = 50
            self.url()
            self.state = 51
            self.username()
            self.state = 52
            self.pass_()
            self.state = 53
            self.dbname()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 54
                self.match(DetectCommandsParser.NewLine)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DetectCommandsParser.STRING, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUrl" ):
                return visitor.visitUrl(self)
            else:
                return visitor.visitChildren(self)




    def url(self):

        localctx = DetectCommandsParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(DetectCommandsParser.T__1)
            self.state = 61
            self.match(DetectCommandsParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsernameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DetectCommandsParser.STRING, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_username

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsername" ):
                listener.enterUsername(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsername" ):
                listener.exitUsername(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsername" ):
                return visitor.visitUsername(self)
            else:
                return visitor.visitChildren(self)




    def username(self):

        localctx = DetectCommandsParser.UsernameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_username)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(DetectCommandsParser.T__2)
            self.state = 64
            self.match(DetectCommandsParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Pass(self):
            return self.getToken(DetectCommandsParser.Pass, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_pass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPass" ):
                listener.enterPass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPass" ):
                listener.exitPass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPass" ):
                return visitor.visitPass(self)
            else:
                return visitor.visitChildren(self)




    def pass_(self):

        localctx = DetectCommandsParser.PassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(DetectCommandsParser.T__3)
            self.state = 67
            self.match(DetectCommandsParser.Pass)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DbnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DetectCommandsParser.STRING, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_dbname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDbname" ):
                listener.enterDbname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDbname" ):
                listener.exitDbname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDbname" ):
                return visitor.visitDbname(self)
            else:
                return visitor.visitChildren(self)




    def dbname(self):

        localctx = DetectCommandsParser.DbnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dbname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(DetectCommandsParser.T__4)
            self.state = 70
            self.match(DetectCommandsParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Load_terminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self):
            return self.getTypedRuleContext(DetectCommandsParser.PathContext,0)


        def NewLine(self, i:int=None):
            if i is None:
                return self.getTokens(DetectCommandsParser.NewLine)
            else:
                return self.getToken(DetectCommandsParser.NewLine, i)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_load_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad_terminal" ):
                listener.enterLoad_terminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad_terminal" ):
                listener.exitLoad_terminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoad_terminal" ):
                return visitor.visitLoad_terminal(self)
            else:
                return visitor.visitChildren(self)




    def load_terminal(self):

        localctx = DetectCommandsParser.Load_terminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_load_terminal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(DetectCommandsParser.T__5)
            self.state = 73
            self.path()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 74
                self.match(DetectCommandsParser.NewLine)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Load_customerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self):
            return self.getTypedRuleContext(DetectCommandsParser.PathContext,0)


        def NewLine(self, i:int=None):
            if i is None:
                return self.getTokens(DetectCommandsParser.NewLine)
            else:
                return self.getToken(DetectCommandsParser.NewLine, i)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_load_customer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad_customer" ):
                listener.enterLoad_customer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad_customer" ):
                listener.exitLoad_customer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoad_customer" ):
                return visitor.visitLoad_customer(self)
            else:
                return visitor.visitChildren(self)




    def load_customer(self):

        localctx = DetectCommandsParser.Load_customerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_load_customer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(DetectCommandsParser.T__6)
            self.state = 81
            self.path()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 82
                self.match(DetectCommandsParser.NewLine)
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


    class Load_transactionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self):
            return self.getTypedRuleContext(DetectCommandsParser.PathContext,0)


        def NewLine(self, i:int=None):
            if i is None:
                return self.getTokens(DetectCommandsParser.NewLine)
            else:
                return self.getToken(DetectCommandsParser.NewLine, i)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_load_transaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad_transaction" ):
                listener.enterLoad_transaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad_transaction" ):
                listener.exitLoad_transaction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoad_transaction" ):
                return visitor.visitLoad_transaction(self)
            else:
                return visitor.visitChildren(self)




    def load_transaction(self):

        localctx = DetectCommandsParser.Load_transactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_load_transaction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(DetectCommandsParser.T__7)
            self.state = 89
            self.path()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 90
                self.match(DetectCommandsParser.NewLine)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(DetectCommandsParser.STRING, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = DetectCommandsParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(DetectCommandsParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DetectCommandsParser.CommandContext)
            else:
                return self.getTypedRuleContext(DetectCommandsParser.CommandContext,i)


        def getRuleIndex(self):
            return DetectCommandsParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommands" ):
                return visitor.visitCommands(self)
            else:
                return visitor.visitChildren(self)




    def commands(self):

        localctx = DetectCommandsParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.command()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def detect_customer(self):
            return self.getTypedRuleContext(DetectCommandsParser.Detect_customerContext,0)


        def detect_terminal(self):
            return self.getTypedRuleContext(DetectCommandsParser.Detect_terminalContext,0)


        def detect_date_range(self):
            return self.getTypedRuleContext(DetectCommandsParser.Detect_date_rangeContext,0)


        def detect_degree_limit(self):
            return self.getTypedRuleContext(DetectCommandsParser.Detect_degree_limitContext,0)


        def NewLine(self, i:int=None):
            if i is None:
                return self.getTokens(DetectCommandsParser.NewLine)
            else:
                return self.getToken(DetectCommandsParser.NewLine, i)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = DetectCommandsParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(DetectCommandsParser.T__8)
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 104
                self.detect_customer()
                pass
            elif token in [11]:
                self.state = 105
                self.detect_terminal()
                pass
            elif token in [12]:
                self.state = 106
                self.detect_date_range()
                pass
            elif token in [13]:
                self.state = 107
                self.detect_degree_limit()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 110
                self.match(DetectCommandsParser.NewLine)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detect_customerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start_date(self):
            return self.getTypedRuleContext(DetectCommandsParser.Start_dateContext,0)


        def end_date(self):
            return self.getTypedRuleContext(DetectCommandsParser.End_dateContext,0)


        def limit(self):
            return self.getTypedRuleContext(DetectCommandsParser.LimitContext,0)


        def getRuleIndex(self):
            return DetectCommandsParser.RULE_detect_customer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetect_customer" ):
                listener.enterDetect_customer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetect_customer" ):
                listener.exitDetect_customer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetect_customer" ):
                return visitor.visitDetect_customer(self)
            else:
                return visitor.visitChildren(self)




    def detect_customer(self):

        localctx = DetectCommandsParser.Detect_customerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_detect_customer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(DetectCommandsParser.T__9)
            self.state = 117
            self.start_date()
            self.state = 118
            self.end_date()
            self.state = 119
            self.limit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detect_terminalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start_date(self):
            return self.getTypedRuleContext(DetectCommandsParser.Start_dateContext,0)


        def end_date(self):
            return self.getTypedRuleContext(DetectCommandsParser.End_dateContext,0)


        def limit(self):
            return self.getTypedRuleContext(DetectCommandsParser.LimitContext,0)


        def getRuleIndex(self):
            return DetectCommandsParser.RULE_detect_terminal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetect_terminal" ):
                listener.enterDetect_terminal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetect_terminal" ):
                listener.exitDetect_terminal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetect_terminal" ):
                return visitor.visitDetect_terminal(self)
            else:
                return visitor.visitChildren(self)




    def detect_terminal(self):

        localctx = DetectCommandsParser.Detect_terminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_detect_terminal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(DetectCommandsParser.T__10)
            self.state = 122
            self.start_date()
            self.state = 123
            self.end_date()
            self.state = 124
            self.limit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detect_date_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start_date(self):
            return self.getTypedRuleContext(DetectCommandsParser.Start_dateContext,0)


        def end_date(self):
            return self.getTypedRuleContext(DetectCommandsParser.End_dateContext,0)


        def getRuleIndex(self):
            return DetectCommandsParser.RULE_detect_date_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetect_date_range" ):
                listener.enterDetect_date_range(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetect_date_range" ):
                listener.exitDetect_date_range(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetect_date_range" ):
                return visitor.visitDetect_date_range(self)
            else:
                return visitor.visitChildren(self)




    def detect_date_range(self):

        localctx = DetectCommandsParser.Detect_date_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_detect_date_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(DetectCommandsParser.T__11)
            self.state = 127
            self.start_date()
            self.state = 128
            self.end_date()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detect_degree_limitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def degree(self):
            return self.getTypedRuleContext(DetectCommandsParser.DegreeContext,0)


        def limit(self):
            return self.getTypedRuleContext(DetectCommandsParser.LimitContext,0)


        def getRuleIndex(self):
            return DetectCommandsParser.RULE_detect_degree_limit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetect_degree_limit" ):
                listener.enterDetect_degree_limit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetect_degree_limit" ):
                listener.exitDetect_degree_limit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetect_degree_limit" ):
                return visitor.visitDetect_degree_limit(self)
            else:
                return visitor.visitChildren(self)




    def detect_degree_limit(self):

        localctx = DetectCommandsParser.Detect_degree_limitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_detect_degree_limit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(DetectCommandsParser.T__12)
            self.state = 131
            self.degree()
            self.state = 132
            self.limit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Detect_structured_transactionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start_date(self):
            return self.getTypedRuleContext(DetectCommandsParser.Start_dateContext,0)


        def end_date(self):
            return self.getTypedRuleContext(DetectCommandsParser.End_dateContext,0)


        def limit(self):
            return self.getTypedRuleContext(DetectCommandsParser.LimitContext,0)


        def getRuleIndex(self):
            return DetectCommandsParser.RULE_detect_structured_transactions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetect_structured_transactions" ):
                listener.enterDetect_structured_transactions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetect_structured_transactions" ):
                listener.exitDetect_structured_transactions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetect_structured_transactions" ):
                return visitor.visitDetect_structured_transactions(self)
            else:
                return visitor.visitChildren(self)




    def detect_structured_transactions(self):

        localctx = DetectCommandsParser.Detect_structured_transactionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_detect_structured_transactions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(DetectCommandsParser.T__13)
            self.state = 135
            self.start_date()
            self.state = 136
            self.end_date()
            self.state = 137
            self.limit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_dateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(DetectCommandsParser.DATE, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_start_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_date" ):
                listener.enterStart_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_date" ):
                listener.exitStart_date(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_date" ):
                return visitor.visitStart_date(self)
            else:
                return visitor.visitChildren(self)




    def start_date(self):

        localctx = DetectCommandsParser.Start_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_start_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(DetectCommandsParser.T__14)
            self.state = 140
            self.match(DetectCommandsParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class End_dateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(DetectCommandsParser.DATE, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_end_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd_date" ):
                listener.enterEnd_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd_date" ):
                listener.exitEnd_date(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd_date" ):
                return visitor.visitEnd_date(self)
            else:
                return visitor.visitChildren(self)




    def end_date(self):

        localctx = DetectCommandsParser.End_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_end_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(DetectCommandsParser.T__15)
            self.state = 143
            self.match(DetectCommandsParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(DetectCommandsParser.NUMBER, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_limit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit" ):
                listener.enterLimit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit" ):
                listener.exitLimit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimit" ):
                return visitor.visitLimit(self)
            else:
                return visitor.visitChildren(self)




    def limit(self):

        localctx = DetectCommandsParser.LimitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_limit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(DetectCommandsParser.T__16)
            self.state = 146
            self.match(DetectCommandsParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DegreeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(DetectCommandsParser.NUMBER, 0)

        def getRuleIndex(self):
            return DetectCommandsParser.RULE_degree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDegree" ):
                listener.enterDegree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDegree" ):
                listener.exitDegree(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDegree" ):
                return visitor.visitDegree(self)
            else:
                return visitor.visitChildren(self)




    def degree(self):

        localctx = DetectCommandsParser.DegreeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_degree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(DetectCommandsParser.T__17)
            self.state = 149
            self.match(DetectCommandsParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





