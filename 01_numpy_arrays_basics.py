import numpy as np

# NumPy tiene un funcionamiento parecido a las listas de Python, pero con la diferencia de que sus arrays son homogéneos (todos los elementos son del mismo tipo) y tienen un tamaño fijo (no se puede modificar una vez creados).
list = [1, 2, 3] # Lista de Python
a = np.array(list) # Array de NumPy a partir de una lista de Python
print(list)
print(a)
print(type(list))
print(type(a))


# Definir el tipo de los elementos
c = np.array([1, 2, 3], dtype=np.float32)
print(c)
print(c.dtype)


# Valores especiales
print(type(np.nan)) # Not a Number. Para representar valores numéricos que no son números reales manteniendo el tipo de dato float para poder realizar operaciones con ellos
print(type(None)) # None. Para representar la ausencia de un valor. No es un valor numérico, por lo que no se pueden realizar operaciones matemáticas con él.
print(np.array([[1, 2, 3], [4, np.nan, 6]])) # Array con un valor NaN


# Acceso a los elementos de un array. Slice notation
a = np.array([1, 2, 3])
print(a[0]) # Primer elemento
print(a[-1]) # Último elemento
print(a[1:]) # Desde el segundo elemento hasta el final
print(a[:-1]) # Desde el primer elemento hasta el penúltimo
print(a[::-1]) # Array invertido
print(a[0:2]) # Desde el primer elemento hasta el tercero (sin incluirlo)


# Like the original list, the array is mutable
a[0] = 10
print(a)


# Two- and higher-dimensional arrays can be initialized from nested Python sequences
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b[0, 0]) # Primer elemento

c = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(c)
print(c[1, 3]) # Segunda fila, cuarta columna = 8


# Array attributes:
print(f"Dimensiones: {c.ndim}") # número de dimensiones
print(f"Shape: {c.shape}") # The shape of an array is a tuple of non-negative integers that specify the number of elements along each dimension
print(f"Numero elementos: {c.size}") # total number of elements
print(f"Tipo elementos: {c.dtype}") #  tipo de los elementos. Si no lo especificamos, NumPy intentará inferirlo


# Funciones básicas para crear arrays
print(np.zeros((2, 3))) # Array de ceros

print(np.ones((2, 3))) # Array de unos

print(np.empty(2)) # Array vacío. No inicializa los valores de los elementos. Se crea más rápido que np.zeros o np.ones, pero no se recomienda su uso si no se van a asignar valores a todos los elementos.

print(np.arange(254, 259, dtype=np.uint8)) # Array de números enteros consecutivos start = 254, stop = 259, step = 1 (por defecto) y tipo uint8 (entero sin signo de 8 bits) que termina en 258 por eso reinicia en 0 en el siguiente paso

print(np.linspace(0, 10, num=5)) # Devuelve un ndarray de NumPy con 5 elementos equidistantes entre 0 y 10

print(np.zeros(4, dtype=np.int64)) # Array de ceros de 64 bits

print(np.full((3,3), True)) # Crea una matriz de 3x3 con todos los elementos a True (bool)
print(np.full(shape=(3,2), fill_value=5)) # Crea una matriz de 3x2 con todos los elementos a 5 (int)
print(np.full((3,2), 5.0)) # Crea una matriz de 3x2 con todos los elementos a 5.0
print(np.full((3,2), 5, dtype=np.float64)) # Crea una matriz de 3x2 con todos los elementos a 5.0

print(np.eye(3)) # Matriz identidad de 3x3


# Numeros aleatorios
rng = np.random.default_rng() # Creamos un generador de números aleatorios de NumPy
                                # default_rng: Es la forma recomendada desde NumPy 1.17 para generar números aleatorios, porque es más moderno y seguro que el antiguo módulo np.random
print(rng.random((3, 4))) # Crea una matriz de 3x4 con números aleatorios entre 0 y 1
print(rng.integers(5, size=(2, 4))) # Crea una matriz de 2x4 con números aleatorios entre 0 y 4rng = np.random.default_rng() # Creamos un generador de números aleatorios de NumPy
print(rng.random((3, 4))) # Crea una matriz de 3x4 con números aleatorios entre 0 y 1
print(rng.integers(5, size=(2, 4))) # Crea una matriz de 2x4 con números aleatorios entre 0 y 4


# Create an array from existing data
a1 = np.array([[1, 1],
               [2, 2]])
a2 = np.array([[3, 3],
               [4, 4]])
print(np.concatenate((a1, a2))) # Concatenar por filas
print(np.concatenate((a1, a2), axis=1)) # Concatenar por columnas
print(np.vstack((a1, a2))) # Stack arrays in sequence vertically (row wise)
print(np.hstack((a1, a2))) # Stack arrays in sequence horizontally (column wise)


# Filtrado
arr = np.array([1, 2, 3, 4])
print(arr)
x = [True, False, True, False] 
array_filtrado = arr[x] # Filtramos los elementos de arr que están en las posiciones True de x
print(array_filtrado)

a = np.arange(11)**2
print(a)
print(a[a<10]) # Nos quedamos con los valores menores a 10
print(a[a==16]) # Nos quedamos con los valores iguales a 16
print(a[a!=16]) # Nos quedamos con los valores distintos a 16
print(a[(a>20) | (a<50)]) # Nos quedamos con los valores mayores a 20 o menores a 50
print(a[(a>20) & (a<50)]) # Nos quedamos con los valores mayores a 20 y menores a 50

 
#Unique values and counts
data = np.array(['a', 'b', 'b', 'c', 'a'])
print(np.unique(data)) # ['a' 'b' 'c']
print(np.unique(data, return_counts=True)) # (array(['a', 'b', 'c'], dtype='<U1'), array([2, 2, 1]))
unique_values, counts = np.unique(data, return_counts=True)
print(unique_values, counts) # ['a' 'b' 'c'] [2 2 1]


# Sorting. np.sort() devuelve una copia del array ordenado, mientras que sort() modifica el array original
#np.sort() => procedimientos
#sort() => métodos programación orientada a objetos
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr)) # [1 2 3 4 5 6 7 8]
print(arr) # [2 1 5 3 7 4 6 8] El array original no se modifica

arr2 = np.array([2, 1, 5, 3, 7, 4, 6, 8])
arr2.sort()
print(arr2) # [1 2 3 4 5 6 7 8] El array original se modifica


# Adding, removing, and sorting elements
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
arr_copy = np.copy(arr) # Copia del array
print(arr_copy)
arr[0] = 0 # Modificar el array original no afecta a la copia
print(arr)
print(arr_copy)


# Transposing and reshaping a matrix
data = np.array([[1, 2], [3, 4], [5, 6]])
print(data.T) # Transpuesta
print(data.reshape(2, 3)) # Cambio de forma
print(data.reshape(6, 1)) # Cambio de forma

# Reshape
a = np.arange(6).reshape((3, 2))
print(a)
print(a.reshape(2, 3))


# Flip  an array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.flip(a)) # Flip the entries in each row in the left/right direction
print(np.flip(a, axis=0)) # Flip the entries in each column in the up/down direction


# Flatten, ravel, and squeeze
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.flatten()) # Flatten the array to a 1D array (row-major order) (copy) 
print(a.ravel()) # Return a contiguous flattened array. It does not create a copy, it’s memory efficient and any modifications to the array will be reflected in the original array
print(a.ravel().shape) # (6,) 1D array
print(a.ravel().reshape(2, 3)) # Reshape the array


# Splitting an array
a = np.array([1, 2, 3, 99, 99, 3, 2, 1])
print(np.split(a, [3, 5])) # Split the array at positions 3 and 5
print(np.split(a, 4)) # Split the array into 4 sub-arrays
