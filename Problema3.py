#Definimos el peso de los dos productos
peso_payaso=112
peso_muneca=75
#Ingresar el número de productos
numero_payasos=int(input('Ingrese el número de payasos: '))
numero_munecas=int(input('Ingrese el número de muñecas: '))
#Calculo del paquete
peso_paquete=(numero_payasos*peso_payaso)+(numero_munecas*peso_muneca)
print(f'El peso total del paquete es de {peso_paquete} g')