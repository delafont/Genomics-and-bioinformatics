data = read.table("annot.txt", header=TRUE, sep='\t', dec='.')
colnames(data)
start = data['txStart']
end = data['txEnd']
sizes = end-start
