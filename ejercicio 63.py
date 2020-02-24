def palindromo(a):
	if a == a[::-1]:
		return a + " si es un palindromo"
	else:
		return a + " no es un palindromo"