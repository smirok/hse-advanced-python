import ast
import networkx as nx

node_colors = {
    ast.Module: '#e14221',
    ast.FunctionDef: '#bdb86b',
    ast.arguments: '#fa28fd',
    ast.arg: '#e2258e',
    ast.Name: '#8d0775',
    ast.Load: '#445d6a',
    ast.Assign: '#6c7b07',
    ast.Store: '#6d98cb',
    ast.List: '#7e6f54',
    ast.Constant: '#1f4978',
    ast.While: '#879c1d',
    ast.Compare: '#bcb74c',
    ast.Call: '#76a916',
    ast.Lt: '#4f9ae8',
    ast.Expr: '#0e889d',
    ast.Attribute: '#5277d9',
    ast.BinOp: '#5009a2',
    ast.Subscript: '#20c79a',
    ast.Index: '#9000f7',
    ast.Add: '#77340b',
    ast.UnaryOp: '#2b57c7',
    ast.USub: '#ce93f8',
    ast.Return: '#5cc033'
}


def get_color(class_node: ast.AST.__class__) -> str:
    return node_colors[class_node.__class__]


def get_label(node: ast.AST) -> str:
    if isinstance(node, ast.FunctionDef):
        return f'Function definition {node.name}'
    if isinstance(node, ast.Name):
        return f'Name {node.id}'
    if isinstance(node, ast.Constant):
        return f'Constant {node.value}'
    if isinstance(node, ast.arg):
        return f'Argument {node.arg}'
    if isinstance(node, ast.Attribute):
        return f'Attribute {node.attr}'
    return node.__class__.__name__


class AstVisitor:
    def __init__(self):
        self.__graph = nx.DiGraph()

    def get_graph(self) -> nx.DiGraph:
        return self.__graph

    def traverse(self, node: ast.AST) -> int:
        node_pos = len(self.__graph) + 1

        self.__graph.add_node(
            node_pos,
            label=get_label(node),
            color=get_color(node),
            style='filled'
        )

        for name, value in ast.iter_fields(node):
            if isinstance(value, ast.AST):
                self.__graph.add_edge(node_pos, self.traverse(value))
            elif isinstance(value, list):
                for child in value:
                    self.__graph.add_edge(node_pos, self.traverse(child))

        return node_pos
