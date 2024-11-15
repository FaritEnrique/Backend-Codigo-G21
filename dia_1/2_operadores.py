numero1 = 20
numero2 = 40

# Aritméticos
suma = numero1 + numero2
print(suma)
resta = numero1 - numero2

multiplicacion = numero1 * numero2

division = numero1 / numero2

division_entera = numero1 // numero2
print(division_entera)
modulo = numero1 % numero2

potencia = numero1 ** numero2

resultado = (1/3)/(1/2)
""" fraccion = Fraction(resultado).limit_denominator()
print(fraccion) """

# Comparación
# Boolean > Verdadero o Falso
# = > Asignación
numero = 30
# == > Comparación
# numero == numero2
# Igual que
print(numero1 == numero2)
# Diferencte que
print(numero1 != numero2)
# Mayor que
print(numero1 > numero2)
# Menor que
print(numero1 < numero2)
# Mayor o igual que
print(numero1 >= numero2)
# Menor o igual que
print(numero1 <= numero2)

# Lógicos
# and se tiene que cumplir las dos condiciones para que todo sea verdadero
# or se tiene que cumplir una condición para que todo sea verdadero
# not Invierte el resultado de la comparación (si es V, ahora es F)
print(numero1 > numero2 and numero1 != numero2)
print(numero1 > numero2 or numero1 != numero2)
print(not numero1 > numero2)
