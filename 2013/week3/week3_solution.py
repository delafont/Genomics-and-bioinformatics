#--------------#
# Question 3.1 #
#--------------#

from Bio import SeqIO
genome = SeqIO.read("chrI.fa", "fasta")  # This creates a 'SeqRecord' object
sequence = genome.seq  # a 'Seq' object, similar to a string

# Alternatively:

f = open("chrI.fa")
sequence = f.read()  # a string
f.close()

"""Note that in this case all the file is read as a single string.
For large genomes this could cause memory problems! It is even worse with annotation files.
Note also the multiple-line comment we use here."""

#--------------#
# Question 3.2 #
#--------------#

total_length = len(sequence)
print "The length is:", total_length

#--------------#
# Question 3.3 #
#--------------#

sequence = sequence.lower()  # transforms characters to lower case
a = sequence.count('a')
c = sequence.count('c')
g = sequence.count('g')
t = sequence.count('t')
print 'A: %s, C: %s, G: %s, T: %s' % (a,c,g,t)
# each '%s' will be replaced by the corresponding string on the right of the '%'

# Alternatively:
a=0; c=0; g=0; t=0; n=0
for base in sequence:
    base = base.lower()
    if base == 'a': a+=1 # equivalent to a = a+1
    elif base == 'c': c+=1
    elif base == 'g': g+=1
    elif base == 't': t+=1
    else: n+=1 # There are 'N's in the file to indicate repeated (uninteresting) sequences.
print 'A: %s, C: %s, G: %s, T: %s' % (a,c,g,t)

#--------------#
# Question 3.4 #
#--------------#

# Either import the Biopyton GC function:
from Bio.SeqUtils import GC

# or use your own:
def GC(sequence):
    a=0; c=0; g=0; t=0; n=0
    for base in sequence:
        base = base.lower()
        if base == 'a': a+=1
        elif base == 'c': c+=1
        elif base == 'g': g+=1
        elif base == 't': t+=1
        else: n+=1
    return 100*float(c+g)/len(sequence)

gc_percentage = GC(sequence)
print "The total GC percentage is:", gc_percentage

#---------------------------#
# Question 3.5(a) computing #
#---------------------------#

window_size = 100000  # arbitrary
start_positions = range(0, total_length, window_size)
gc_per_window = []

for start in start_positions:
    stop  = start + window_size
    gc_in_window = GC(sequence[start:stop])
    gc_per_window.append(gc_in_window)

#--------------------------#
# Question 3.5(b) plotting #
#--------------------------#

from matplotlib.pyplot import *
plot(start_positions, gc_per_window)
title("GC content with a window size of %i base pairs" % window_size)
xlabel("Genome position [base pairs]")
ylabel("GC content [%]")
show()

#--------------#
# Question 3.6 #
#--------------#

f = open('gc_per_window.txt', 'w')
for i in range(number_of_windows):
    start = start_positions[i]
    stop  = start_positions[i] + window_size
    gc    = gc_per_window[i]
    line  = "%i\t%i\t%f\n" % (start, stop, gc) # %i - integer, %f - float, "\t" - tab, "\n" - newline
    f.write(line)
f.close()
