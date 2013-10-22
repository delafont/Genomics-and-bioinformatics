#--------------#
# Question 2.1 #
#--------------#

bases = ['t','c','a','g']

# Solution 1:
codons = []
for x in bases:
    for y in bases:
        for z in bases:
            codons.append(x+y+z)

# Solution 2 ("list comprehension"):
codons = [x+y+z for x in bases for y in bases for z in bases]

#--------------#
# Question 2.2 #
#--------------#

# Solution 0 (manually):
codon_to_amino = {}
codon_to_amino['TTT'] = 'F'
codon_to_amino['TTC'] = 'F'
# ...

# Solution 1:
aminos = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codon_to_amino = {}
for i in range(len(codons)):
    codon_to_amino[codons[i]] = aminos[i]

# Solution 2:
aminos = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codon_to_amino = dict(zip(codons, aminos))

#--------------#
# Question 2.3 #
#--------------#

def translate(seq):
    """Translates a nucleotide sequence *seq* into an aminoacid sequence."""
    translation = [codon_to_amino[seq[i:i+3]] for i in range(0,len(seq),3)]
    return ''.join(translation) # transforms the list into a string. str([1,2,3]) won't work directly.

#--------------#
# Question 2.4 #
#--------------#

def complementary(seq):
    """Return the reverse complement of a given sequence *seq*."""
    compl = []
    for letter in seq:
        letter = letter.lower() # lower case
        if letter == "a":
            compl.append("t")
        elif letter == "c":
            compl.append("g")
        elif letter == "g":
            compl.append("c")
        elif letter == "t":
            compl.append("a")
    return ''.join(reversed(compl))

def cut(seq):
    """Cut the end of sequence *seq* so that its length is a multiple of three."""
    if len(seq)%3 == 0:
        sequence = seq
    elif len(seq)%3 == 1:
        sequence = seq[:-1] # up to last element, excluded
    elif len(seq)%3 == 2:
        sequence = seq[:-2]
    return sequence

#f = open('sequence_ex2.fasta', 'r') # Exercise 2
f = open('fragment_007.fasta', 'r') # Exercise 3
f.readline() # skip header
raw = f.read()
raw = raw.lower() # small letters only
sequence = raw.replace('\n','').replace(' ','') # remove spaces and newlines
complement = complementary(sequence)

for i in [0,1,2]:
    seq = cut(sequence[i:])
    print "\nForward strand, shift " + str(i) + ":\n" + translate(seq)
for i in [0,1,2]:
    comp = cut(complement[i:])
    print "\nReverse strand, shift " + str(i) + ":\n" + translate(comp)

"""
The third reading frame in the forward direction is best since the
other reading frames are filled with stop codons.

This example was taken from the yeast TCP1-beta gene.
The original file can be found found here:

http://www.ncbi.nlm.nih.gov/sites/entrez?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=1293613
"""
