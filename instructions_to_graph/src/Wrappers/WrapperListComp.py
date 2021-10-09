import ast

from instructions_to_graph.src.Wrappers.WrapperInstr import WrapperInstr


class WrapperListComp(WrapperInstr):
    def __init__(self,instr,infos):
        super(WrapperListComp, self).__init__(instr,infos)
    def parse(self):
        self.text = ast.get_source_segment(self.infos.code)