# Question 2.1 #
with open('reads.fastq', 'r') as f:
    reads = [line.strip() for line in f]
num_of_reads = len(reads)
read_length = len(reads[1])

# Question 2.2 #
def overlaps(read1, read2, min_overlap=10):
    """Returns a positive number if the end of read1
       overlaps with the begining of read2, 0 otherwise"""
    for i in xrange(read_length, min_overlap, -1):
        if read1[-i:] == read2[0:i]: return i
    return 0.0

# Question 2.3 #
from numpy import zeros
edges_matrix = zeros((num_of_reads, num_of_reads))
for i in xrange(num_of_reads):
    for j in xrange(num_of_reads):
        if i == j: continue
        edges_matrix[i][j] = overlaps(reads[i], reads[j])

# Question 2.4 #
