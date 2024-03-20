import string

def contar_palabras(cadena):
    # Eliminar signos de puntuación y convertir a minúsculas
    cadena = cadena.translate(str.maketrans('', '', string.punctuation)).lower()
    palabras = cadena.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def main():
    texto = input("Ingrese una cadena de texto: ")
    resultado = contar_palabras(texto)
    print("Conteo de palabras:")
    for palabra, cantidad in resultado.items():
        print(f"{palabra}: {cantidad}")

main()
