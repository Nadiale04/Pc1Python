primer_num=float(input('Ingrese el primer número: '))
segundo_num=float(input('Ingrese el segundo número: '))
suma=primer_num+segundo_num
resta=primer_num-segundo_num
multi=primer_num*segundo_num
operación=input('Ingrese la operación que desea realizar: ').lower().strip()
if operación=='suma':
    resultado=suma
elif operación=='resta':
    resultado=resta
elif operación=='multiplicación':
    resultado=multi
else:
    resultado='no válido'
print(f'El resultado de la {operación} es {resultado}')