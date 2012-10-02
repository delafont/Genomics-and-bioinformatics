
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

raw = open('sequence_001.txt', 'r').read()
sequence = raw.replace(' ','').replace('\n','') # remove spaces and newlines
for i in [0,1,2]: # forward strand
    print translate(sequence[i:])
complementary = sequence.lower().replace('a','t').replace('t','a').replace('g','c').replace('c','g')
for i in [-1,-2,-3]: # reverse strand
    print translate(complementary[i::-1])

"""
The answer is obviously the third reading frame in the forward direction since the
other reading frames are filled with stop codons everywhere.

This example was taken from the yeast TCP1-beta gene.
The original file is found here:

http://www.ncbi.nlm.nih.gov/sites/entrez?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=1293613
"""
