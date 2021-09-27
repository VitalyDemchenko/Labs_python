import math

def f(x):
    return  4.5*x**4 - 4*x**3 + 1.5*x**2 - 2*x - 7
    
    
def df(x):
    return 18*x**3 - 12*x**2 + 3*x - 2
    
def df2(x):
    return 54*x**2 - 24*x + 3
    
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
        
        
    '''    while condition :
        xip1 = xi - ((xi - x0)/(f(xi)-f(x0)))*f(xi)
        xi = xip1
        condition = abs(xip1 - xi) > e '''
        
    xk = xip1
    #f(xk)
    return xk 
print(metod(1, 2, 0.0001))
print('x: ' + str(metod(1, 2, 0.0001)))
xk2 = metod(1, 2, 0.0001)
print ('f(x): ' + str(f(xk2)))