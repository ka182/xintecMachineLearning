import numpy as np

data = open('5dAlarms.txt')

count = 0

X1=[]
Y1=[]

for line in data:
    xx,yy,zz,ww,uu,y = line.split(',')
    X1 = "%s,[%s,%s,%s,%s,%s]" % (X1,xx,yy,zz,ww,uu)
    Y1 = "%s,%s" % (Y1,y.strip())
print(Y1)


