dinero = float(input('Cual es el monto de la compra?: '))
miembro = input('Eres mienmbro de la tienda?: ').strip().lower()
descuento1 = (dinero * 0.9 )
total = descuento1 - dinero
if dinero > 1000 and miembro == 'si' :
    print()
    print('*** Felicidades eres miembro de la tienda y tienes un 10% de descuento! ***')
    print(f'Monto total de la compra: {dinero}')
    print(f'Monto total con descuento premium: {descuento1}')
elif miembro == 'si' and  dinero <= 1000 :
    print()
    print('Por solo ser miembro tendras un 5% de Descuento!')
    print(f'Tu monto es de {dinero * 0.95}')
elif miembro == 'no' and dinero > 1000:
    print()
    print(f'No sos miembro, pero superaste los $1000. Tu monto total es de {dinero * 0.97} con un 3% OFF.')
    print('Te invitamos a que seas socio de nuestra marca!')
else:
    print()
    print(f'No sos miembro, ni tampoco superaste los $1000. Tu monto total es de {dinero}')
