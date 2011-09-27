
## Exercise 4.1
gtf <- read.table('chr18.gtf',header=TRUE,sep='\t') # If you forget the "sep" argument, it cuts all spaces.
exon.lines <- gtf["feature"]=='exon' # The indices of all lines of type "exon".
gtf <- gtf[exon.lines,] # The "exon" type lines of the original table.
colnames(gtf) # You see that you need "start" and "end".
starts = gtf["start"]
ends = gtf["end"]
lengths = ends-starts
gtf["exonSize"] <- lengths # Adds a new column to the table.
hist(lengths[,1])

## Exercise 4.2



