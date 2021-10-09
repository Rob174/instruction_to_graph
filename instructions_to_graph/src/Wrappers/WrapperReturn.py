from instructions_to_graph.src.Wrappers.WrapperInstr import WrapperInstr


class WrapperReturn(WrapperInstr):
    def __init__(self,instr,infos):
        super(WrapperReturn, self).__init__(instr,infos)
    def parse(self):
        super(WrapperReturn, self).parse()
        returned_elements = [x.id for x in self.instr.value.elts]
        self.infos.graph.node("out")
        for r in returned_elements:
            src = r+"|"+str(WrapperInstr.dico_node[r]-1)
            self.infos.graph.edge(src,"out")