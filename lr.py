import math
import Tkinter
import matplotlib.pyplot as plt
from numpy import *

def summ(p):
    n = len(p) #len(p) gets the length of the list
    x=0
    y=0
    xy=0
    x2=0
    y2=0
    for i in range(n):
        x += float(p[i][0]) #turns the value to float
        y += float(p[i][1])
        xy += float(p[i][0]*p[i][1]) 
        x2 += float(p[i][0]*p[i][0]) 
        y2 += float(p[i][1]*p[i][1]) 
    return [x, y, xy, x2, y2]


def correlation(p):
    n = len(p)
    soma = summ(p)
    x = soma[0]
    y = soma[1]
    xy = soma[2]
    x2 = soma[3]
    y2 = soma[4]

    r = ((n * xy) - (x*y)) / math.sqrt((n*x2 - x*x)*(n*y2 - y*y)) #correlation equation
    return r


def a_and_b(p):
    n = len(p)
    soma = summ(p)
    x = soma[0]
    y = soma[1]
    xy = soma[2]
    x2 = soma[3]

    a = ((n * xy) - (x*y)) / ((n*x2) - (x*x)) #Linear regression - angular coeficient
    b = ((y/n) - (a*x/n)) #Linear regression - constant
    return [a,b]


'''------MAIN------'''


def main():
    #p = [[1,3], [2,6], [3,7], [4,10], [5,10], [6,12]] #data used for test - it will be changed by a file
    #p = [[80,220], [100,180], [120,140], [140,125], [160,95]] #- another amount of data

    p = genfromtxt("data.csv", delimiter=",") #opening data file

    print ("Correlation: %f%%." %(correlation(p)*100))
    ab = a_and_b(p)
    print("m = %f \nAnd b = %f"%(ab[0], ab[1]))

    n = len(p)

    q = []
    r = []

    for i in range(n): #putting X values into q[] and Y values into r[]
        q.append(p[i][0]) 
        r.append(p[i][1])

           
    '''PLOTTING THE DATA'''


    plt.plot(q, r, 'ro') #plotting the points of the input

    s = sorted(q)

    plt.plot([s[0], s[-1]], [ab[0]*s[0] + ab[1], ab[0]*s[-1] + ab[1]]) #plotting the line found
    plt.show()

if __name__ == "__main__": #defining a main function
    main()
