# snake case
nombre_completo = 'Farit Enrique Espinoza Tuesta'

# camelCase
nombreCompleto = 'Farit Enrique Espinoza Tuesta'

# PascalCase
NombreCompleto = 'Farit Enrique Espinoza Tuesta'

# Los nombres de las variables no pueden contener caracteres especiales '@' '/' y simbolos
# nombre@completo = 'Farit Espinoza'

# Tampoco pueden comenzar con números
nombre1 = 'Farit'
n1ombre = 'Carlos'
# 1nombre = 'Eduardo'

# Al hacer suma de String, lo asume como una concatenación
# Solamente la suma se puede hacer entre String o Int o Float, no combinarlos
resultado = 'Fabiola' + 'Roberta'

print(resultado)

# Nosotros podemos acceder a los String, en base a sus posiciones
nombre = 'Pedrito'
print(nombre[3])

# solamente se puede visualizar el texto en sus posiciones MAS NO modificarlos
# inmutables (no se puede mutar o modificar)
# nombre[6] = 'a'

# Para saber la longitud del Texto
longitud = len(nombre)
print(longitud)

# Se puede sacar un sub string o sub cadena
texto = 'El día de hoy me levante y fui a marchar por mi país y de ahí me comi un pan con pejerrey'

sub_texto = texto[3:17]
print(sub_texto)
# Empieza desde el inicio hasta la posición < 17
sub_texto = texto[:17]
print(sub_texto)

sub_texto = texto[23:]
print(sub_texto)

# Si colocamos [:] haremos una copia del contenido de la variable texto
sub_texto = texto[:]
sub_texto = texto
print(sub_texto)

# NUMERICOS
resultado = 10 + 3.75
# forma para hacer más leíble un número grande con la adherencia de '-', esto solamente sirve para lectura
# Esta ayuda está disponible desde la versión 3.6 en adelante
numerazo = 1_010_101_010
print(resultado)
print(numerazo)

# Limitar el número de decimales de una división con redondeo
print("{:.4f}".format(resultado))

# Otra forma de escribir las variables
numero1, numero2, numero3 = 3, 75, 100
numero1, numero2, numero3, numero4 = 3, 'Arequipa', True, 4.5
print(numero1)
print(numero2)

# Boolean
libre = True
# En python, para hacer uso del operador '!' se tiene que utilizar el operador 'not'
print(not libre)

