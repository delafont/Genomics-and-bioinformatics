
# Deep search algorithm to find an Hamiltonian path in a graph
# (visiting every edge once and only once)
"""
EXAMPLES

V = ['AA','AB','BC','CD','DE','EF']
E = [('AA','AB'),('AB','BC'),('BC','CD'),('CD','DE'),('DE','EF'),('EF','AA'),('AB','EF'),('EF','CD'),('CD','AB')]
returns [['AA','AB','BC','CD','DE','EF'], ['AB','BC','CD','DE','EF','AA'], ['BC','CD','DE','EF','AA','AB'],
         ['CD','DE','EF','AA','AB','BC'], ['DE','EF','AA','AB','BC','CD'], ['EF','AA','AB','BC','CD','DE']]

V = ['a','b','c','d','e']
E = [('a','b'),('a','c'),('b','d'),('d','c'),('d','e'),('e','c'),('c','e')]
returns [['a', 'b', 'd', 'c', 'e'], ['a', 'b', 'd', 'e', 'c']]
"""

import time

class Node(object):
    def __init__(self, name='',idx=-1,active=1,label=''):
        self.name = name        # node name
        self.idx = idx          # node index
        self.neighbours = set() # all accessible nodes

    def __eq__(self,node):
        return self.idx == node.idx and self.name == node.name

class Vertex(object):
    def __init__(self,inc,out, name='',label='',active=1):
        assert isinstance(inc,Node), "Expected Node class, got %s." % type(inc)
        assert isinstance(out,Node), "Expected Node class, got %s." % type(out)
        self.inc = inc          # node it comes from
        self.out = out          # node it goes to
        self.name = ''          # vertex name

    def __getitem__(self,i):
        if i==0: return self.inc
        if i==1: return self.out


def hamiltonian(V, E):
    E = set([Vertex(Node(name=e[0],idx=V.index(e[0])),Node(name=e[1],idx=V.index(e[1]))) for e in E])
    V = [Node(idx=i,name=V[i]) for i in range(len(V))]
    for e in E:
        V[e[0].idx].neighbours.add(V[e[1].idx])
    t1 = time.time()
    L = 1
    paths = [[v] for v in V]
    while L < len(V):
        q = []
        toremove = []
        for p in paths:
            if p[-1].neighbours:
                for n in p[-1].neighbours:
                    if n not in p:
                        q.append(p+[n])
            else:
                toremove.append(p)
        for p in toremove: paths.remove(p)
        L+=1
        paths = q
    t2 = time.time()
    print "Running time: %s" % (t2-t1,)
    return [[n.name for n in p] for p in paths]

