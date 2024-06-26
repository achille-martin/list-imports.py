__all__ = ['get', 'parse']


import ast


def get(path):
    """return a list of python file imports"""
    code = open(path).read()
    return parse(code)


def parse(code):
    """return a list of python code imports"""
    imports = set()
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for subnode in node.names:
                    imports.add(subnode.name)
            if isinstance(node, ast.ImportFrom):
                imports.add(('.' * node.level) + str(node.module))
    except Exception as e:
        print("EXCEPTION CAUGHT: {}".format(str(e)))
    return list(imports)
