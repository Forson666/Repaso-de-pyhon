def potencia(a,b):
	if b == 1:
		return a
	else:
		return a*potencia(a,b-1)