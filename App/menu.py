from sqlserver import conectar_sql_server
import pyodbc


def mostrarMenu():
    while True:
        print("----- Menú -----")
        print("1. Borrar Modelo")
        print("2. Crear Modelo")
        print("3. Extraer Informacion")
        print("4. Cargar Informacion")
        print("5. Realizar Consultar")
        print("6. Salir")
        
        try:
            opcion = int(input("Selecciona una opción: "))
            
            if opcion == 1:
                print("Opcion 1")
            elif opcion == 2:
                print("Opcion 2")
            elif opcion == 3:
                print("Opcion 3")
            elif opcion == 4:
                print("Opcion 4")
            elif opcion == 5:
                print("Opcion 5")
            elif opcion == 6:
                print("Saliendo...")
                break  
            else:
                print("Opción inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
