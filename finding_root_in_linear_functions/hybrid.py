import mpmath as mp 
#method which is using bisection and secants method

def hybrid(f,a,b,epsilon):
    max_iter = mp.ceil(mp.log((b-a)/epsilon)/mp.log(2))

    for i in range(2):
        c = a + (b-a)/2
        if abs(f(c)) < epsilon:
            return c,i
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    x = b
    max_iter = mp.ceil(mp.log((b-a)/epsilon)/mp.log(2))
    while abs(f(x)) > epsilon:
        x = (f(a)*b - f(b)*a)/(f(a)-f(b))
        if f(x)*f(a) > 0:
            a = x
        else:
            b = x
        i += 1
        if i > max_iter:
            return x,i

    return x,i