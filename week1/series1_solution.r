
#------------------#
# Question 1.3 - R #
#------------------#

# Read the file; header=TRUE is to skip the first title line.
data = read.table("genes_expression_100.txt", header=TRUE)

names = data[,1]            #first column (vector of strings)
c1 = data[,2]               #second (vector of numbers)
c2 = data[,3]               #and third
ratios = log2(c1/c2)
means = log10(sqrt(c1*c2))
plot(ratios~means)          #draw; '~' means 'with respect to'

# One cannot write a full vector to a file, one must create a
# 'data frame' with theses vectors as columns, and write the data frame:
output = data.frame(Gene_name=names, Ratio=ratios, Mean=means)
write.table(output,"output_R.txt")
