from bisection import bisection
from tangent_method import tangent_method
from secants_method import secants_method
from hybrid import hybrid
import mpmath as mp

def f1(x):
    return mp.cos(x)*mp.cosh(x) - 1

def df1(x):
    return mp.cos(x)*mp.sinh(x) - mp.sin(x)*mp.cosh(x)

def f2(x):
    if x == 0:
        return +float('inf')
    return 1/x - mp.tan(x)

def df2(x):
    return -1/(x**2) - 1/(mp.cos(x)**2)

def f3(x):
    return mp.power(2, -x) + mp.exp(x) + 2*mp.cos(x) - 6

def df3(x):
    return mp.exp(x) - mp.power(2, -x)*mp.log(2) - 2*mp.sin(x)





print("Bisection:")
print("For 1e-7:")
print(bisection(f1, 3/2*mp.pi, 2*mp.pi, 1e-7))
print(bisection(f2, 0, mp.pi/2, 1e-7))
print(bisection(f3, 1, 3, 1e-7))

print("For 1e-15:")
print(bisection(f1, 3/2*mp.pi, 2*mp.pi, 1e-15))
print(bisection(f2, 0, mp.pi/2, 1e-15))
print(bisection(f3, 1, 3, 1e-15))


print("For 1e-33:")
print(bisection(f1, 3/2*mp.pi, 2*mp.pi, 1e-33))
print(bisection(f2, 0, mp.pi/2, 1e-33))
print(bisection(f3, 1, 3, 1e-33))


print("Tangent method:")
print("Dla 1e-7:")
print(tangent_method(f1,df1,3/2*mp.pi,2*mp.pi,1e-7))
print(tangent_method(f2,df2,0,mp.pi/2,1e-7))
print(tangent_method(f3,df3,1,3,1e-7))


print("Dla 1e-15:")
print(tangent_method(f1,df1,3/2*mp.pi,2*mp.pi,1e-15))
print(tangent_method(f2,df2,0,mp.pi/2,1e-15))
print(tangent_method(f3,df3,1,3,1e-15))

print("Dla 1e-33:")
print(tangent_method(f1,df1,3/2*mp.pi,2*mp.pi,1e-33))
print(tangent_method(f2,df2,0,mp.pi/2,1e-33))
print(tangent_method(f3,df3,1,3,1e-33))



print("Secants method:")
print("Dla 1e-7:")
print(secants_method(f1, 3/2*mp.pi, 2*mp.pi, 1e-7))
print(secants_method(f2, 0, mp.pi/2, 1e-7))
print(secants_method(f3, 1, 3, 1e-7))

print("Dla 1e-15:")
print(secants_method(f1, 3/2*mp.pi, 2*mp.pi, 1e-15))
print(secants_method(f2, 0, mp.pi/2, 1e-15))
print(secants_method(f3, 1, 3, 1e-15))

print("Dla 1e-33:")
print(secants_method(f1, 3/2*mp.pi, 2*mp.pi, 1e-33))
print(secants_method(f2, 0, mp.pi/2, 1e-33))
print(secants_method(f3, 1, 3, 1e-33))



print("HYBRID")
print(hybrid(f2, 0, mp.pi/2, 1e-33))
