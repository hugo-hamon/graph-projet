from Algo import Greedy, GreedyOpti
temoin = Greedy(20)
graph = GreedyOpti(8, temoin.get_vertices())
path = (temoin.compute())
path2 = (graph.compute())
temoin.draw_path(path)
graph.draw_path(path2)
print(temoin.compute_distance_by_path(path))
print(temoin.compute_distance_by_path(path2))
