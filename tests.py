from graph import Graph

g = Graph(10)
shortest = g.brute_force()
print(g.compute_distance_by_path(shortest))