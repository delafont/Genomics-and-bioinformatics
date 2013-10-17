
#-----------------------#
# Question 1.3 - Python #
#-----------------------#

# These functions are not included by default, so you have to import them:
from math import sqrt,log
from matplotlib.pyplot import plot,show

f = open("genes_expression_100.txt","r")  #open input file in 'read' mode
g = open("output_py.txt","w")             #open output file in 'write' mode (create)
header = f.readline()                     #to skip this header line
g.write("Gene_name \t Ratio \t Mean \n")  #add a header to the output

for l in f:                               #for each line in the file
    name, c1, c2 = l.split()              #extract elements in the line (strings)
    c1 = float(c1); c2 = float(c2)        #convert to floating point numbers
    if c1*c2 != 0:                        #if none of them is zero
        ratio = log(c1/c2, 2)
        mean = log(sqrt(c1*c2), 10)
        plot(mean,ratio,"o")              #draw the point
        g.write(name + '\t' + str(ratio) + '\t' + str(mean) + '\n')

f.close(); g.close()                      #don't forget to close files!
show()                                    #don't forget to display the figure
