consumo=float(input('Ingrese su consumo total $ '))
porcentaje_propina=float(input('Ingrese el número de porcentaje de propina igual o mayor a 15: '))
if porcentaje_propina>=15:
    propina=(porcentaje_propina*consumo)/100
    print(f'La cantidad de propina es de: {propina}')
else:
    print('¡Por favor ingrese un número mayor o igual a 15!')