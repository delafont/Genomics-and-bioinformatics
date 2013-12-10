## Demonstration of R and ggplot2
## This script creates a simple manhattan plot based on results of a Genome Wide Association study.

setwd("path to your directory here") ##set this to your local directory, where your input file and this script are
data=read.table("manhattan.data.txt", header=TRUE)

head(data, n=10) ##display the top 10 rows of the data
data[1:10, ] ##equivalent to the head function above


##convert p values to -logp
data[,4]=-log10(data[,4])
##change the name of the fourth column
colnames(data)[4]="logp"

hist(data[,"logp"], main="Distribution of -log10(p)", xlab="-log10(p)") ## plot the histogram of the -log10(p) values

##generate a new column with a series of numbers
data[,5]=1:nrow(data)


##generate a data frame for plotting
df=data.frame(ID=as.numeric(data[,1]), chr=factor(data[,2]), coord=as.numeric(data[,3]), logp=as.numeric(data[,4]), order=as.numeric(data[,5]))

##generate a new data frame with a subset of data such that -log10(p) is greater than 2
trimmed.df=df[df[,"logp"]>2,]

##load the package needed to draw the manhattan plot.
##note: you will need to install the package if you are using it for the first time
install.packages("ggplot2")  ##only do this one time
library(ggplot2) ##you have to call this every time you start a new session of R
##use the ggplot() function to map your variables to the coordinates of the points. Alpha determines the transparency of each point, and is based on logp
ggplot(trimmed.df, aes(x=order, y=logp, color=chr)) +  geom_point(aes(alpha=logp)) + ggtitle("Manhattan plot") + xlab("") + ylab("-log10(p)")