def gestion_agenda():
    agenda = {}
    while True:
        print("\n1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            agenda[nombre] = telefono
            print(f"Contacto {nombre} agregado con éxito.")
        elif opcion == '2':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            if nombre in agenda:
                print(f"Nombre: {nombre}, Teléfono: {agenda[nombre]}")
            else:
                print(f"Contacto {nombre} no encontrado en la agenda.")
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"Contacto {nombre} eliminado.")
            else:
                print(f"Contacto {nombre} no encontrado en la agenda.")
        elif opcion == '4':
            print("Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

gestion_agenda()
