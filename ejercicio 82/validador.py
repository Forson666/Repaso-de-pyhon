from modulo import *

def validar(a,b):
    if b == 2:
        if validarBin(a):
            return "El número es binario"
        else:
            return "El número no es binario"
    elif b == 8:
        if validarOct(a):
            return "El número esta en base octal"
        else:
            return "El número no esta en base octal"
    elif b == 10:
        if validarDec(a):
            return "El número esta en base decimal"
        else:
            return "El número no esta en base decimal"
    elif b == 16:
        if validarHex(a):
            return "El número esta en base hexadecimal"
        else:
            return "El número no esta en base hexadecimal"
    else:
        return "base no valida"