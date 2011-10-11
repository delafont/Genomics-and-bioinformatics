
#--------------------#
#--- Question 2.2 ---#
#--------------------#

"""
We used a lot of "List comprehensions" here. For example,
print [a+5 for a in [1,2,3,4,5,6]]
returns: [6,7,8,9,10,11]
Each time you can replace it by
for a in [1,2,3,4,5,6]:
    print a+5
But list comprehensions are one of the reasons why Python is attractive, try it!

The code is designed to work in simple situations, where for example
reads overlap only two-by-two.
"""

#reads = ["CCACAG", "CACAGA"] # min overlap is 5
#reads = ["AAATTTGGC", "TGGCAAA", "CAAATTGCGAGT"] #min overlap is 4
reads = ["AATGT", "ATGTC", "GTCGA", "CGATT"] # min overlap is 3
#reads = ["AATGT","TGTAT","GTATG","ATGCC"] # min overlap is 3

l = 3  #arbitrary, but need *l* inferior or equal to *min_overlap*+1

#------------------#
# Overlap function #
#------------------#
# The function from exercise 1. We will reuse it.
def overlaps(read1, read2, min_overlap):
    """If the end of read1 overlaps with at least *min_overlaps* nucleotides
    of read2, return the overlap sequence, False otherwise."""
    read_length = min(len(read1),len(read2))
    if read1 in read2: return read1
    if read2 in read1: return read2
    for i in xrange(read_length, min_overlap-1, -1):
        if read1[-i:] == read2[:i]:
            return read2[:i]
    return "" # small change here, because False has no length.

#------------------#
# Subseqs function #
#------------------#
def subseqs(read, l):
    """Extracts all sub-sequences of length l"""
    return [read[i:i+l] for i in xrange(len(read)-l+1)]

#----------------------#
# Build the dual graph #
#----------------------#
Vdual = [] # Vertices: all unique (l-1)-mers
for r in reads: Vdual.extend(subseqs(r,l-1))
Vdual = list(set(Vdual))

Sl = [] # All l-mers
for r in reads: Sl.extend(subseqs(r,l))

"""
This would suffice with the example we gave you, but actually you
are counting twice l-mers from overlap sequences. One has to remove copies.
It is even more complicated than what is written here, especially if multiple reads
overlap in the same region.
"""
Olaps = [overlaps(v1,v2,l) for v1 in reads for v2 in reads if v1!=v2]
copies = []
for o in Olaps: copies.extend(subseqs(o,l))
for c in copies: Sl.pop(Sl.index(c))

Edual = [] # Edges
for s in Sl:
    linked_by_s = [(v1,v2) for v1 in Vdual for v2 in Vdual if (s[:-1]==v1 and s[1:]==v2 and v1!=v2)]
    Edual.extend(linked_by_s)

print "Vertices:", Vdual
print "Sl:", Sl
print "Edges:", Edual

#--------------------------------#
# Find start and end, bind them. #
#--------------------------------#
"""
This part is more difficult.
The general way to find the start and end of your contig is to look for
vertices with unequal number of outgoing and incoming edges.
You don't have to create functions, but else it becomes very ugly and
more difficult to understand.
"""

def outgoing(vertex, edges):
    """Returns the list of edges from *edges* entering into node *vertex*."""
    return [edge for edge in edges if edge[0] == vertex]

def incoming(vertex, edges):
    """Returns the list of edges from *edges* coming from node *vertex*."""
    return [edge for edge in edges if edge[1] == vertex]

start = [v for v in Vdual if len(outgoing(v,Edual)) > len(incoming(v,Edual))]
end = [v for v in Vdual if len(outgoing(v,Edual)) < len(incoming(v,Edual))]
Edual.append((end[0], start[0]))
print "start:",start, ",\t end:",end # start and end should both have only one element.


#---------------#
# Find the path #
#---------------#
import hierholzer
path = hierholzer.hierholzer(Vdual, Edual)

#------------------------#
# Reconstruct the contig #
#------------------------#
istart = path.index(start[0])
path = path[istart:]+path[:istart]
print "Eulerian path:", path[:-1]
contig = path[0]
for i in range(1,len(path)-1):
    contig = contig+path[i][-1]
print "Contig:",contig

"""
e.g. with l=3:
Sequence: AATGTCGATT
Reads: AATGT, ATGTC, GTCGA, CGATT
Vdual = AA, AT, TG, GT, TC, CG, TT, GA
Sl = AAT, ATG, TGT, GTC, TCG, CGA, GAT, ATT, TTG, TGA, GAC
Edual = [(AA,AT), (AT,TG), (AT,TT), (AT,GA), ...]

The graph: TG -> GT -> TC
           ^           ^
           |           |
     AA -> AT <- GA <- CG
       ^   |
        \  v             # AA-TT to close the cycle
           TT            # begin from AA, then add the last base of each vertex.
"""
