import math as mt

def print_formula(d):
    c = 50
    h = 30
    Q = mt.sqrt((2*c*d)/h)
    return int(Q)

print(print_formula(150))