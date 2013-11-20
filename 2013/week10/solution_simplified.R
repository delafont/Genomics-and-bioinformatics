## Load the annotation data
annot = read.table("chrVII_UCSC.txt", header=TRUE)
head(annot)

## Load the expression data
# NET-seq data
net.minus = read.table("GSE25107_chrVII/WT_NC_minus.chrVII.wig", skip=2, header=FALSE, col.names=c("pos","count"))
net.plus = read.table("GSE25107_chrVII/WT_NC_plus.chrVII.wig", skip=2, header=FALSE, col.names=c("pos","count"))
# RNA-seq data
rna.minus = read.table("GSE25107_chrVII/WT_mRNA_minus.chrVII.wig", skip=2, header=FALSE, col.names=c("pos","count"))
rna.plus = read.table("GSE25107_chrVII/WT_mRNA_plus.chrVII.wig", skip=2, header=FALSE, col.names=c("pos","count"))

## To replicate figure 1.b in the paper, need two panels: one for the RNA-seq data, and one for the NET-seq data

## Get information about gene RPL30 (YGL030W)
gene.name = "YGL030W"
gene.coords = annot[annot$name == gene.name, ]
gene.start = gene.coords$txStart
gene.end = gene.coords$txEnd
gene.length = gene.end - gene.start

## Extract the locus data from two datasets: WT_mRNA_plus and WT_NC_plus
gene.net = net.plus[ (net.plus$pos >= gene.start)  &  (net.plus$pos <= gene.end) , ]
gene.rna = rna.plus[ (rna.plus$pos >= gene.start)  &  (rna.plus$pos <= gene.end) , ]

## Prepare a graph with 2 rows, 1 column
par(mfcol=c(2,1))


# Plot Nascent RNA data
plot(gene.net$pos, gene.net$count, type="p", xlim=c(gene.start,gene.end), col="white",
     xlab="Nascent RNA", ylab="reads per 10e7 sequences")
segments(x0=gene.net$pos, y0=0, x1=gene.net$pos, y1=gene.net$count , col="red")
# or : lines(gene.net$pos, gene.net$count, col="red")

# Plot Mature RNA data
plot(gene.rna$pos, gene.rna$count, type="p", xlim=c(gene.start,gene.end), col="white",
     xlab="Fragmented mature RNA", ylab="reads per 10e7 sequences")
segments(x0=gene.rna$pos, y0=0, x1=gene.rna$pos, y1=gene.rna$count , col="blue")
# or : lines(gene.rna$pos, gene.rna$count, col="blue")


