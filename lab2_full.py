import math

# Метод половинного ділення

def f(x):
    f = 4.5*x**4 - 4*x**3 + 1.5*x**2 - 2*x - 7
    return f 
print('  ')
print(' Метод половинного ділення ')
print('  ')
print(' x =  ')
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

def df(x):
    return 18*x**3 - 12*x**2 + 3*x - 2
    
def df2(x):
    return 54*x**2 - 24*x + 3

print('  ')
print(' Метод хорд ')
print('  ')

def metod(a,b,e):
    if (f(a)*df2(a)) > 0 :
        x0 = a 
        xi1 = b 
    else:
        x0 = b 
        xi1 = a 
    #xip1 = xi1
    xi = xi1
    x02 = x0
    xip1 = xi - ((xi - x02)/(f(xi)-f(x02)))*f(xi)
    xi = xip1
    while abs(xip1 - xi) > e :
        xip1 = xi - ((xi - x02)/(f(xi)-f(x02)))*f(xi)
        xi = xip1
        
        
    
        
    xk = xip1
    #f(xk)
    return xk 
print(metod(1, 2, 0.0001))
print('x: ' + str(metod(1, 2, 0.0001)))
xk2 = metod(1, 2, 0.0001)
print ('f(x): ' + str(f(xk2)))