# Brute force algorithm for Hamiltonian problem #
"""
EXAMPLE
edges = [('ATGTC', 'GTCGA'), ('GTCGA', 'CGATT'), ('AATGT', 'ATGTC')]
comb = [('ATGTC', 'GTCGA'), ('GTCGA', 'CGATT'), ('AATGT', 'ATGTC')]
return = ['AATGT', 'ATGTC', 'GTCGA', 'CGATT']
sequence = AATGTCGATT
"""

def bruteforce(edges, min_overlap):
    """Simply generates all permutation
       and finds the one that passes as the longest
       sequence"""
    # Generate all possiblities #
    from itertools import permutations
    combinations = permutations(edges)
    # Initial variables #
    best_sequence = ''
    best_path = None
    best_length = -1
    # Core loop #
    for comb in combinations:
        # How far can we follow it #
        for i in xrange(len(comb)-1):
            edgeA = comb[i]
            edgeB = comb[i+1]
            if edgeA[1] != edgeB[0]:
                comb = comb[:i+1]
                break
        if not comb: continue
        # How long is it ? #
        path = [edge[0] for edge in comb] + [comb[-1][1]]
        sequence = make_sequence(path, min_overlap)
        comb_length = len(sequence)
        if comb_length > best_length:
            best_sequence = sequence
            best_path     = path
            best_length   = comb_length
    return best_path

# Hierholzer's algorithm for Eulerian graphs #
"""
EXAMPLE
V = [1,2,3,4,5,6]
E = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1),(2,6),(6,4),(4,2)]
r = [1, 2, 6, 4, 2, 3, 4, 5, 6, 1]

EXAMPLE
V = ["AA","AB","BC","CD","DE","EF"]
E = [("AA","AB"),("AB","BC"),("BC","CD"),("CD","DE"),("DE","EF"),("EF","AA"),("AB","EF"),("EF","CD"),("CD","AB")]
r = ['AA', 'AB', 'EF', 'CD', 'AB', 'BC', 'CD', 'DE', 'EF', 'AA']
"""

def adjacents(vertex, edges):
    """Returns the list of edges from *edges* adjacent to node *vertex*."""
    return [edge for edge in edges if edge[0] == vertex]

def walk(vertex, edges):
    """From node *vertex*, walk along edges *edges*, never taking an already
    used one. Return the chosen *path* and the remaining edges.
    If the graph is Eulerian, *path* is a cycle."""
    path = [vertex]; adj = adjacents(vertex,edges)
    while adj:
        e = adj[0]
        edges.remove(e)
        path.append(e[1])
        vertex = e[1]
        adj = adjacents(vertex,edges)
    return path, edges

def hierholzer(vertices, edges):
    """Finds an Eulerian cycle in a connected Eulerian graph defined
    by the set *vertices* of its vertices and the set *edges* of its edges.
    The cycle is returned as a list of vertices."""
    assert any([len(adjacents(v,edges))%2==1 for v in vertices]), "Your graph is not Eulerian."
    v = vertices[0]
    cycle, edges = walk(v, edges)
    notvisited = set(cycle)
    while len(notvisited) != 0:
        v = notvisited.pop()
        if len(adjacents(v, edges)) != 0:
            i = cycle.index(v)
            sub, E = walk(v, edges)
            cycle = cycle[:i]+sub+cycle[i+1:]
            notvisited.update(sub)
    return cycle[:-1]

"""
EXAMPLE
path = ['AATGT', 'ATGTC', 'GTCGA', 'CGATT']
return = AATGTCGATT
"""
# Sequence retrival #
def make_sequence(path, min_overlap):
    """From a list of vertices, builds the contig"""
    sequence = path[0]
    for i, vertex in enumerate(path[1:]):
        sequence = overlaps(sequence, vertex, min_overlap)
        if not sequence: raise Exception("You didn't input a path: " + path[i-1] + '-' + path[i] + '-' + path[i+1] )
    return sequence
