import mpmath as mp

def tangent_method(f,df,a,b,epsilon):
    x = (a+b)/2
    i = 0
    max_iter = mp.ceil(mp.log((b-a)/epsilon)/mp.log(2))
    while abs(f(x)) > epsilon:
        x = x - f(x)/df(x)
        i += 1
        if i > max_iter:
            return x,i
    
    return x,i
