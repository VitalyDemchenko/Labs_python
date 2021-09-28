import math

def f(x):
    f = 4.5*x**4 - 4*x**3 + 1.5*x**2 - 2*x - 7
    return f 

def metpol(a,b,e):
    while (math.fabs(b-a) > e):
        k = (a + b)/2.0
        if (f(a) * f(k) < 0):
            b = k 
        else:
            a = k 
    x = (a+b)/2
    print (str(x))
    return x 
f(2/3)
metpol(1,2,0.0001)