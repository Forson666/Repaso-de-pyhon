from funciones_aritmeticas import *

def operar(a,b,c):
    if c == 1:
        return suma(a,b)
    elif c == 2:
        return resta(a,b)
    elif c == 3:
        return multiplicacion(a,b)
    elif c == 4:
        return division(a,b)
    else:
        return potencia(a,b)
