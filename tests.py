from Algo import Greedy, GreedyOpti, BranchAndBound

temoin = Greedy(5)
graph = GreedyOpti(5, temoin.get_vertices())

path = (temoin.compute())
path2 = (graph.compute())