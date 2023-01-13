from Algo import Greedy, GreedyOpti
temoin = Greedy(15)
graph = GreedyOpti(8, temoin.get_vertices())
path = (temoin.compute())
path2 = (graph.compute())