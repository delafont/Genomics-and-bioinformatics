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

# Read the file
with open('reads.fastq', 'r') as f:
    reads = [line.strip() for line in f]
num_of_reads = len(reads)
read_length = len(reads[0])

# Build the graph for the Hamiltonian path problem
V = set(reads) # vertices # use sets to have only unique elements
E = set([(r1,overlaps(r1,r2),r2) for (r1,r2) in zip(V,V) if overlaps(r1,r2)]) # edges

"""
e.g. with min_overlap=3:
V = [ATTTGCG, TGCGAAT, CCCCGTA]
E = [(ATTTGCG,TGCG,TGCGAAT)]
Edges are defined as couples of vertices, but we like to keep the overlap sequence between them.
"""


# Question 2.2#
def subseqs(read,l):
    """Extracts all sub-sequences of length l"""
    subs = []
    for i in len(read)-l:
        subs.append(read[i:i+l])
    return subs

l = read_length-1 # arbitrary, to reduce the number of elements

# Build the dual graph 
Vdual = []
for r in reads:
    Vdual.extend([subseqs(r,l) for r in reads])
Vdual = set(Vdual)
Edual = []
for r in reads:
    Edual.extend([(v1,r,v2) for (v1,v2) in zip(Vdual,Vdual) if (r[:l]==v1 and r[-l:]==v2)])
Edual = set(Edual)

"""
e.g. with l=6:
Vdual = [ATTTGC,TTTGCG,TGCGAA,GCGAAT,CCCCGT,CCCGTA]
Edual = [(ATTTGC,ATTTGCG,TTTGCG),(TGCGAA,TGCGAAT,GCGAAT),(CCCCGT,CCCCGTA,CCCGTA)]
Again, should be couples of vertices, but we want to keep the read each edge corresponds to.
"""
