def validarBin(a):
    try:
        int(str(a),2)
        return True
    except ValueError:
        return False

def validarOct(a):
    try:
        int(str(a),8)
        return True
    except ValueError:
        return False

def validarDec(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def validarHex(a):
    try:
        int(str(a),16)
        return True
    except ValueError:
        return False
