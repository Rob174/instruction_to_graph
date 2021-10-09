import ast

from instructions_to_graph.src.Wrappers.WrapperBinOp import WrapperBinOp
from instructions_to_graph.src.Wrappers.WrapperCall import WrapperCall
from instructions_to_graph.src.Wrappers.WrapperInstr import WrapperInstr


class WrapperAssign(WrapperInstr):
    def __init__(self,instr,infos):
        super(WrapperAssign, self).__init__(instr,infos)
    def parse(self):
        super(WrapperAssign, self).parse()
        dico_parser = {
            ast.Call:WrapperCall,
            ast.BinOp:WrapperBinOp
        }
        self.dest_var = self.instr.targets[0].id
        if type(self.instr.value) in dico_parser:
            wrapper = dico_parser[type(self.instr.value)](self.instr.value,self.infos)
            name_id = self.dest_var+"|"
            if self.dest_var in WrapperInstr.dico_node:
                name_id += str(WrapperInstr.dico_node[self.dest_var])
            else:
                name_id += "0"
                WrapperInstr.dico_node[self.dest_var] = 0
            for argname,arg in wrapper.arguments:
                for k in WrapperInstr.dico_node.keys():
                    if k in arg:
                        src_node = k+"|"+str(WrapperInstr.dico_node[k]-1)
                        self.infos.graph.edge(src_node,name_id)
            WrapperInstr.dico_node[self.dest_var] += 1
            self.infos.graph.node(name_id,label=wrapper.text,shape="record")