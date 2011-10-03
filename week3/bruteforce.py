# Sample graph
# V = [1,2,3,4,5,6]
# E = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1),(2,6),(6,4),(4,2)]
# This program finds [1, 2, 6, 4, 2, 3, 4, 5, 6, 1]

def adjacents(v,E):
    """Returns the list of edges from *E* adjacent to node *v*."""
    return [edge for edge in E if edge[0]==v]

def walk(v,E):
    """From node *v*, walk along edges *E*, never taking an already
    used one. Returns the chosen *path* and the remaining edges.
    If the graph is Eulerian, *path* is a cycle."""
    path = [v]; adj = adjacents(v,E)
    while 1:
        e = adj[0]
        E.remove(e)
        path.append(e[1])
        v = e[1]
        adj = adjacents(v,E)
        if len(adj) == 0: return path, E

def bruteforce(V,E):
    """Lorem ipsum."""
    return cycle
