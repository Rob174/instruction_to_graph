import ast

from instructions_to_graph.src.Infos import Infos
from instructions_to_graph.src.Wrappers.WrapperAssign import WrapperAssign


def WrapperAugAssign(instr,infos):
    code = ast.get_source_segment(infos.code,instr)
    dico_parse = {
        ast.Mult:"*",
        ast.Div:"/",
        ast.Add:"+",
        ast.Sub:"-"
    }
    symbol = dico_parse[type(instr.op)]
    code_splited = code.split(f"{symbol}=")
    code_splited[1] = code_splited[0] + symbol + code_splited[1]
    new_code = "=".join(code_splited)
    parsed_code = ast.parse(new_code)
    instruct = parsed_code.body[0]
    infos = Infos(infos.graph,code=new_code,parsed=parsed_code)
    return WrapperAssign(instruct,infos)
        