from graph import *
graph = Greedy(4)
graph.plot()
graph.compute()
g = Greedy_opti(8, graph.get_vertices())
g.plot()
g.compute()