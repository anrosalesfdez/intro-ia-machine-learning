import numpy as np

# Operaciones con arrays
data = np.array([1, 2])         #   [1 2]
ones = np.ones(2, dtype=int)    #   [1 1]
print(data + ones) # Sum            [2 3]
print(data - ones) # Subtraction    [0 1]
print(data * ones) # Multiplication [1 2]
print(data / data) # Division       [1. 1.]
print(data // data) # Floor division    [1 1]
print(data % data) # Modulus       [0 0]
print(data ** data) # Exponentiation [1 4]


a = np.array([1, 2, 3, 4])
print(a.sum())
b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0)) # Suma por columnas [3 3]
print(b.sum(axis=1)) # Suma por filas [2 4]

# Broadcasting
data = np.array([1.0, 2.0])
print(data * 1.6) # [1.6 3.2]   Multiplicación por un escalar

# Array operations min, max, sum, mean, std
data = np.array([1, 2, 3, 4])
print(data.min()) # 1
print(data.max()) # 4
print(data.argmaxmax()) # 3
print(data.sum()) # 10
print(data.mean()) # 2.5
print(data.cumsum()) # [ 1  3  6 10] (suma acumulada)
print(data.std()) # 1.118033988749895 (desviación estándar)
print(data.var()) # 1.25 (varianza)

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
print(a.sum()) # 4.8595784
print(a.min()) # 0.05093587
print(a.min(axis=0)) # [0.12697628 0.05093587 0.26590556 0.5510652 ] Mínimo por columnas
print(a.min(axis=1)) # [0.17296777 0.05093587 0.12697628] Mínimo por filas





