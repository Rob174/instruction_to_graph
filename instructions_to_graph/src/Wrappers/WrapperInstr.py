class WrapperInstr:
    liste_instr = []
    dico_node = {}
    id = 0
    def __init__(self,instr,infos:Infos):
        self.instr = instr
        self.infos: Infos = infos
        WrapperInstr.id += 1
        self.id = WrapperInstr.id
        self.parse()
        WrapperInstr.liste_instr.append(self)
    def parse_with_poss(self,dico_parser_poss,data_loc,*args):
        for v in data_loc:
            if type(v) in dico_parser_poss:
                dico_parser_poss[type(v)](v,self.infos,*args)
            else:
                pass
    @abstractmethod
    def parse(self):
        pass