def numdias(n):
	if n == 2:
		return 28
	elif n < 8 and n % 2 == 0:
		return 30
	elif n < 8 and n % 2 != 0:
		return 31
	elif n % 2 == 0:
		return 31
	elif n % 2 != 0:
		return 30
	