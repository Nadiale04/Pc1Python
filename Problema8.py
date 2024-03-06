horaingresada=input('Ingrese la hora: ')
hora_minutos=horaingresada.split(':')
hora=float(hora_minutos[0])
if hora>=7 and hora<=8:
    print('¡Es hora del desayuno!') 
elif hora>=12 and hora<=13:
    print('¡Es hora del almuerzo!')
elif hora>=18 and hora<=19:
    print('¡Es hora de la cena!')