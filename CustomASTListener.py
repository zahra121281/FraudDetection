from default_codes.ast import AST
from default_codes.make_ast_subtree import make_ast_subtree
from gen.DetectCommandsListener import DetectCommandsListener
from gen.DetectCommandsParser import DetectCommandsParser

class ASTListener(DetectCommandsListener):
    def __init__(self, rule_names):
        self.overridden_rules = ['start', 'command', 'setting', 'url', 'username', 'pass', 'load_terminal', 'load_customer' , 'load_transaction',
                                 'detect_customer', 'detect_terminal', 'detect_date_range', 'detect_degree_limit',
                                 'start_date', 'end_date', 'limit', 'degree']
        self.binary_operator_list = []
        self.rule_names = rule_names
        self.ast = AST()
        self.current_setting = None
        self.current_command = None
        self.current_detect_customer = None
        self.current_detect_terminal = None
        self.current_detect_date_range = None
        self.current_detect_degree_limit = None
        self.current_Load = None

    def exitStart(self, ctx: DetectCommandsParser.StartContext):
        start_node = make_ast_subtree(self.ast, ctx, 'Start', True)
        if self.current_setting:
            self.ast.add_child(start_node, self.current_setting)
        if self.current_command:
            self.ast.add_child(start_node, self.current_command)

    def exitCommand(self, ctx: DetectCommandsParser.CommandContext):
        self.current_command = make_ast_subtree(self.ast, ctx, 'Command', True)

    def exitSetting(self, ctx: DetectCommandsParser.SettingContext):
        self.current_setting = make_ast_subtree(self.ast, ctx, 'Setting', True)

    def exitUrl(self, ctx: DetectCommandsParser.UrlContext):
        url_node = make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)
        if self.current_setting:
            self.ast.add_child(self.current_setting, url_node)

    def exitUsername(self, ctx: DetectCommandsParser.UsernameContext):
        username_node = make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)
        if self.current_setting:
            self.ast.add_child(self.current_setting, username_node)

    def exitPass(self, ctx: DetectCommandsParser.PassContext):
        pass_node = make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)
        if self.current_setting:
            self.ast.add_child(self.current_setting, pass_node)

    def exitLoad_terminal(self, ctx:DetectCommandsParser.Load_terminalContext):
        load_data_node = make_ast_subtree(self.ast, ctx, 'Load_terminal', True)
        if self.current_setting:
            self.ast.add_child(self.current_setting, load_data_node)

    def exitLoad_customer(self, ctx:DetectCommandsParser.Load_customerContext):
        load_data_node = make_ast_subtree(self.ast, ctx, 'Load_customer', True)
        if self.current_setting:
            self.ast.add_child(self.current_setting, load_data_node)

    def exitLoad_transaction(self, ctx:DetectCommandsParser.Load_transactionContext):
        load_data_node = make_ast_subtree(self.ast, ctx, 'Load_transaction', True)
        if self.current_setting:
            self.ast.add_child(self.current_setting, load_data_node)

    def exitDetect_customer(self, ctx: DetectCommandsParser.Detect_customerContext):
        self.current_detect_customer = make_ast_subtree(self.ast, ctx, 'Detect_customer', True)
        if self.current_command:
            self.ast.add_child(self.current_command, self.current_detect_customer)

    def exitDetect_terminal(self, ctx: DetectCommandsParser.Detect_terminalContext):
        self.current_detect_terminal = make_ast_subtree(self.ast, ctx, 'Detect_terminal', True)
        if self.current_command:
            self.ast.add_child(self.current_command, self.current_detect_terminal)

    def exitDetect_date_range(self, ctx: DetectCommandsParser.Detect_date_rangeContext):
        self.current_detect_date_range = make_ast_subtree(self.ast, ctx, 'Detect_date_range', True)
        if self.current_command:
            self.ast.add_child(self.current_command, self.current_detect_date_range)

    def exitDetect_degree_limit(self, ctx: DetectCommandsParser.Detect_degree_limitContext):
        self.current_detect_degree_limit = make_ast_subtree(self.ast, ctx, 'Detect_degree_limit', True)
        if self.current_command:
            self.ast.add_child(self.current_command, self.current_detect_degree_limit)

    def exitStart_date(self, ctx: DetectCommandsParser.Start_dateContext):
        start_date_node = make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)
        if self.current_detect_customer:
            self.ast.add_child(self.current_detect_customer, start_date_node)
        elif self.current_detect_terminal:
            self.ast.add_child(self.current_detect_terminal, start_date_node)
        elif self.current_detect_date_range:
            self.ast.add_child(self.current_detect_date_range, start_date_node)

    def exitEnd_date(self, ctx: DetectCommandsParser.End_dateContext):
        end_date_node = make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)
        if self.current_detect_customer:
            self.ast.add_child(self.current_detect_customer, end_date_node)
        elif self.current_detect_terminal:
            self.ast.add_child(self.current_detect_terminal, end_date_node)
        elif self.current_detect_date_range:
            self.ast.add_child(self.current_detect_date_range, end_date_node)

    def exitLimit(self, ctx: DetectCommandsParser.LimitContext):
        limit_node = make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)
        if self.current_detect_customer:
            self.ast.add_child(self.current_detect_customer, limit_node)
        elif self.current_detect_terminal:
            self.ast.add_child(self.current_detect_terminal, limit_node)
        elif self.current_detect_degree_limit:
            self.ast.add_child(self.current_detect_degree_limit, limit_node)

    def exitDegree(self, ctx: DetectCommandsParser.DegreeContext):
        degree_node = make_ast_subtree(self.ast, ctx, ctx.getChild(1).getText(), True)
        if self.current_detect_degree_limit:
            self.ast.add_child(self.current_detect_degree_limit, degree_node)


    def exitPath(self, ctx:DetectCommandsParser.PathContext):
        path_node =make_ast_subtree(self.ast, ctx, ctx.getChild(0).getText(), False)
        if self.current_Load:
            self.ast.add_child(self.current_Load, path_node)