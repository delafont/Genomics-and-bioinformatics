
## Exercise 4.1
gtf <- read.table('chr18.gtf',header=TRUE,sep='\t') # If you forget the "sep" argument, it cuts all spaces.
exonLines <- gtf["feature"]=='exon' # The indices of all lines of type "exon".
gtf <- gtf[exonLines,] # The "exon" type lines of the original table.
colnames(gtf) # You see that you need "start" and "end".
starts <- gtf["start"]
ends <- gtf["end"]
lengths <- ends-starts
gtf["exonSize"] <- lengths # Adds a new column to the table.
hist(lengths[,1]) # [,1] because it is a dataframe. You must select the first column, which is a vector.


## Exercise 4.2
attr <- read.table('chr18_attributes.txt',header=TRUE,sep='\t')
exonLines <- attr["feature"]=='exon'
attr <- attr[exonLines,]
geneIds <- attr["gene_id"]
exonLengths <- attr["end"] - attr["start"]
differentGenes <- levels(geneIds[1,])
# 2.a)
maxIndex <- which(exonLengths[,1]==max(exonLengths)) # or: which.max(lengths[,1])
maxGene <- as.vector(geneIds[maxIndex,]) # as.vector: else it is a "factor vector"
# 2.c)
maxNrOfExons <- 0
for (g in differentGenes) {
    l = length(which(attr["gene_id"]==g))
    if (l > maxNrOfExons) {
        maxNrOfExons <- l
        maxGene <- g
        }
    }
maxGene
# 3. One needs to check if exons in a gene are contiguous
for (g in differentGenes) {
    exonIndexes = attr["gene_id"][,1]==g
    start <- attr["start"][,1][exonIndexes]
    end <- attr["end"][,1][exonIndexes]
    strand <- attr["strand"][,1][exonIndexes]
    end <- sort(end)
    start <- sort(start)
    diff <- start[-1] - end[-length(end)]
    if (sum(diff)==0 & length(diff)!=0) print(g)
    }


## Exercise 4.3
# Something like...
# pyresult <- read.table("result.py")
# plot(pyresult["GC_content"])
# hist(pyresult["GC_content"])
