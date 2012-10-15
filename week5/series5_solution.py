#--------------#
# Question 2.1 #
#--------------#

bases = ['t', 'c', 'a', 'g']
codons = [x+y+z for x in bases for y in bases for z in bases]

#--------------#
# Question 2.2 #
#--------------#

aminos = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codon_to_amino = dict(zip(codons, aminos))

#--------------#
# Question 2.3 #
#--------------#

def translate(seq):
    translation = [codon_to_amino[seq[i:i+3]] for i in range(0,len(seq),3)]
    return ''.join(translation) # transforms the list into a string

#--------------#
# Question 2.4 #
#--------------#

def complementary(seq):
    compl = []
    for letter in seq:
        if letter == "a":
            compl.append("t")
        if letter == "c":
            compl.append("g")
        if letter == "g":
            compl.append("c")
        if letter == "t":
            compl.append("a")
    return ''.join(reversed(compl))

def cut(seq):
    """Cut the given sequence such that its length is a factor of three."""
    if len(seq)%3 == 0:
        sequence = seq
    elif len(seq)%3 == 1:
        sequence = seq[:-1]
    elif len(seq)%3 == 2:
        sequence = seq[:-2]
    return sequence

raw = open('sequence_001.txt', 'r').read()
sequence_raw = raw.replace('\n','').replace(' ','') # remove spaces and newlines
complement_raw = complementary(sequence_raw)

for i in [0,1,2]:
    sequence = cut(sequence_raw[i:])
    complement = cut(complement_raw[i:])
    print "Forward strand "+str(i)+": ",  translate(sequence)
    print "Reverse strand "+str(i)+": ", translate(complement)

"""
The answer is obviously the third reading frame in the forward direction since the
other reading frames are filled with stop codons everywhere.

This example was taken from the yeast TCP1-beta gene.
The original file is found here:

http://www.ncbi.nlm.nih.gov/sites/entrez?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=1293613
"""
