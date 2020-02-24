import time

def segundos(h,m,s):
    return (h*3600) + (m*60) + s

def horasMinutosSegundos(s):
	return [(s // 3600), ((s% 3600)// 60), ((s%3600)%60)]

def cronometrar (h,m,s):
    s = segundos(h,m,s)
    tiempo = horasMinutosSegundos(s)
    print(tiempo[0], ":",tiempo[1],":",tiempo[2])
    for x in range (1,s+1):
        time.sleep(1)
        tiempo = horasMinutosSegundos(s-x)
        print(tiempo[0], ":",tiempo[1],":",tiempo[2])
