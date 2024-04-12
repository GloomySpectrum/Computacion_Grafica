import numpy as np
import matplotlib.pyplot as plt

# Definir los colores en formato RGB
cyan = np.array([0, 1, 1])
blanco = np.array([1, 1, 1])
rojo = np.array([1, 0, 0])
magenta = np.array([1, 0, 1])
gris = np.array([0.5, 0.5, 0.5])
verde = np.array([0, 1, 0])
amarillo = np.array([1, 1, 0])
negro = np.array([0, 0, 0])
azul = np.array([0, 0, 1])

# Crear la matriz 3x3 con los colores en cada celda
matriz_colores = np.array([
    [cyan, blanco, rojo],
    [magenta, gris, verde],
    [amarillo, negro, azul]
])

# Visualizar la matriz como una imagen
plt.imshow(matriz_colores, interpolation='nearest')
plt.axis('off')
plt.show()
