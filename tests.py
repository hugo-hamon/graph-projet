from graph import *

graph = Greedy(8)
s = graph.compute()
print("Distance greedy: ", graph.compute_distance_by_path(s))
graph.draw_path(s)
g = Greedy_opti(8, graph.get_vertices())
s2 = g.compute()
graph.draw_path(s2)
print("Distance greedy opti: ", g.compute_distance_by_path(s2))
