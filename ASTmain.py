from antlr4 import *

from default_codes.ast_to_networkx_graph import transform_ast_to_networkx, show_ast
from CustomASTListener import ASTListener
from gen.DetectCommandsLexer import DetectCommandsLexer
from gen.DetectCommandsParser import DetectCommandsParser
import argparse
from default_codes.post_order_ast_traverser import PostOrderASTTraverser
from ILGenerator import ILMapper
import os
def main(args):
    # Step 1: Load input source into stream
    out_path = input("enter output path for generated codes :")
    if not os.path.exists(out_path):
        os.makedirs(out_path)
        
    stream = FileStream(args.file, encoding='utf8')
    print('Input language_apps:\n{0}'.format(stream))
    print('Result:')

    # Step 2: Create an instance of AssignmentStLexer
    lexer = DetectCommandsLexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = DetectCommandsParser(token_stream)
    # Step 5: Create parse tree
    parse_tree = parser.start()
    # Step 6: Create an instance of AssignmentStListener
    ast_generator = ASTListener(parser.ruleNames)

    # Step 7(a): Walk parse tree with a customized listener (Automatically)
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_generator)
    normal_ast = ast_generator.ast
    show_ast(normal_ast.root)
    post_order_ast_traverser = PostOrderASTTraverser()
    post_order_ast_traverser.node_attributes = ['label']
    traversal_dict = post_order_ast_traverser.traverse_ast(normal_ast.root)
    traversal = [item['label'] for item in traversal_dict]
    # //////////////////////////////////////////////////
    print(traversal)
    # post_order_ast_traverser = PostOrderASTTraverser()
	# post_order_ast_traverser.node_attributes = ['label', 'text', 'number']
	# traversal = post_order_ast_traverser.traverse_ast(ast.root)
    code_generator = ILMapper(out_path)
    generated_code = code_generator.generate_intermediate_language(traversal)
    with open(args.output, 'w') as output_file:
        output_file.write(generated_code)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument( '-n', '--file',help='Input source', default=r'input.txt')
    argparser.add_argument('-o', '--output', help='Output path', default=r'test_output.py')
    args = argparser.parse_args()
    main(args)
