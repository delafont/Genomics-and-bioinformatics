# Question 2.1 #
bases = ["t", "c", "a", "g"]
codons = [x+y+z for x in bases for y in bases for z in bases]

# Question 2.2 #
aminos = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codon_to_amino = dict(zip(codons, aminos))

# Add some nice colors (optional) #
codon_to_amino['aug'] = '\033[42mM\033[0m'
codon_to_amino['uaa'] = '\033[41m*\033[0m'
codon_to_amino['uag'] = '\033[41m*\033[0m'
codon_to_amino['uga'] = '\033[41m*\033[0m'

# Question 2.3 #
def seq_to_prot(seq):
    prot = ''
    for i in xrange(0, len(seq), 3):
        codon = seq[i:i+3]
        amino = codon_to_amino[codon]
        prot += amino
    return prot

# Question 2.4 #
seqence = open("sequence.fa", "r").read().strip()
for i in [0,1,2]: print seq_to_prot[i:]
