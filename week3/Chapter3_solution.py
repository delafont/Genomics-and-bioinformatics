# Question 2.1 #
with open('reads.fastq', 'r') as f:
    v = [line.strip() for line in f]
num_of_reads = len(v)
read_length = len(v[1])

# Question 2.2 #
def overlaps(read1, read2, min_overlap=10):
    """Returns True if end of read1 overlaps with
       the begining of read2, False otherwise"""
    for i in xrange(min_overlap, read_length):
        if read1[-i] == read2[i]: return True
    return False

# Question 2.3 #
from numpy import zeros
edges_matrix = zeros((num_of_reads, num_of_reads))
for i,j in zip(xrange(num_of_reads), file2)
