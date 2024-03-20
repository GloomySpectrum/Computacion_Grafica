def validar_parentesis(secuencia):
    pila = []
    for caracter in secuencia:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila.pop() != '(':
                return False
    return not pila

def main():
    secuencia = input("Ingrese una secuencia de paréntesis: ")
    if validar_parentesis(secuencia):
        print("La secuencia de paréntesis es válida.")
    else:
        print("La secuencia de paréntesis no es válida.")

main()
