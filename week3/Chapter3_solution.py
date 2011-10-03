"""
This has been written without even running a Python instance.
One needs to complete, correct and test it.
"""

# Question 2.1 #
def overlaps(read1, read2, min_overlap=10):
    """Returns the overlap sequence if the end of read1
    overlaps with the begining of read2, False otherwise"""
    for i in xrange(read_length, min_overlap, -1):
        if read1[-i:] == read2[:i]: return read2[:i]
    return False

# Read the file #
with open('reads1.fastq', 'r') as f:
    reads = [line.strip() for line in f]
num_of_reads = len(reads)
read_length = len(reads[0])

# Build the graph for the Hamiltonian path problem
vertices = set(reads) # vertices # use sets to have only unique elements
edges = set([(r1,overlaps(r1,r2),r2) for (r1,r2) in zip(vertices,vertices) if overlaps(r1,r2)]) # edges

# Find the path #
sequence = bruteforce(edges)
print sequence

"""
e.g. with min_overlap=3:
Sequence: AATGTCGATT
V = [AATGT, ATGTC, GTCGA, CGATT]
E = [(AATGT,ATGT,ATGTC), (ATGTC,GTC,GTCGA), (GTCGA,CGA,CGATT)]
Edges are defined as couples of vertices, but we like to keep the overlap sequence between them.
"""

# Question 2.2 #
def subseqs(read, l):
    """Extracts all sub-sequences of length l"""
    return [read[i:i+l] for i in xrange(len(read)-l)]

# Build the dual graph #
l = read_length-1 # arbitrary, to reduce the number of elements

Vdual = []
for r in reads: Vdual.extend(subseqs(r,l-1))
Vdual = set(Vdual)

Sl = []
for r in reads: Sl.extend(subseqs(r,l))
Sl = set(Sl)

Edual = []
for s in Sl: Edual.extend([(v1,s,v2) for (v1,v2) in zip(Vdual,Vdual) if (s[:-1]==v1 and s[l:]==v2)])
Edual = set(Edual)

# Find the path #
path = hierholzer(Vdual, Edual)

"""
e.g. with l=3:
Sequence: AATGTCGATT
Reads: AATGT, ATGTC, GTCGA, CGATT
Vdual = AA, AT, TG, GT, TC, CG, TT, GA
Sl = AAT, ATG, TGT, GTC, TCG, CGA, GAT, ATT, TTG, TGA, GAC
Edual = [(AA,AAT,AT), (AT,ATG,TG), (AT,ATT,TT), (AT,TGA,GA), ...]

The graph: TG -> GT -> TC
           |           |
     AA -> AT <- GA <- CG
         \ |             # AA-TT to close the cycle
           TT            # begin from AA, then add the last base of each vertex.
"""
