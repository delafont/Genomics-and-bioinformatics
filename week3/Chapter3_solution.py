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
t1 = time.time()
path = bruteforce(edges, min_overlap)
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

# Question 2.2 #
def subseqs(read, l):
    """Extracts all sub-sequences of length l"""
    return [read[i:i+l] for i in xrange(len(read)-l+1)]

# Build the dual graph #
all_lmers = []
for r in reads: all_lmers.extend(subseqs(r,min_overlap))
all_lmers = list(set(all_lmers))

all_lmers_minus_one = []
for r in reads: all_lmers_minus_one.extend(subseqs(r,min_overlap-1))
all_lmers_minus_one = list(set(all_lmers_minus_one))

# The edges #
edges = []
for lmer in all_lmers:
    for small1 in all_lmers_minus_one:
        for small2 in all_lmers_minus_one:
            if lmer[:-1]==small1 and lmer[1:]==small2:
                edges.append((small1,small2))
edges = list(set(edges))

# Find the path #
import time
t1 = time.time()
path = hierholzer(all_lmers_minus_one, edges)
t2 = time.time()

# Display info #
print "Eulerian path:", path
print "Time to find it: %s seconds" % (t2-t1)
print "The sequence:", make_sequence(path[:], min_overlap-2)

"""
e.g. with l=3:
Sequence: AATGTCGATT
Reads: AATGT, ATGTC, GTCGA, CGATT
all_lmers           = AAT, ATG, TGT, GTC, TCG, CGA, GAT, ATT, TTG, TGA, GAC
all_lmers_minus_one = AA, AT, TG, GT, TC, CG, TT, GA
edges = [(AA,AT), (AT,TG), (AT,TT), (AT,GA), ...]

The graph: TG -> GT -> TC
           |           |
     AA -> AT <- GA <- CG
      \    |             # AA-TT to close the cycle
       --> TT            # begin from AA, then add the last base of each vertex.
"""
