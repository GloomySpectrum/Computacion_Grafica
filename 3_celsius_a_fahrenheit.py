def celsius_a_fahrenheit(grados_celsius):
    return (grados_celsius * 9/5) + 32

def main():
    try:
        temperaturas_celsius = input("Ingrese una lista de temperaturas en grados Celsius separadas por comas: ")
        temperaturas_celsius = [float(temp) for temp in temperaturas_celsius.split(",")]
        temperaturas_fahrenheit = list(map(lambda x: celsius_a_fahrenheit(x), temperaturas_celsius))
        print(f"Temperaturas en Fahrenheit: {temperaturas_fahrenheit}")
    except ValueError:
        print("Error: Ingrese temperaturas válidas separadas por comas.")

main()
