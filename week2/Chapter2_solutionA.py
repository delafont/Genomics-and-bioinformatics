# Question 3.1 #
from Bio import SeqIO
genome = SeqIO.read("chr18.fa", "fasta")

# Question 3.2 #
total_length = len(genome)
print "The length is:", total_length

# Question 3.3 #
A_count = genome.seq.count('A')
C_count = genome.seq.count('C')
G_count = genome.seq.count('G')
T_count = genome.seq.count('T')
print 'A: %s, C: %s, G: %s, T: %s' % (A_count, C_count, G_count, T_count)

# Question 3.4 #
from Bio.SeqUtils import GC
gc_percentage = GC(genome.seq)
print "The total GC percentage is:", gc_percentage

# Question 3.5 computing #
number_of_points = 1000
window_size      = total_length / number_of_points
start_positions  = range(0, total_length, window_size)
gc_per_window    = []
for start in start_positions:
    stop  = start + window_size
    gc_in_window = GC(genome[start:stop].seq)
    gc_per_window.append(gc_in_window)

# Question 3.5 plotting #
from matplotlib import pyplot
pyplot.plot(start_positions, gc_per_window)
pyplot.title("GC content with a window size of %i base pairs" % window_size)
pyplot.xlabel("Genome position [base pairs]")
pyplot.ylabel("GC content [%]")
pyplot.ion()

# Question 3.6 #
with open('gc_per_window.txt', 'w') as f:
    for i in xrange(number_of_points):
        start = start_positions[i]
        stop  = start_positions[i] + window_size
        gc    = gc_per_window[i]
        line  = "%i\t%i\t%f\n" % (start, stop, gc)
        f.write(line)
