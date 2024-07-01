# Generated from E:/Sem6/Compiler/New folder (2)/FraudDetection/grammar/DetectCommands.g4 by ANTLR 4.13.1
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
        4,1,20,110,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,
        43,8,1,10,1,12,1,46,9,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,
        1,5,1,5,5,5,60,8,5,10,5,12,5,63,9,5,1,6,1,6,1,6,1,6,1,6,3,6,70,8,
        6,1,6,5,6,73,8,6,10,6,12,6,76,9,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,
        1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,0,0,16,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,0,99,0,32,1,0,0,0,2,37,
        1,0,0,0,4,47,1,0,0,0,6,50,1,0,0,0,8,53,1,0,0,0,10,56,1,0,0,0,12,
        64,1,0,0,0,14,77,1,0,0,0,16,82,1,0,0,0,18,87,1,0,0,0,20,91,1,0,0,
        0,22,95,1,0,0,0,24,98,1,0,0,0,26,101,1,0,0,0,28,104,1,0,0,0,30,107,
        1,0,0,0,32,33,3,2,1,0,33,34,3,10,5,0,34,35,3,12,6,0,35,36,5,0,0,
        1,36,1,1,0,0,0,37,38,5,1,0,0,38,39,3,4,2,0,39,40,3,6,3,0,40,44,3,
        8,4,0,41,43,5,20,0,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,
        45,1,0,0,0,45,3,1,0,0,0,46,44,1,0,0,0,47,48,5,2,0,0,48,49,5,15,0,
        0,49,5,1,0,0,0,50,51,5,3,0,0,51,52,5,15,0,0,52,7,1,0,0,0,53,54,5,
        4,0,0,54,55,5,18,0,0,55,9,1,0,0,0,56,57,5,5,0,0,57,61,3,30,15,0,
        58,60,5,20,0,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,
        0,0,0,62,11,1,0,0,0,63,61,1,0,0,0,64,69,5,6,0,0,65,70,3,14,7,0,66,
        70,3,16,8,0,67,70,3,18,9,0,68,70,3,20,10,0,69,65,1,0,0,0,69,66,1,
        0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,74,1,0,0,0,71,73,5,20,0,0,72,
        71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,13,1,0,0,
        0,76,74,1,0,0,0,77,78,5,7,0,0,78,79,3,22,11,0,79,80,3,24,12,0,80,
        81,3,26,13,0,81,15,1,0,0,0,82,83,5,8,0,0,83,84,3,22,11,0,84,85,3,
        24,12,0,85,86,3,26,13,0,86,17,1,0,0,0,87,88,5,9,0,0,88,89,3,22,11,
        0,89,90,3,24,12,0,90,19,1,0,0,0,91,92,5,10,0,0,92,93,3,28,14,0,93,
        94,3,26,13,0,94,21,1,0,0,0,95,96,5,11,0,0,96,97,5,17,0,0,97,23,1,
        0,0,0,98,99,5,12,0,0,99,100,5,17,0,0,100,25,1,0,0,0,101,102,5,13,
        0,0,102,103,5,16,0,0,103,27,1,0,0,0,104,105,5,14,0,0,105,106,5,16,
        0,0,106,29,1,0,0,0,107,108,5,15,0,0,108,31,1,0,0,0,4,44,61,69,74
    ]

class DetectCommandsParser ( Parser ):

    grammarFileName = "DetectCommands.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Setting'", "'url='", "'username='", 
                     "'pass='", "'LoadData'", "'Detect'", "'customer'", 
                     "'terminal'", "'name3'", "'name4'", "'startdate='", 
                     "'enddate='", "'limit='", "'degree='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "NUMBER", 
                      "DATE", "Pass", "WS", "NewLine" ]

    RULE_start = 0
    RULE_setting = 1
    RULE_url = 2
    RULE_username = 3
    RULE_pass = 4
    RULE_load_data = 5
    RULE_command = 6
    RULE_detect_customer = 7
    RULE_detect_terminal = 8
    RULE_detect_date_range = 9
    RULE_detect_degree_limit = 10
    RULE_start_date = 11
    RULE_end_date = 12
    RULE_limit = 13
    RULE_degree = 14
    RULE_path = 15

    ruleNames =  [ "start", "setting", "url", "username", "pass", "load_data", 
                   "command", "detect_customer", "detect_terminal", "detect_date_range", 
                   "detect_degree_limit", "start_date", "end_date", "limit", 
                   "degree", "path" ]

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
    STRING=15
    NUMBER=16
    DATE=17
    Pass=18
    WS=19
    NewLine=20

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


        def load_data(self):
            return self.getTypedRuleContext(DetectCommandsParser.Load_dataContext,0)


        def command(self):
            return self.getTypedRuleContext(DetectCommandsParser.CommandContext,0)


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
            self.state = 32
            self.setting()
            self.state = 33
            self.load_data()
            self.state = 34
            self.command()
            self.state = 35
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
            self.state = 37
            self.match(DetectCommandsParser.T__0)
            self.state = 38
            self.url()
            self.state = 39
            self.username()
            self.state = 40
            self.pass_()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 41
                self.match(DetectCommandsParser.NewLine)
                self.state = 46
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
            self.state = 47
            self.match(DetectCommandsParser.T__1)
            self.state = 48
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
            self.state = 50
            self.match(DetectCommandsParser.T__2)
            self.state = 51
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
            self.state = 53
            self.match(DetectCommandsParser.T__3)
            self.state = 54
            self.match(DetectCommandsParser.Pass)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Load_dataContext(ParserRuleContext):
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
            return DetectCommandsParser.RULE_load_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad_data" ):
                listener.enterLoad_data(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad_data" ):
                listener.exitLoad_data(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoad_data" ):
                return visitor.visitLoad_data(self)
            else:
                return visitor.visitChildren(self)




    def load_data(self):

        localctx = DetectCommandsParser.Load_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_load_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(DetectCommandsParser.T__4)
            self.state = 57
            self.path()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 58
                self.match(DetectCommandsParser.NewLine)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 12, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(DetectCommandsParser.T__5)
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 65
                self.detect_customer()
                pass
            elif token in [8]:
                self.state = 66
                self.detect_terminal()
                pass
            elif token in [9]:
                self.state = 67
                self.detect_date_range()
                pass
            elif token in [10]:
                self.state = 68
                self.detect_degree_limit()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 71
                self.match(DetectCommandsParser.NewLine)
                self.state = 76
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
        self.enterRule(localctx, 14, self.RULE_detect_customer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(DetectCommandsParser.T__6)
            self.state = 78
            self.start_date()
            self.state = 79
            self.end_date()
            self.state = 80
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
        self.enterRule(localctx, 16, self.RULE_detect_terminal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(DetectCommandsParser.T__7)
            self.state = 83
            self.start_date()
            self.state = 84
            self.end_date()
            self.state = 85
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
        self.enterRule(localctx, 18, self.RULE_detect_date_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(DetectCommandsParser.T__8)
            self.state = 88
            self.start_date()
            self.state = 89
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
        self.enterRule(localctx, 20, self.RULE_detect_degree_limit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(DetectCommandsParser.T__9)
            self.state = 92
            self.degree()
            self.state = 93
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
        self.enterRule(localctx, 22, self.RULE_start_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(DetectCommandsParser.T__10)
            self.state = 96
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
        self.enterRule(localctx, 24, self.RULE_end_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(DetectCommandsParser.T__11)
            self.state = 99
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
        self.enterRule(localctx, 26, self.RULE_limit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(DetectCommandsParser.T__12)
            self.state = 102
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
        self.enterRule(localctx, 28, self.RULE_degree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(DetectCommandsParser.T__13)
            self.state = 105
            self.match(DetectCommandsParser.NUMBER)
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
        self.enterRule(localctx, 30, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(DetectCommandsParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





