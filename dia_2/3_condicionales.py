numero1 = 40
numero2 = 60

if numero1 > numero2:
    # si la condición se cumple
    print('En efecto, se debe agregar a la bd')
elif numero1 == numero2:
    print('No debemos hacer nada')
else:
    # si la condicion no se cumple
    print('Debemos solicitar los registros')

numero_ventas = 10

if numero_ventas > 50:
    print('dscto de 20%')
elif numero_ventas >30:
    print('dscto de 10%')
elif numero_ventas > 20:
    print('dscto de 5%')
else:
    print('dscto de 2%')

# crear una funcion, donde se reciba el nombre del alumno y la nota
# Si la nota es entre 20 y 18, recibe una felicitación pública
# Si la nota es entre 15 y 17, el alumno está aprobado y exonerado de la exposición final
# Si la nota es entre 11 y 14, el alumno está aprobado
# si la nota es menor o igual que 10 entonces el alumno esta jalado

# al final retornar un mensaje diciendo 'El alumno EDUARDO esta 'aprobado y exonerado de la exposicion final' > 15 y 17
# deadline Miercoles 20/11 18:59:59:59