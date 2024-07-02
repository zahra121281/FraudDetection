#version 3
from default_codes.ast import AST
from default_codes.make_ast_subtree import make_ast_subtree
from gen.DetectCommandsListener import DetectCommandsListener
from gen.DetectCommandsParser import DetectCommandsParser

class ASTListener(DetectCommandsListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['start', 'command', 'setting', 'url', 'username', 'pass', 'dbname',
                                 'load_terminal', 'load_customer' , 'load_transaction',
                                 'detect_customer', 'detect_terminal', 'detect_date_range', 'detect_degree_limit',
                                 'Detect_structured_transactions',
                                 'start_date', 'end_date', 'limit', 'degree']
        self.rule_names = rule_names
        self.ast = AST()

    def exitStart(self, ctx: DetectCommandsParser.StartContext):
        make_ast_subtree(self.ast, ctx, 'Start', True)

    def exitCommand(self, ctx: DetectCommandsParser.CommandContext):
        if ctx.getChildCount() <=1 or (ctx.getChildCount()==2 and ctx.getChild(1).getText()=='\n'):
            raise ValueError("Command is missing .")
        make_ast_subtree(self.ast, ctx, 'Command', False)

    def exitSetting(self, ctx: DetectCommandsParser.SettingContext):
        if ctx.getChildCount() == 0:
            raise ValueError("Setting is missing .")
        make_ast_subtree(self.ast, ctx, 'Setting', True)

    def exitUrl(self, ctx: DetectCommandsParser.UrlContext):
        if ctx.getChildCount() <= 1 :
            raise ValueError("Url is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

    def exitUsername(self, ctx: DetectCommandsParser.UsernameContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Username is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

    def exitPass(self, ctx: DetectCommandsParser.PassContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Pass is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

    def exitDbname(self, ctx: DetectCommandsParser.DbnameContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Dbname is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

    def exitLoad_terminal(self, ctx: DetectCommandsParser.Load_terminalContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Load_terminal is missing .")
        make_ast_subtree(self.ast, ctx, 'Load_terminal', True)

    def exitLoad_customer(self, ctx: DetectCommandsParser.Load_customerContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Load_customer is missing .")
        make_ast_subtree(self.ast, ctx, 'Load_customer', True)

    def exitLoad_transaction(self, ctx: DetectCommandsParser.Load_transactionContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Load_transaction is missing .")
        make_ast_subtree(self.ast, ctx, 'Load_transaction', True)

    def exitCommands(self, ctx: DetectCommandsParser.CommandsContext):
        if ctx.getChildCount()==0:
            raise ValueError("Commands is missing .")
        make_ast_subtree(self.ast, ctx, 'commands', True)

    def exitDetect_customer(self, ctx: DetectCommandsParser.Detect_customerContext):

        make_ast_subtree(self.ast, ctx, 'Detect_customer', True)

    def exitDetect_terminal(self, ctx: DetectCommandsParser.Detect_terminalContext):

        make_ast_subtree(self.ast, ctx, 'Detect_terminal', True)

    def exitDetect_date_range(self, ctx: DetectCommandsParser.Detect_date_rangeContext):
        make_ast_subtree(self.ast, ctx, 'Detect_date_range', True)

    def exitDetect_degree_limit(self, ctx: DetectCommandsParser.Detect_degree_limitContext):
        make_ast_subtree(self.ast, ctx, 'Detect_degree_limit', True)

    def exitDetect_structured_transactions(self, ctx: DetectCommandsParser.Detect_structured_transactionsContext):
        make_ast_subtree(self.ast, ctx, 'Detect_structured_transactions', True)

    def exitStart_date(self, ctx: DetectCommandsParser.Start_dateContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Start_date node is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

    def exitEnd_date(self, ctx: DetectCommandsParser.End_dateContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("End_date node is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

    def exitLimit(self, ctx: DetectCommandsParser.LimitContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Limit node is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

    def exitDegree(self, ctx: DetectCommandsParser.DegreeContext):
        if ctx.getChildCount() <= 1:
            raise ValueError("Degree is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

    def exitPath(self, ctx: DetectCommandsParser.PathContext):
        if ctx.getChild(0).getText() == '<missing <INVALID>>':
            raise ValueError("Path is missing .")
        make_ast_subtree(self.ast, ctx, ctx.getChild(0).getText(), False)




#version 1 
# from default_codes.ast import AST
# from default_codes.make_ast_subtree import make_ast_subtree
# from gen.DetectCommandsListener import DetectCommandsListener
# from gen.DetectCommandsParser import DetectCommandsParser

# class ASTListener(DetectCommandsListener):
#     def __init__(self, rule_names):
#         self.overridden_rules = ['start', 'command', 'setting', 'url', 'username', 'pass', 'dbname',
#                                  'load_terminal', 'load_customer' , 'load_transaction',
#                                  'detect_customer', 'detect_terminal', 'detect_date_range', 'detect_degree_limit',
#                                  'start_date', 'end_date', 'limit', 'degree']
#         self.rule_names = rule_names
#         self.ast = AST()

#     def exitStart(self, ctx: DetectCommandsParser.StartContext):
#         make_ast_subtree(self.ast, ctx, 'Start', True)

#     def exitCommand(self, ctx: DetectCommandsParser.CommandContext):
#         make_ast_subtree(self.ast, ctx, 'Command', False)

#     def exitSetting(self, ctx: DetectCommandsParser.SettingContext):
#         make_ast_subtree(self.ast, ctx, 'Setting', True)

#     def exitUrl(self, ctx: DetectCommandsParser.UrlContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitUsername(self, ctx: DetectCommandsParser.UsernameContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitPass(self, ctx: DetectCommandsParser.PassContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitDbname(self, ctx:DetectCommandsParser.DegreeContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitLoad_terminal(self, ctx:DetectCommandsParser.Load_terminalContext):
#         make_ast_subtree(self.ast, ctx, 'Load_terminal', True)

#     def exitLoad_customer(self, ctx:DetectCommandsParser.Load_customerContext):
#         make_ast_subtree(self.ast, ctx, 'Load_customer', True)

#     def exitLoad_transaction(self, ctx:DetectCommandsParser.Load_transactionContext):
#         make_ast_subtree(self.ast, ctx, 'Load_transaction', True)

#     def exitCommands(self, ctx:DetectCommandsParser.CommandContext):
#         make_ast_subtree(self.ast, ctx, 'commands', True)

#     def exitDetect_customer(self, ctx: DetectCommandsParser.Detect_customerContext):
#         make_ast_subtree(self.ast, ctx, 'Detect_customer', True)

#     def exitDetect_terminal(self, ctx: DetectCommandsParser.Detect_terminalContext):
#         make_ast_subtree(self.ast, ctx, 'Detect_terminal', True)

#     def exitDetect_date_range(self, ctx: DetectCommandsParser.Detect_date_rangeContext):
#         make_ast_subtree(self.ast, ctx, 'Detect_date_range', True)

#     def exitDetect_degree_limit(self, ctx: DetectCommandsParser.Detect_degree_limitContext):
#         make_ast_subtree(self.ast, ctx, 'Detect_degree_limit', True)

#     def exitStart_date(self, ctx: DetectCommandsParser.Start_dateContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitEnd_date(self, ctx: DetectCommandsParser.End_dateContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitLimit(self, ctx: DetectCommandsParser.LimitContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitDegree(self, ctx: DetectCommandsParser.DegreeContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitPath(self, ctx:DetectCommandsParser.PathContext):
#         make_ast_subtree(self.ast, ctx, ctx.getChild(0).getText(), False)


#version 2 
# from default_codes.ast import AST
# from default_codes.make_ast_subtree import make_ast_subtree
# from gen.DetectCommandsListener import DetectCommandsListener
# from gen.DetectCommandsParser import DetectCommandsParser

# class ASTListener(DetectCommandsListener):
#     def __init__(self, rule_names):
#         self.overridden_rules = ['start', 'command', 'setting', 'url', 'username', 'pass', 'dbname',
#                                  'load_terminal', 'load_customer' , 'load_transaction',
#                                  'detect_customer', 'detect_terminal', 'detect_date_range', 'detect_degree_limit',
#                                  'start_date', 'end_date', 'limit', 'degree']
#         self.rule_names = rule_names
#         self.ast = AST()

#     def exitStart(self, ctx: DetectCommandsParser.StartContext):
#         if ctx.getChildCount() > 0:
#             make_ast_subtree(self.ast, ctx, 'Start', True)

#     def exitCommand(self, ctx: DetectCommandsParser.CommandContext):
#         if ctx.getChildCount() > 0:
#             make_ast_subtree(self.ast, ctx, 'Command', False)

#     def exitSetting(self, ctx: DetectCommandsParser.SettingContext):
#         if ctx.getChildCount() > 0:
#             make_ast_subtree(self.ast, ctx, 'Setting', True)

#     def exitUrl(self, ctx: DetectCommandsParser.UrlContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitUsername(self, ctx: DetectCommandsParser.UsernameContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitPass(self, ctx: DetectCommandsParser.PassContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitDbname(self, ctx: DetectCommandsParser.DbnameContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitLoad_terminal(self, ctx: DetectCommandsParser.Load_terminalContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, 'Load_terminal', True)

#     def exitLoad_customer(self, ctx: DetectCommandsParser.Load_customerContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, 'Load_customer', True)

#     def exitLoad_transaction(self, ctx: DetectCommandsParser.Load_transactionContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, 'Load_transaction', True)

#     def exitCommands(self, ctx: DetectCommandsParser.CommandsContext):
#         if ctx.getChildCount() > 0:
#             make_ast_subtree(self.ast, ctx, 'commands', True)

#     def exitDetect_customer(self, ctx: DetectCommandsParser.Detect_customerContext):
#         if ctx.getChildCount() > 3:
#             make_ast_subtree(self.ast, ctx, 'Detect_customer', True)

#     def exitDetect_terminal(self, ctx: DetectCommandsParser.Detect_terminalContext):
#         if ctx.getChildCount() > 3:
#             make_ast_subtree(self.ast, ctx, 'Detect_terminal', True)

#     def exitDetect_date_range(self, ctx: DetectCommandsParser.Detect_date_rangeContext):
#         if ctx.getChildCount() > 2:
#             make_ast_subtree(self.ast, ctx, 'Detect_date_range', True)

#     def exitDetect_degree_limit(self, ctx: DetectCommandsParser.Detect_degree_limitContext):
#         if ctx.getChildCount() > 2:
#             make_ast_subtree(self.ast, ctx, 'Detect_degree_limit', True)

#     def exitStart_date(self, ctx: DetectCommandsParser.Start_dateContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitEnd_date(self, ctx: DetectCommandsParser.End_dateContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitLimit(self, ctx: DetectCommandsParser.LimitContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitDegree(self, ctx: DetectCommandsParser.DegreeContext):
#         if ctx.getChildCount() > 1:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)

#     def exitPath(self, ctx: DetectCommandsParser.PathContext):
#         if ctx.getChildCount() > 0:
#             make_ast_subtree(self.ast, ctx, ctx.getChild(0).getText(), False)


