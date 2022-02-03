import ast
import inspect

import networkx as nx
from ast_visitor import AstVisitor
from fibonacci import fibonacci


def draw_ast(function, output_directory, output_filename):
    ast_visitor = AstVisitor()
    ast_visitor.traverse(ast.parse(inspect.getsource(function)))
    nx.drawing.nx_pydot.to_pydot(ast_visitor.get_graph()).write(f'{output_directory}/{output_filename}', format='png')


if __name__ == "__main__":
    draw_ast(fibonacci, 'artifacts', 'ast.png')
