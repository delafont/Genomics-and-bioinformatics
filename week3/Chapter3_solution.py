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
        if read1[-i:] == read2[0:i]: return read1[-i:]
    return 0

# Question 2.3 #
v = reads
e = [(r1,r2) for r1 in l for r2 in l if r1 != r2 and overlaps(r1,r2)]

# Question 2.4 #
