import ast

from instructions_to_graph.src.Infos import Infos
from instructions_to_graph.src.Wrappers.WrapperAssign import WrapperAssign
from instructions_to_graph.src.Wrappers.WrapperAugAssign import WrapperAugAssign
from instructions_to_graph.src.Wrappers.WrapperInstr import WrapperInstr
from instructions_to_graph.src.Wrappers.WrapperReturn import WrapperReturn


class Parser:
    def __init__(self,infos:Infos):
        self.infos = infos
        self.source_func = self.infos.parsed.body[3].body[1]
        for arg in self.source_func.args.args[1:]:
            name = arg.arg+"|0"
            if arg.arg not in WrapperInstr.dico_node:
                WrapperInstr.dico_node[arg.arg] = 0

            self.infos.graph.node(name,label=arg.arg)
            WrapperInstr.dico_node[arg.arg] += 1
    def parse_instructions(self):
        fun_list = self.source_func.body
        dico_parser = {
            ast.Assign:WrapperAssign,
            ast.Return:WrapperReturn,
            ast.AugAssign:WrapperAugAssign
        }
        for instr in fun_list:
            t = type(instr)
            if t in dico_parser:
                dico_parser[t](instr,self.infos)
        return
        