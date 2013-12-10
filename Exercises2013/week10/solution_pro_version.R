setwd("C:/YOURDIRECTORY") ##set to your local directory

#load the annotation data
annot=read.table("chrVII_UCSC.txt", header=TRUE)
head(annot)

#load the expression data into a single "list" object called "data"
all.samples = list.files(path="GSE25107_chrVII/", pattern="*.wig") #first get all the wiggle filenames in the directory
paths=paste("GSE25107_chrVII/", all.samples, sep="")
sample.names=gsub(".chrVII.wig", "", all.samples) ## strip the ".chrVII.wig" part of the filename
nsamples = length(all.samples)

data=list() ##create an empty list in which all the data will be loaded

for (i in 1:nsamples) {
  data[[i]]=read.table(paths[i], skip=2, header=FALSE)
  names(data)[i] = sample.names[i]
  names(data[[i]])  = c("coord","reads")
}


## to replicate figure 1.b in the paper, need three panels: one for the gene structure, one for the RNA-seq data, and one for the NET-seq data
## get information about RPL30 (YGL030W)
gene.name="YGL030W"
RPL30.coords=annot[annot[,2]==gene.name,]
RPL30.length=RPL30.coords$txEnd-RPL30.coords$txStart
## extract the locus data from two datasets: WT_mRNA_plus and WT_NC_plus
RPL30.mRNA=data$WT_mRNA_plus[data$WT_mRNA_plus[,1]>=RPL30.coords$txStart & data$WT_mRNA_plus[,1]<=RPL30.coords$txEnd,]
RPL30.NET=data$WT_NC_plus[data$WT_NC_plus[,1]>=RPL30.coords$txStart & data$WT_NC_plus[,1]<=RPL30.coords$txEnd,]
par(mfcol=c(3,1))
# Add gene structure plot
RPL30.exonStarts=as.numeric(unlist(strsplit(as.character(RPL30.coords$exonStarts),",")))
RPL30.exonEnds=as.numeric(unlist(strsplit(as.character(RPL30.coords$exonEnds),",")))
RPL30.struct=rep(0,RPL30.length) #set 0 for introns
for (i in 1:length(RPL30.exonStarts)){
  RPL30.struct[(RPL30.exonStarts[i]-RPL30.coords$txStart):(RPL30.exonEnds[i]-RPL30.coords$txStart)]=1
}
plot(RPL30.struct, type="l", ylim=c(-1,1), col="white", yaxt="n", xaxt="n", xlab=gene.name, ylab="", bty="n")
segments(x0=1:length(RPL30.struct), y0=0, x1=1:length(RPL30.struct), y1=RPL30.struct, lwd=4, col="darkgreen")
segments(x0=1:length(RPL30.struct), y0=0, x1=1:length(RPL30.struct), y1=-RPL30.struct, lwd=4, col="darkgreen")

# plot Nascent RNA data
plot(RPL30.NET$coord, RPL30.NET$reads, type="p", xlim=c(RPL30.coords$txStart, RPL30.coords$txEnd), col="white", xlab="Nascent RNA", ylab="reads per 10e7 sequences")
segments(x0=RPL30.NET$coord, y0=0, x1=RPL30.NET$coord, y1=RPL30.NET$reads, col="red")
# plot Mature RNA data
plot(RPL30.mRNA$coord, RPL30.mRNA$reads, type="p", xlim=c(RPL30.coords$txStart, RPL30.coords$txEnd), col="white", xlab="Fragmented mature RNA", ylab="reads per 10e7 sequences")
segments(x0=RPL30.mRNA$coord, y0=0, x1=RPL30.mRNA$coord, y1=RPL30.mRNA$reads, col="blue")


# to replicate figure 3b in the paper
# for each annotated gene on chromosome VII, calculate two values: the antisense/sense ratio in rco1 mutant and the antisense/sense ratio in the WT
# refer to the methods section for how they defined sense and antisense transcription levels
par(mfcol=c(1,1))
saTable=data.frame(gene=character(), WT=numeric(), RCO1=numeric())
for (i in 1:nrow(annot)){
    TSS=annot$txStart[i]
    strand=annot$strand[i]
    gene.name=as.character(annot$name[i])
    # for the sense transcription levels, we need to compute sum of the read densities in area spanning the TSS until 500bp downstream
    # this is simpler than the paper, where they make 500 bp windows and choose the window with the maximum level
    # here, we calculate the values in fixed windows: TSS to TSS+500 for the sense, and TSS-900 to TSS-400
    if (strand=="+"){
      
      WT.sense.level=sum(data$WT_NC_plus[data$WT_NC_plus[,1]>=TSS & data$WT_NC_plus[,1]<=TSS+500,2]) + 1
      WT.antisense.level=sum(data$WT_NC_minus[data$WT_NC_minus[,1]<=TSS-400 & data$WT_NC_minus[,1]>=TSS-900,2]) + 1
      RCO1.sense.level=sum(data$RCO1D_plus[data$RCO1D_plus[,1]>=TSS & data$RCO1D_plus[,1]<=TSS+500,2]) + 1
      RCO1.antisense.level=sum(data$RCO1D_minus[data$RCO1D_minus[,1]<=TSS-400 & data$RCO1D_minus[,1]>=TSS-900,2]) + 1
    
    }else if(strand=="-"){
      
      WT.sense.level=sum(data$WT_NC_minus[data$WT_NC_minus[,1]<=TSS & data$WT_NC_minus[,1]>=TSS-500,2]) + 1
      WT.antisense.level=sum(data$WT_NC_plus[data$WT_NC_plus[,1]>=TSS+400 & data$WT_NC_plus[,1]<=TSS+900,2]) + 1
      RCO1.sense.level=sum(data$RCO1D_minus[data$RCO1D_minus[,1]<=TSS & data$RCO1D_minus[,1]>=TSS-500,2]) + 1
      RCO1.antisense.level=sum(data$RCO1D_plus[data$RCO1D_plus[,1]>=TSS+400 & data$RCO1D_plus[,1]<=TSS+900,2]) + 1
            
    }
    WT.antisense.sense=log10(WT.antisense.level/WT.sense.level)
    RCO1.antisense.sense=log10(RCO1.antisense.level/RCO1.sense.level)
    toADD=data.frame(gene=gene.name,WT=WT.antisense.sense, RCO1=RCO1.antisense.sense)
    saTable=rbind(saTable, toADD)
    
}

# plot the ratios
plot(saTable$WT,saTable$RCO1, col="blue", xlab="WT antisense/sense (log10)", ylab="RCO1D antisense/sense (log10)", pch=16)
abline(a=0, b=1)
