
print("Hello")

# Use it as a calculator

6*3
a = 6
a*3

# Vectors

a = c(1,3,4,7)
a
a[2]

# Read files

data = read.table("genes.csv")
head(data)
data = read.table("genes.csv",header=TRUE)
head(data)
data$C1
data$C1[1:5]

# Easy plots

c1 = data$C1
c2 = data$C2
hist(c1)
hist(c1,col="gold",breaks=100)
plot(c1 ~ c2)

# Easy statistics (regression)

model = lm(c1 ~ c2)
model
abline(model,col="red")
