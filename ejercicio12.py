def horasMinutosSegundos(s):
	return str(s // 3600) + " horas, " + str((s% 3600)// 60) + " minutos, " + str((s%3600)%60) + " segundos"