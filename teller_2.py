
''' ejercicio 1
import numpy as np

# Crear un array del 1 al 10
array = np.array(range(1, 11))

# Cambiar la forma del array a 2 filas y 5 columnas
array_reshape = array.reshape(2, 5)

# Imprimir las propiedades del array
print("Dimensiones:", array_reshape.ndim)
print("Forma:", array_reshape.shape)
print("Tamaño:", array_reshape.size)
'''

'''ejercicio 2
import numpy as np

# Definir dos arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

# Suma de arrays
suma = a + b

# Resta de arrays
resta = a - b

# Producto elemento a elemento
producto = a * b

# Suma de todos los elementos en a
suma_total = np.sum(a)

# Imprimir resultados
print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("Suma total de 'a':", suma_total)

'''

'''ejercicio 3
import numpy as np

# Crear un array del 1 al 10
data = np.array(range(1, 11))

# Obtener el quinto elemento (índice 4)
quinto_elemento = data[4]

# Obtener una subsección del segundo al sexto elemento (índices 1 a 5)
subseccion = data[1:6]

# Imprimir resultados
print("Quinto elemento:", quinto_elemento)
print("Subsección del segundo al sexto elemento:", subseccion)

'''

'''ejercicio 4
import numpy as np

# Crear un array A
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Sumar un escalar a A
A_suma_escalar = A + 10

# Aplicar la función raíz cuadrada a A
A_raiz_cuadrada = np.sqrt(A)

# Imprimir resultados
print("A + 10:")
print(A_suma_escalar)

print("\nnp.sqrt(A):")
print(A_raiz_cuadrada)

'''

'''ejercicio 5
import numpy as np

# Crear una matriz M
M = np.array([[1, 2, 3], [4, 5, 6]])

# Cambiar la forma de M a 3 filas y 2 columnas
M_cambiada = M.reshape(3, 2)

# Calcular el producto punto de M y su transpuesta
producto_punto = np.dot(M, M.T)

# Imprimir resultados
print("Matriz M:")
print(M)

print("\nMatriz M con forma cambiada:")
print(M_cambiada)

print("\nProducto punto de M y su transpuesta:")
print(producto_punto)

'''

'''ejercicio 6
import numpy as np

# Crear un array con datos faltantes (np.nan)
data = np.array([1, 2, np.nan, 4, 5])

# Reemplazar np.nan por 0
data_sin_nan = np.nan_to_num(data, nan=0)

# Calcular la media del array resultante
media = np.mean(data_sin_nan)

# Imprimir resultados
print("Array original:")
print(data)

print("\nArray sin np.nan:")
print(data_sin_nan)

print("\nMedia del array sin np.nan:", media)

'''

'''ejercicio 7
import numpy as np

# Crear un array
data = np.array([1, 2, 3, 4, 5])

# Guardar el array en un archivo
np.save('mi_array.npy', data)

# Cargar el array desde el archivo
data_cargada = np.load('mi_array.npy')

# Imprimir el array cargado
print("Array cargado desde 'mi_array.npy':")
print(data_cargada)

'''