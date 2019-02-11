from xmlConv1 import xmlConv
import math

def method1():
    path= r'D:\Application\samples\scivalAward_excel2xml\QA\001a\501100003921.xml'
    print path
    xmlConv.xmlConversion(path)
    print 'done'

def method2000():
    l=[]
    for i in range(2000,3201,1):
        if(i%7==0) and (i%5!=0):
            l.append(str(i))
    print ', '.join(l)

def factorial(x):
    k=x
    for i in range (x-1,1,-1):
       k=k*i
    print 'Factorial is :' + str(k)

def method3(x):
    l=dict()
    for i in range(1,x+1):
        l[i]=i*i
    print l

def SquareRoot(x):
    l=[]
    c=50
    h=30

    for d in x.split(","):
        l.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
    print l


if __name__ == '__main__':
    givenPath = raw_input('Please enter number:')
    #factorial(int(givenPath))
    SquareRoot(givenPath)


