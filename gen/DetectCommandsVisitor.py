# Generated from C:/Term 6/Compiler design project/FraudDetection/grammar/DetectCommands.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DetectCommandsParser import DetectCommandsParser
else:
    from DetectCommandsParser import DetectCommandsParser

# This class defines a complete generic visitor for a parse tree produced by DetectCommandsParser.

class DetectCommandsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DetectCommandsParser#start.
    def visitStart(self, ctx:DetectCommandsParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#setting.
    def visitSetting(self, ctx:DetectCommandsParser.SettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#url.
    def visitUrl(self, ctx:DetectCommandsParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#username.
    def visitUsername(self, ctx:DetectCommandsParser.UsernameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#pass.
    def visitPass(self, ctx:DetectCommandsParser.PassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#dbname.
    def visitDbname(self, ctx:DetectCommandsParser.DbnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#load_terminal.
    def visitLoad_terminal(self, ctx:DetectCommandsParser.Load_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#load_customer.
    def visitLoad_customer(self, ctx:DetectCommandsParser.Load_customerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#load_transaction.
    def visitLoad_transaction(self, ctx:DetectCommandsParser.Load_transactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#path.
    def visitPath(self, ctx:DetectCommandsParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#commands.
    def visitCommands(self, ctx:DetectCommandsParser.CommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#command.
    def visitCommand(self, ctx:DetectCommandsParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#detect_customer.
    def visitDetect_customer(self, ctx:DetectCommandsParser.Detect_customerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#detect_terminal.
    def visitDetect_terminal(self, ctx:DetectCommandsParser.Detect_terminalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#detect_date_range.
    def visitDetect_date_range(self, ctx:DetectCommandsParser.Detect_date_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#detect_degree_limit.
    def visitDetect_degree_limit(self, ctx:DetectCommandsParser.Detect_degree_limitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#start_date.
    def visitStart_date(self, ctx:DetectCommandsParser.Start_dateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#end_date.
    def visitEnd_date(self, ctx:DetectCommandsParser.End_dateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#limit.
    def visitLimit(self, ctx:DetectCommandsParser.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DetectCommandsParser#degree.
    def visitDegree(self, ctx:DetectCommandsParser.DegreeContext):
        return self.visitChildren(ctx)



del DetectCommandsParser