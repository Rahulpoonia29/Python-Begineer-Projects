# from math import pi

# def fibonacci(n):
#     return ((pi**n)-((-pi)**(-n)))/(5**(1/2))
Phi = 1.6180339887498948482045868343656381177203091798057628621354486227052604628189024497072072041893911374


def fibonacci(n):
    return (((Phi) ** n) - ((-Phi) ** -n)) / ((5) ** (1 / 2))


for i in range(0, 11):
    print(f"f({i})  =  {fibonacci(i):0f}")
