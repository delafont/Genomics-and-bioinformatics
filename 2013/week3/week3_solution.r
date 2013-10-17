#--------------#
# Exercise 4.1 #
#--------------#

gtf <- read.table('Caenorhabditis_elegans.WS220.64.gtf', sep='\t') # If you forget the "sep" argument, it cuts all spaces.
colnames(gtf) <- c("chromosome", "source", "feature", "start", "end", "score", "strand", "frame", "attributes")

exonLines <- which(gtf["feature"] == 'exon') # The indices of all lines of type "exon".
gtf <- gtf[exonLines, ] # The "exon" type lines of the original table.

starts <- gtf["start"]
ends <- gtf["end"]
lengths <- ends - starts
gtf["exonSize"] <- lengths # Adds a new column to the table.

hist(lengths[,1]) # [,1] because it is a dataframe. You must select the first column, which is a vector.

#--------------#
# Exercise 4.2 #
#--------------#

pyresult <- read.table("gc_per_window.txt")
plot(pyresult[,1], pyresult[,3], type="l") # Plot Column1 or Column2 (Start/End) against Column3 (GC%)
