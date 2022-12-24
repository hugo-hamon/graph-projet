from Algo import Greedy, GreedyOpti
temoin = Greedy(4)
graph = GreedyOpti(8, temoin.get_vertices())
path = (temoin.compute())
path2 = (graph.compute())
temoin.draw_path(path)
print(temoin.compute_distance_by_path(path))
print(temoin.compute_distance_by_path(path2))