horaingresada=input('Ingrese la hora: ')
hora_minutos=horaingresada.split(':')
hora=float(hora_minutos[0])
minutos=float(hora_minutos[1])
minutos=minutos/60
horatotal=hora+minutos #Para interpretarlo como decimal
if horatotal>=7 and horatotal<=8:
    print('¡Es hora del desayuno!') 
elif horatotal>=12 and horatotal<=13:
    print('¡Es hora del almuerzo!')
elif horatotal>=18 and horatotal<=19:
    print('¡Es hora de la cena!')