
#--------------------#
#--- Question 2.1 ---#
#--------------------#

#---------------#
# Read the file #
#---------------#
#with open('reads1.fastq', 'r') as f:
#    reads = [line.strip() for line in f]
num_of_reads = len(reads)
read_length = len(reads[0])
min_overlap = 5

#------------------#
# Overlap function #
#------------------#
def overlaps(read1, read2, min_overlap):
    """If the end of read1 overlaps with at least *min_overlaps* nucleotides
    of read2, return the overlap sequence, False otherwise."""
    for i in xrange(read_length, min_overlap-1, -1):
        if read1[-i:] == read2[:i]: return read1 + read2[i:]
    return False

#--------------------------------------------------#
# Build the graph for the Hamiltonian path problem #
#--------------------------------------------------#
vertices = list(set(reads)) # One can use list(set()) to get unique values in Python
edges = [(r1,r2) for r1 in vertices for r2 in vertices if overlaps(r1,r2,min_overlap) and not r1 == r2]

"""
EXAMPLE
min_overlap = 3
vertices = [AATGT, ATGTC, GTCGA, CGATT]
edges = [(AATGT,ATGTC), (ATGTC,GTCGA), (GTCGA,CGATT)]
sequence = "AATGTCGATT"
"""

#----------------------------------------------------------------------------------------------#

#--------------------#
#--- Question 2.2 ---#
#--------------------#

def subseqs(read, l):
    """Extracts all sub-sequences of length l"""
    return [read[i:i+l] for i in xrange(len(read)-l+1)]

l = 3  #arbitrary, but needs to be small enough

#----------------------#
# Build the dual graph #
#----------------------#
Vdual = [] # All (l-1)-mers
for r in reads: Vdual.extend(subseqs(r,l-1))
Vdual = list(set(Vdual))

Sl = [] # All l-mers
for r in reads: Sl.extend(subseqs(r,l))
Sl = list(set(Sl))

Edual = []
for s in Sl:
    Edual.extend([(v1,v2) for v1 in Vdual for v2 in Vdual if (s[:-1]==v1 and s[1:]==v2)])
Edual = list(set(Edual))

#--------------------------------#
# Find start and end, bind them. #
#--------------------------------#
""" For our simple case, you were asked to do something like the following:

starts = [e[0] for e in Edual]
ends = [e[1] for e in Edual]
uniques = [e for e in starts+ends if (e in starts and e not in ends)
                                  or (e in ends and e not in starts)]
Edual.append((uniques[1],uniques[0]))

However, here is the general way to find the start and end of your contig,
which are the vertices with unequal number of outgoing and incoming edges: """

from hierholzer import incoming, outgoing
start, end = [v for v in Vdual if len(outgoing(v,Edual)) != len(incoming(v,Edual))]
print start, end # if you get more or less than 2 elements, choose a better value of *l*.
Edual.append((end, start))

#---------------#
# Find the path #
#---------------#
import hierholzer
path = hierholzer.hierholzer(Vdual, Edual)
print "Eulerian path:", path

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