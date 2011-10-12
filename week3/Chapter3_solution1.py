
#--------------------#
#--- Question 2.1 ---#
#--------------------#

#---------------#
# Read the file #
#---------------#
f = open('reads1.fastq', 'r')
reads = []
for line in f:
    reads.append(line.strip()) 
    # .strip('xyz') removes chars x,y,z at both extremities of the string
    # use .split() if you need to extract words from a line

num_of_reads = len(reads)
read_length = len(reads[0])
min_overlap = 5

#------------------#
# Overlap function #
#------------------#
def overlaps(read1, read2, min_overlap):
    """If the end of read1 overlaps with at least *min_overlaps* nucleotides
    of read2, return the overlap sequence, False otherwise."""
    read_length = min(len(read1),len(read2))
    for i in xrange(read_length, min_overlap-1, -1):
        if read1[-i:] == read2[:i]: 
            return read2[:i]
    return False

#--------------------------------------------------#
# Build the graph for the Hamiltonian path problem #
#--------------------------------------------------#
vertices = list(set(reads)) # One can use list(set()) to get unique values in Python
edges = [(r1,r2) for r1 in vertices for r2 in vertices \
            if overlaps(r1,r2,min_overlap) and not r1 == r2] 
            #'\' is to continue on a new line

""" 
Try to write an algorithm that finds the way if you like.
The idea would be the following (runs in exponential time):
Walk along the graph while you can, mark already visited nodes.
If the current node has no unvisited neighbours, step back one node and try another way.
"""

"""
EXAMPLE
min_overlap = 3
vertices = [AATGT, ATGTC, GTCGA, CGATT]
edges = [(AATGT,ATGTC), (ATGTC,GTCGA), (GTCGA,CGATT)]
sequence = "AATGTCGATT"
"""


#--------------------#
#--- Question 2.2 ---#
#--------------------#

# See next week!
