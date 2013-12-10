# MSA_SP_score.py

PAM = open("PAM250.txt")
MSA = open("MSA.txt")

scoring_matrix = []
for line in PAM:
    scoring_matrix.append(line.strip("\n").split("\t"))

gap_penalty = -10
score = {}
score[("-","-")] = gap_penalty
for i in range(1,24):
    row = scoring_matrix[i][0]
    score[(row, "-")] = gap_penalty
    score[("-", row)] = gap_penalty
    for j in range(1,24):
        column = scoring_matrix[0][j]
        score[(row, column)] = int(scoring_matrix[i][j])
        score[(column, row)] = score[(row, column)]


alignment = []
for line in MSA:
    alignment.append(list(line.strip("\n")))

SP_score = 0
nb_sequences = len(alignment)
nb_residues = len(alignment[0])
for j in range(nb_residues):
    for i1 in range(nb_sequences):
        for i2 in range((i1+1),nb_sequences):
            SP_score += score[(alignment[i1][j], alignment[i2][j])]

print "The SP score of the MSA is ", SP_score

PAM.close()
MSA.close()
