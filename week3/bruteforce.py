# edges = [('AATGT','ATGT','ATGTC'), ('ATGTC','GTC','GTCGA'), ('GTCGA','CGA','CGATT')]
# This program finds AATGTCGATT

def bruteforce(edges):
    # Generate all possiblities #
    from itertools import permutations
    combinations = permutations(range(len(edges)))
    # Initial variables #
    best_sequence = ''
    best_comb = None
    best_length = -1
    # Core loop #
    for comb in combinations:
        # Is it legal ? #
        legal = True
        for i in xrange(len(comb)-1):
            edge1 = edges[comb[i]]
            edge2 = edges[comb[i+1]]
            if edge1[1] != edge2[0]: legal = False
        if not legal: continue
        # How long is it ? #
        sequence = ''.join(edges[comb[0][0]] + [edges[i][1] for i in comb])
        comb_length = len(sequence)
        if comb_length > best_length:
            best_sequence = sequence
            best_comb     = comb
            best_length   = comb_length
    return best_sequence
