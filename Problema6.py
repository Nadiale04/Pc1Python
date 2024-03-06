edad=int(input('Por favor, ingrese su edad: '))
if edad<4:
    print('¡Puede entrar gratis!')
elif edad<18:
    print('¡Debe pagar $5!')
elif edad>=18:
    print('¡Debe pagar $10!')