print 'hello'

print 9/4
print type(9)
print type(9.0)
print type('9')
print 9.0/4
#print '9'/4
#print 9/0

a = 6
print 23*a+6
a = [1,2,3,4,7]
print a[2]
a = [0,'a','b','7',7]
print a[2]

print range(5)

for i in range(5):
    print 'next:', i+3

smile = ':)'
print smile
if smile == ':)':
    print 'True!'
else:
    print 'False!'

for i in range(10):
    if i%2 == 0:     # (mod 2)
        print i

f = open('genes.csv')
print f.readline()
print f.readline()
l = f.readline()
pieces = l.split()
print pieces[1] , pieces[2]
print pieces[1] + pieces[2]
print type(pieces[1])
print float(pieces[1]) + float(pieces[2])
f.close()

f = open('genes.csv')
f.readline()
for line in f:
    l = line.split()
    print float(l[1])*float(l[2])
f.close()

