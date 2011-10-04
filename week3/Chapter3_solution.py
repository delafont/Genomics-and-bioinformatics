# Question 2.1 #
# Read the file #
with open('reads2.fastq', 'r') as f:
    reads = [line.strip() for line in f]
num_of_reads = len(reads)
read_length = len(reads[0])
min_overlap = 5

# Overlap function #
def overlaps(read1, read2, min_overlap):
    """If the end of read1 overlaps with the begining of read2,
       return read1 extended with the overlap, False otherwise."""
    for i in xrange(read_length, min_overlap-1, -1):
        if read1[-i:] == read2[:i]: return read1 + read2[i:]
    return False

# Build the graph for the Hamiltonian path problem #
# One can use list(set()) to get unique values in Python
vertices = list(set(reads))
edges = [(r1,r2) for r1 in vertices for r2 in vertices if overlaps(r1,r2,min_overlap) and not r1 == r2]

# Find the path #
import time
import findcycles
t1 = time.time()
path = findcycles.bruteforce(edges, min_overlap)
t2 = time.time()

# Display info #
print "Hamiltonian path:", path
print "Time to find it: %s seconds" % (t2-t1)
print "The sequence:", make_sequence(path, min_overlap)

"""
EXAMPLE
min_overlap = 3
vertices = [AATGT, ATGTC, GTCGA, CGATT]
edges = [(AATGT,ATGTC), (ATGTC,GTCGA), (GTCGA,CGATT)]
sequence = "AATGTCGATT"
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

""" Find start and end, bind them """
starts = [e[0] for e in Edual]
ends = [e[1] for e in Edual]
uniques = [e for e in starts+ends if (e in starts and e not in ends)
                                  or (e in ends and e not in starts)] #should be 2 elements
Edual.append((uniques[1],uniques[0]))

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

