# Sample graph
# V = [1,2,3,4,5,6]
# E = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1),(2,6),(6,4),(4,2)]
# This program finds [1, 2, 6, 4, 2, 3, 4, 5, 6, 1]
# V = ["AA","AB","BC","CD","DE","EF"]
# E = [("AA","AB"),("AB","BC"),("BC","CD"),("CD","DE"),("DE","EF"),
#      ("EF","AA"),("AB","EF"),("EF","CD"),("CD","AB")]
# Returns ("EF","AA"),("AB","EF"),("EF","CD"),("CD","AB")]

def adjacents(v,E):
    """Returns the list of edges from *E* adjacent to node *v*."""
    return [edge for edge in E if edge[0]==v]

def walk(v,E):
    """From node *v*, walk along edges *E*, never taking an already
    used one. Return the chosen *path* and the remaining edges.
    If the graph is Eulerian, *path* is a cycle."""
    path = [v]; adj = adjacents(v,E)
    while adj:
        e = adj[0]
        E.remove(e)
        path.append(e[1])
        v = e[1]
        adj = adjacents(v,E)
        if len(adj) == 0: return path, E

def hierholzer(V,E):
    """Finds an Eulerian cycle in a connected Eulerian graph defined
    by the set *V* of its vertices and the set *E* of its edges.
    The cycle is returned as a list of vertices."""
    v = V[0]
    cycle, E = walk(v,E)
    while len(E) != 0:
        for i in range(len(cycle)):
            v = cycle[i]
            if len(adjacents(v,E)) != 0:
                sub, E = walk(v,E)
                cycle = cycle[:i]+sub+cycle[i+1:]
    return cycle
