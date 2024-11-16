def saludar():
    # Declarado el funcionamiento de la función saludar
    print('Buenas Noches')
    print('Buenas Tardes')
    print('Buenos Días')

# Para ejecutar una función
saludar()
saludar()
saludar()

def saludar_bonito(nombre):
    print('Buenas Noches', nombre)

saludar_bonito('Juanita')

def saludar_complejo(titulo, nombre, saludo):
    texto = saludo + ' ' + titulo + ' ' + nombre
    print(texto)

saludar_complejo('jovencito', 'Juancito', 'Buen Fin de Semana')

# Declara una función que reciba n parametros
# args > parametros
def mostrar_alumnos(*args):
    print(args)

mostrar_alumnos('Eduardo')
mostrar_alumnos('Luis', 'Francesca', 'Juan', 'Christian', 'Javier')
mostrar_alumnos('Arnold', 10, False, 8.5, {'nombre': 'Backend'})

# Kwargs > Keyboard Arguments
# Es una función que recibirá n parámetros, PERO con la definición del nombre del parámetro
def mostrar_info(**kwargs):
    print(kwargs)

mostrar_info(nombre='Gerardo', edad=30, aprobado=False, promedio_final=9.5)

def sumar(numero1, numero2):
    return numero1 + numero2

resultado = sumar(40, 20)

print(resultado)