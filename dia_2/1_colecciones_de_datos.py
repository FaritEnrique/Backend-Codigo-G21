# Listas (Arreglos o Arrays)
# Ordenada y Editable
frutas = ['Manzanas', 'Platano', 'Papaya', 'Pitahaya']

# Ordenado > Cada elemento de la lista, está en una POSICIÓN determinada
print(frutas[1])
# Editable > Agregar y eliminar elmentos de la lista
frutas.append('Madarina')
frutas.append('piña')

print(len(frutas))

frutas.remove('Platano')
print(frutas)
# El método remove sólo si existe el elmento lo eliminará, sino lanzará un error
# frutas.remove('Aguaymanto')

# El método pop funciona con la POSICIÓN de la fruta
frutas.pop(0)
print(frutas)

frutas[0] = 'Kiwi'

print(frutas)

# Colocando como primer parámetro el índice donde se agregará el nuevo contenido y como segundo parámetro el contenido a agregar
frutas.insert(2, 'Uvas')
print(frutas)

# Tuplas
# No son EDITABLES una vez creada ya no se puede modificar
# Son Ordenadas
alumnos = ('Farit', 'Francesca', 'Cesar', 'Christian', 'Eddy')

print(alumnos[0])

# Otra forma de crear una lista a partir de una TUPLA, pero la Tupla original sigue siendo una Tupla que no se puede modificar
copia_alumnos = list(alumnos)
print(id(alumnos))
print(id(copia_alumnos))

copia_alumnos[0] = 'Brigit'
print(copia_alumnos)

segunda_copia = tuple(copia_alumnos)
print(id(segunda_copia))
# segunda_copia[0] = 'Pedro'

# Cuando copiamos una lista a otra variable, lo que estamos haciendo en realidad, es utilizar la misma posición de la memoria
# Ahora hago una copia del contenido y esto indica que se guarde en otra posición de memoria
otras_frutas = frutas[:]
print(id(otras_frutas))
print(id(frutas))

print(otras_frutas)

frutas[1] = 'Frutas del Dragón'
print(otras_frutas)


# Set
# Es DESORDENADA
# Es EDITABLE
inventario = {
    'Monitores',
    'Mouse',
    'Proyectores',
    'Ventiladores',
    'Teclados'
}

print(inventario)
# Esto no se puede hacer, porque no es ordenado
# print(inventario[0])

inventario.add('Memoria RAM')
inventario.remove('Mouse')
print(inventario)

print('Monitores' in inventario)
print('Laptops' in inventario)

# DICCIONARIOS
# Es ORDENADO POR LLAVES no por posición ni índice
# Editable
persona = {
    'nombre': 'Farit',
    'apellido': 'Espinoza',
    'correo': 'faritespinoza@gmail.com',
    'hobbies': ['Comer', 'Programar', 'Montar bici'],
    'direcciones': {
        'calle': 'Morona',
        'numero': 720,
        'postal': 61001,
    },
    'viudo': False,
    'familiares': ('José Tuesta', 'María Espinoza', 'Wilma Tuesta')
}

print(persona['nombre'])

# Quiero ver los hobbies de la persona
print(persona['hobbies'])
# Quiero ver cuántos hobbies tiene la persona (numeros)
print(len(persona['hobbies']))
# Quiero ver en qué calle vive la persona
print(persona['direcciones']['calle'])
# Quiero saber si es viudo o no
print(persona['viudo'])
# Quiero saber si María es Familiar
print('María Washington' in persona['familiares'])

curso = {
    'nombre': 'Backend',
    'duracion': '10 semanas',
    'fecha_inicio': '2024-11-11',
    'fecha_fin': '2025-01-30',
    'topics': ['Python', 'Express', 'Django', 'Flask'],
    'semanas': [
        {
            'nombre': 'semana 01',
            'descripcion': 'intro a python'
        },
        {
            'nombre': 'semana 02',
            'descripcion': 'base de datos'
        }
    ],
    'habilidades': ('logica de programacion', 'manejo de eventos', 'despliegue en servidores'),
    'finalizado': False,
    'profesores': {
        'Arnold Gallegos', 'Eduardo de Rivero'
    },
    'costo': 550.76,
    'descanso': 'a veces'
}

# El nombre del curso y su duracion
print(curso['nombre'], curso['duracion'])
# Cuantos topics tiene el curso
print(curso['topics'])
# Muestrame los 2 primeros topics
print(curso['topics'][0], curso['topics'][1])
# Cuantas semanas tiene el curso
print(len(curso['semanas']))
# la descripcion de la semana01
print(curso['semanas'][0]['descripcion'])
# 'manejo de eventos' es parte de las habilidades?
print('manejo de eventos' in curso['habilidades'])
# Enseñara el profesor "Juan Martinez"?
print('Juan Martinez' in curso['profesores'])
