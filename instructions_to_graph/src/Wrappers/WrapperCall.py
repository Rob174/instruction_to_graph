import ast
from inspect import signature

from instructions_to_graph.src.Wrappers.WrapperInstr import WrapperInstr


class WrapperCall(WrapperInstr):
    def __init__(self,instr,infos):
        super(WrapperCall, self).__init__(instr,infos)
        # print(f"{signature(eval(infos.module_name+instr.func.attr))=}")
        if ast.get_source_segment(infos.code,instr.func).split(".")[0] == "self":
            class_obj = [o for o in infos.parsed.body if isinstance(o,ast.ClassDef)][0]
            fun = [o for o in class_obj.body if instr.func.attr in o.name][0]
            arguments = list(signature(eval(f"self.infos.module.{class_obj.name}.{fun.name}")).parameters.keys())[1:]
            # print(arguments)
        else:
            arguments = signature(eval(f"self.infos.module.{ast.get_source_segment(infos.code, instr.func)}")).parameters.keys()
            # print(arguments)


        self.arg = [(n,ast.get_source_segment(infos.code,arg)) for n,arg in zip(arguments,instr.args)]
        self.kwarg = [(kw.arg,ast.get_source_segment(infos.code,kw.value)) for kw in instr.keywords]
        self.name = instr.func.attr
        self.arguments = [*self.arg,*self.kwarg]
        arguments = ",".join(map(lambda x:x[0]+'='+x[1],self.arguments))
        name = f"{self.name}({arguments})"
        self.text = name
        