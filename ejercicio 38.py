def esprimo(n):
	if n == 1:
		return str(n) + " no es primo"
	for x in range(2, n):
		if n % x == 0:
			return str(n) + " no es primo"
	return str(n) + " si es primo"