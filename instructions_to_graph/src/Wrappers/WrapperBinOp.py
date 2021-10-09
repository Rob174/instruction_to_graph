import ast

from instructions_to_graph.src.Wrappers.WrapperInstr import WrapperInstr


class WrapperBinOp(WrapperInstr):
    def __init__(self,instr,infos):
        super(WrapperBinOp, self).__init__(instr,infos)
    def parse(self):
        self.text = ast.get_source_segment(self.infos.code,self.instr)
        self.arguments = [(k,k) for k in WrapperInstr.dico_node.keys() if k in self.text]
        