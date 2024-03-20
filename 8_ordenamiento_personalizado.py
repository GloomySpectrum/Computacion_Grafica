def ordenamiento_personalizado(lista):
    return sorted(lista, key=lambda x: (x[1], x[0]))

def main():
    lista = [("Juan", 25), ("María", 30), ("Carlos", 20), ("Ana", 25)]
    lista_ordenada = ordenamiento_personalizado(lista)
    print("Lista ordenada:")
    for nombre, edad in lista_ordenada:
        print(f"{nombre}: {edad}")

main()
