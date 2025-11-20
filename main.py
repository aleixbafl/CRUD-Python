# Programa principal para un CRUD con un archivo CSV y además de guardar datos en una base de datos MySQL.

# Menú principal
def menuPrincipal():
    print("Opciones del menú principal:")
    print("1. Acceder al CRUD")
    print("2. Guardar datos en una BD MySQL.")
    print("3. Salir.")

# Menú CRUD
def menuCRUD():
    print("Opciones del CRUD:")
    print("1. Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Borrar")
    print("5. Volver al menú principal")

# Función para obtener un número entero con manejo de errores
def obtenerNumInt(mensaje):
    incorrecto = True
    num = 0
    while incorrecto:
        try:
            num = int(input(mensaje))
            incorrecto = False
        except ValueError:
            print("Error: Debes ingresar un número entero.")
    return num

# Función principal
def main():
    print("Bienvenidos al CRUD hecho con python.")
    menuPrincipal()
    opcion = 0
    while opcion != 3: # Mientras no se seleccione salir (3) del menú principal se seguirá ejecutando
        opcion = obtenerNumInt("->Selecciona una opción del menú principal: ")
        print(opcion)
        if opcion == 1:
            menuCRUD()
            crud_opcion = 0
            while crud_opcion != 5:
                crud_opcion = obtenerNumInt("Selecciona una opción del CRUD: ")
                if crud_opcion == 1:
                    print("Crear operación seleccionada.")
                elif crud_opcion == 2:
                    print("Leer operación seleccionada.")
                elif crud_opcion == 3:
                    print("Actualizar operación seleccionada.")
                elif crud_opcion == 4:
                    print("Borrar operación seleccionada.")
                elif crud_opcion == 5:
                    print("Volviendo al menú principal.")
                else:
                    print("Opción inválida en el CRUD. Intenta de nuevo.")
            menuPrincipal()
        elif opcion == 2:
            print("Guardar datos en una BD MySQL seleccionado.")
        elif opcion == 3:
            print("\nSaliendo del programa. ¡Hasta luego!")
        else:
            print("Opción inválida en el menú principal. Intenta de nuevo.")

if __name__ == "__main__":
    main()