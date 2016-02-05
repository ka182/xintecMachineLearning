import numpy as np
from sklearn.naive_bayes import GaussianNB

data = open('alarms1.txt')

count = 0

X1=[]
Y1=[]

for line in data:
    xx,yy,y = line.split(',')
    X1 = "%s,[%s,%s]" % (X1,xx,yy)
    Y1 = "%s,%s" % (Y1,y.strip())
print(Y1)



