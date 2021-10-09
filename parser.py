import ast
from inspect import signature
from graphviz import Digraph
from instructions_to_graph.src.Infos import Infos
from instructions_to_graph.src.Parser import Parser


if __name__ == '__main__':
    import test_file
    graph = Digraph(format="svg")
    infos = Infos(graph)
    infos.open_file(test_file,"test_file")
    parser = Parser(infos)
    parser.parse_instructions()
    infos.graph.render("./graph")
    s=0