import numpy as np

# Array numpy ineficiente
# 3 listas de 4 elementos con elementos de diferentes tipos. 
# Numpy no puede crear un array homogéneo con estos datos. Convierte a todos los elementos a string.
alumnos_y_notas = np.array([['Antonio', 'Bea', 'Carlos', 'Diana'],
                            [65, 78, 90, 81],
                            [71, 82, 79, 92]]) 

#Array más eficiente.
# Cada elemento de la lista es una tupla con 3 elementos: nombre, nota1 y nota2
# dtype: definimos el tipo de los elementos. 'U10' es una cadena de texto de hasta 10 caracteres. 'i4' es un entero de 32 bits.
alumnos_y_notas = np.array([
    ('Antonio', 65, 71),
    ('Bea', 78, 82),
    ('Carlos', 90, 79),
    ('Diana', 81, 92)
], dtype=[('nombre', 'U10'), ('nota1', 'i4'), ('nota2', 'i4')])

# Promedio por alumno
promedios = (alumnos_y_notas['nota1'] + alumnos_y_notas['nota2']) / 2
print("Promedios:", promedios)

# Acceso a las notas de Carlos
notas_carlos = alumnos_y_notas[alumnos_y_notas['nombre'] == 'Carlos']
print("Notas de Carlos:", notas_carlos)


# Alternativa. usar una lista de tuplas para organizar la información es funcional en Python puro, pero no es la forma más eficiente si planeas realizar operaciones matemáticas o estadísticas, especialmente en un dataset más grande. Este formato mezcla estructuras (tuplas y listas) que pueden ser útiles para almacenar datos pero no para procesarlos eficientemente.:
alumnos_y_notas = [('Antonio', [65, 71]), ('Bea', [78, 82]), ('Carlos', [90, 79]), ('Diana', [81, 92])]
# En Python puro, para calcular el promedio de cada alumno:
for alumno, notas in alumnos_y_notas:
    print(f"{alumno}: Promedio = {sum(notas)/len(notas)}")
# En NumPy, podemos hacerlo de forma más eficiente:
alumnos_y_notas = np.array([
    ('Antonio', [65, 71]),
    ('Bea', [78, 82]),
    ('Carlos', [90, 79]),
    ('Diana', [81, 92])
], dtype=[('nombre', 'U10'), ('notas', '2i4')])
# Acceso a las notas de Carlos
notas_carlos = alumnos_y_notas[alumnos_y_notas['nombre'] == 'Carlos']['notas']
print("Notas de Carlos:", notas_carlos)
# Promedio por alumno
promedios = [np.mean(alumno['notas']) for alumno in alumnos_y_notas]
print("Promedios:", promedios)