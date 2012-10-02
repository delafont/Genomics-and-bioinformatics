
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

#------------------#
# Overlap function #
#------------------#
def overlaps(read1, read2, min_overlap=3):
    """If the end of read1 overlaps with at least *min_overlap* nucleotides
    of read2, return the overlap sequence, False otherwise."""
    read_length = min(len(read1),len(read2))
    for i in range(read_length, min_overlap-1, -1):
        if read1[-i:] == read2[:i]:
            return read2[:i]
    return False

#--------------------------------------------------#
# Build the graph for the Hamiltonian path problem #
#--------------------------------------------------#
min_overlap = 3
V = list(set(reads)) # One can use list(set()) to get unique values in Python
E = [(r1,r2) for r1 in V for r2 in V \
            if overlaps(r1,r2,min_overlap) and not r1 == r2]
            #'\' is to continue on a new line
print "Vertices:", V
print "Edges:", E

#---------------#
# Find the path #
#---------------#
import hamiltonian
path = hamiltonian.hamiltonian(V,E)[0]
print "Hamiltonian path:", path

#------------------------#
# Reconstruct the contig #
#------------------------#
contig = path[0] # begin from the 'start' vertex
for i in range(1,len(path)):
    contig = contig + path[i][len(overlaps(path[i-1],path[i],3)):] # add the last letter of each vertex in the path
print "Contig:",contig


"""
EXAMPLE
min_overlap = 3
V = [AATGT, ATGTC, GTCGA, CGATT]
E = [(AATGT,ATGTC), (ATGTC,GTCGA), (GTCGA,CGATT)]
sequence = "AATGTCGATT"
"""

