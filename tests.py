from graph import Graph
g = Graph(9)
shortest = g.brute_force()
print(g.compute_distance_by_path(shortest))