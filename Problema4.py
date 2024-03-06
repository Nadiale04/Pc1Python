entero_positivo=int(input('Ingrese un número entero positivo: '))
if entero_positivo>0:
    calculo=(entero_positivo*(entero_positivo+1))/2
    print(f'La suma total es de {calculo}')
else:
    print('El número no es valido')
