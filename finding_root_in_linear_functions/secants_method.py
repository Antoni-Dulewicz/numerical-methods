import mpmath as mp

def secants_method(f,a,b,epsilon):
    i = 0
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