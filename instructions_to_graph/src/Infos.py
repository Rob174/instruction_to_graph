import ast


class Infos:
    def __init__(self,graph,code=None,parsed=None):
        self.code = code
        self.parsed = parsed
        self.graph = graph
    def open_file(self,module,module_name,path:str="./test_file.py"):
        with open(path) as fp:
            self.code = fp.read()
            self.parsed = ast.parse(self.code)
            self.module = module
            self.module_name = module_name
        