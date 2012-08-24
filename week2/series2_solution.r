
#--------------#
# Exercise 3.1 #
#--------------#

gtf <- read.table('chr18.gtf',header=TRUE,sep='\t') # If you forget the "sep" argument, it cuts all spaces.
exonLines <- gtf["feature"]=='exon' # The indices of all lines of type "exon".
gtf <- gtf[exonLines,] # The "exon" type lines of the original table.
colnames(gtf) # You see that you need "start" and "end".
starts <- gtf["start"]
ends <- gtf["end"]
lengths <- ends-starts
gtf["exonSize"] <- lengths # Adds a new column to the table.
hist(lengths[,1]) # [,1] because it is a dataframe. You must select the first column, which is a vector.

#--------------#
# Exercise 3.2 #
#--------------#

attributes <- read.table('chr18_attributesibutes.txt',header=TRUE,sep='\t')
exonLines <- attributes["feature"]=='exon'
attributes <- attributes[exonLines,]
geneIds <- attributes["gene_id"]
exonLengths <- attributes["end"] - attributes["start"]
differentGenes <- levels(geneIds[1,])

# 2.a)
maxIndex <- which(exonLengths[,1]==max(exonLengths)) # or: which.max(lengths[,1])
maxGene <- as.vector(geneIds[maxIndex,]) # as.vector: else it is a "factor vector"

# 2.c)
maxNrOfExons <- 0
for (g in differentGenes) {
    l = length(which(attributes["gene_id"]==g))
    if (l > maxNrOfExons) {
        maxNrOfExons <- l
        maxGene <- g
        }
    }
maxGene

# 3. Intron-less genes are genes with only one exon
for (g in differentGenes) {
    exonIndexes = which(attributes["gene_id"][,1]==g)
    if (length(exonIndexes)==1) print(g)
    }

#--------------#
# Exercise 3.3 #
#--------------#

pyresult <- read.table("result.py")
plot(pyresult$V1, pyresult$V3, type="l", ) # Plot Column1 or Column2 (Start/End) against Column3 (GC%)
