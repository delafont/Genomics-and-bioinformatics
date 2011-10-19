# Question 2.1 #
bases = ["t", "c", "a", "g"]
codons = [x+y+z for x in bases for y in bases for z in bases]

# Question 2.2 #
aminos = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codon_to_amino = dict(zip(codons, aminos))

# Question 2.3 #
def seq_to_prot(seq):
    prot = ''
    for i in xrange(0, len(seq), 3):
        prot += codon_to_amino.get(seq[i:i+3], '')
    return prot

# Question 2.4 #
raw = open("sequence_001.txt", "r").read()
sequence = raw.replace(" ","").replace("\n","")
for i in [0,1,2]: print seq_to_prot(sequence[i:])
complementary = sequence.replace("a","T").replace("t","A").replace("g","C").replace("c","G").lower()
for i in [-1,-2,-3]: print seq_to_prot(complementary[i::-1])

"""
The answer is obisously the third reading frame in the forward direction since the
other reading frames are filled with stop codons everywhere.

This example was taken from the yeast TCP1-beta gene.
The original file is found here:

http://www.ncbi.nlm.nih.gov/sites/entrez?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=1293613
"""
