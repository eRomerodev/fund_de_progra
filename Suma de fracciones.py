from fractions import Fraction
from functools import reduce

num = int(input("¿Cuántos fracciones desea sumar? "))

def sumar_fracciones(a,b):
    return a+b

fracciones = []

for i in range(num):
    fracs = input("Ingrese la fracción: ")
    fraci = Fraction(fracs)
    fracciones.append(fraci)

sum = reduce(sumar_fracciones,fracciones)
print(f"{sum.numerator}/{sum.denominator}")