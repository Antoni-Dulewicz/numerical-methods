import mpmath as mp


def bisection(f, a, b, epsilon):

    max_iter = mp.ceil(mp.log((b-a)/epsilon)/mp.log(2))

    for i in range(int(max_iter)):
        c = a + (b-a)/2
        if abs(f(c)) < epsilon:
            return c,i
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return a + (b-a)/2,i

    