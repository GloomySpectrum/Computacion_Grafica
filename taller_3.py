''' ejercicio 1
import numpy as np

# Crear un array unidimensional con los números del 1 al 10
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Imprimir el array
print("Array unidimensional:")
print(array)

'''

''' ejercicio 2
import numpy as np

# Crear una matriz 2D con 3 filas y 3 columnas
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Imprimir la matriz
print("Matriz 2D:")
print(matriz)

'''

''' ejercicio 3
import numpy as np

# Crear dos arrays unidimensionales con los números del 1 al 5
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 3, 4, 5])

# Sumar los dos arrays
resultado = array1 + array2

# Imprimir el resultado
print("Resultado de la suma:")
print(resultado)

'''

''' ejercicio 4
import numpy as np

# Crear un array con los números del 1 al 5
array = np.array([1, 2, 3, 4, 5])

# Calcular la exponencial de cada elemento del array
resultado = np.exp(array)

# Imprimir el nuevo array
print("Resultado de la exponencial:")
print(resultado)

'''

''' ejercicio 5
import numpy as np

# Crear un array con los números del 1 al 10
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Seleccionar los elementos pares del array
array_pares = array[array % 2 == 0]

# Imprimir el nuevo array
print("Elementos pares del array:")
print(array_pares)

'''

''' ejercicio 6
import numpy as np

# Generar un array de 10 números aleatorios entre 0 y 1
array_aleatorio = np.random.rand(10)

# Imprimir el array
print("Array de números aleatorios entre 0 y 1:")
print(array_aleatorio)

'''

''' ejercicio 7
import numpy as np

# Crear un array con los números del 1 al 5
array = np.array([1, 2, 3, 4, 5])

# Calcular la media de los elementos del array
media = np.mean(array)

# Imprimir la media
print("Media de los elementos del array:", media)

'''

''' ejercicio 8
import numpy as np

# Crear un array de 5 elementos, todos inicializados con el valor 7
array = np.full(5, 7)

# Imprimir el array
print("Array de 5 elementos con valor 7:")
print(array)

'''

''' ejercicio 9
import numpy as np

# Crear dos arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Sumar los dos arrays utilizando broadcasting
resultado = array1 + array2

# Imprimir el nuevo array
print("Resultado de la suma utilizando broadcasting:")
print(resultado)

'''

''' ejercicio 10
import numpy as np

# Crear un array con los números del 1 al 6
array = np.array([1, 2, 3, 4, 5, 6])

# Cambiar la forma del array a una matriz 2x3
matriz = array.reshape(2, 3)

# Imprimir la matriz
print("Matriz 2x3:")
print(matriz)

'''

