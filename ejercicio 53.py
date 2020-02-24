def esprimo(n):
	if n == 1:
		return False
	for x in range(2, n):
		if n % x == 0:
			return False
	return True
	
def primos(a,b):
	return [n for n in range(a,b+1) if esprimo(n)]