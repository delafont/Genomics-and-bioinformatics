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
        codon = seq[i:i+3]
        amino = codon_to_amino.get(codon, '')
        prot += amino
    return prot

# Add some nice colors (optional) #
codon_to_amino['atg'] = '\033[42mM\033[0m'
codon_to_amino['taa'] = '\033[41m*\033[0m'
codon_to_amino['tag'] = '\033[41m*\033[0m'
codon_to_amino['tga'] = '\033[41m*\033[0m'

# Question 2.4 #
raw = open("sequence_001.txt", "r").read()
sequence = raw.replace(" ","").replace("\n","")
for i in [0,1,2]: print seq_to_prot(sequence[i:])
for i in [-1,-2,-3]: print seq_to_prot(sequence[i::-1])

"""
The answer is obisously the third reading frame in the forward direction since the
other reading frames are filled with stop codin ons everywhere.

This example was taken from the yeast TCP1-beta gene.
The original file is found here:

http://www.ncbi.nlm.nih.gov/sites/entrez?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=1293613
"""
