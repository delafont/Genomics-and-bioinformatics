
""" Question 2.1 """

def overlaps(read1, read2, min_overlap=3):
    """Returns the overlap sequence if the end of read1
    overlaps with the begining of read2, False otherwise"""
    for i in xrange( min(len(read1),len(read2)), min_overlap-1, -1):
        if read1[-i:] == read2[:i]: return read2[:i]
    return False

""" Read the file """
with open('reads1.fastq', 'r') as f:
    reads = [line.strip() for line in f]
num_of_reads = len(reads)
read_length = len(reads[0])

""" Build the graph for the Hamiltonian path problem """
vertices = list(set(reads)) # one can use list(set()) to get unique values in Python. Unfortunately, no built-in function exists.
edges = [(r1,r2) for r1 in vertices for r2 in vertices if overlaps(r1,r2)]
olaps = {} # remember the overlap sequence corresponding to each edge
for e in edges:
    olaps[e] = overlaps(e[0],e[1])

""" Find the path """
import findcycles
import time
t1 = time.time()
#sequence = findcycles.bruteforce(list(edges))
t2 = time.time()
#print sequence
print "Time to find a cycle:", t2-t1

"""
e.g. with min_overlap=3:
Sequence: AATGTCGATT
V = [AATGT, ATGTC, GTCGA, CGATT]
E = [(AATGT,ATGTC), (ATGTC,GTCGA), (GTCGA,CGATT)]
Edges are defined as couples of vertices, but we like to keep the overlap sequence between them.
"""

#----------------------------------------------------------------------------------------------#

""" Question 2.2 """

def subseqs(read, l):
    """Extracts all sub-sequences of length l"""
    return [read[i:i+l] for i in xrange(len(read)-l+1)]

""" Read the file again if needed """
with open('reads1.fastq', 'r') as f:
    reads = [line.strip() for line in f]
num_of_reads = len(reads)
read_length = len(reads[0])
l = 3 # arbitrary

""" Build the dual graph """
Vdual = []
for r in reads: Vdual.extend(subseqs(r,l-1))
Vdual = list(set(Vdual))

Sl = []
for r in reads: Sl.extend(subseqs(r,l))
Sl = list(set(Sl))

Edual = []
for s in Sl:
    Edual.extend([(v1,v2) for v1 in Vdual for v2 in Vdual if (s[:-1]==v1 and s[1:]==v2)])
Edual = list(set(Edual))

""" Find the path """
import findcycles
import time
t1 = time.time()
path = findcycles.hierholzer(Vdual, Edual)
t2 = time.time()
print "Eulerian path:", path
print "Time to find a cycle:", t2-t1

"""
e.g. with l=3:
Sequence: AATGTCGATT
Reads: AATGT, ATGTC, GTCGA, CGATT
Vdual = AA, AT, TG, GT, TC, CG, TT, GA
Sl = AAT, ATG, TGT, GTC, TCG, CGA, GAT, ATT, TTG, TGA, GAC
Edual = [(AA,AT), (AT,TG), (AT,TT), (AT,GA), ...]

The graph: TG -> GT -> TC
           |           |
     AA -> AT <- GA <- CG
         \ |             # AA-TT to close the cycle
           TT            # begin from AA, then add the last base of each vertex.
"""
