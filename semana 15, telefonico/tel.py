def mostrar_contactos(contactos):
    if not contactos:
        print("La agenda está vacía.")
        return

    print("\nContactos guardados:")
    for nombre, numero in contactos.items():
        print(f"- {nombre}: {numero}")


def main():
    contactos = {}
    print("Bienvenido a la agenda telefónica")

    while True:
        print("\n1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            numero = input("Número telefónico: ").strip()
            if nombre and numero:
                contactos[nombre] = numero
                print(f"Contacto guardado: {nombre}: {numero}")
            else:
                print("El nombre y el número no pueden estar vacíos.")
        elif opcion == "2":
            mostrar_contactos(contactos)
        elif opcion == "3":
            nombre = input("Nombre que deseas buscar: ").strip()
            numero = contactos.get(nombre)
            if numero:
                print(f"Contacto encontrado: {nombre}: {numero}")
            else:
                print("No se encontró ese contacto.")
        elif opcion == "4":
            nombre = input("Nombre que deseas eliminar: ").strip()
            if nombre in contactos:
                del contactos[nombre]
                print(f"Contacto eliminado: {nombre}")
            else:
                print("No se encontró ese contacto.")
        elif opcion == "5":
            print("Gracias por usar la agenda telefónica.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
