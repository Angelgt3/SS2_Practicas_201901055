from App.sqlserver import conectar_sql_server
from App.informacion import extraerInformacion, cargarInformacion
from App.consultas import mostrarMenuConsultas
from App.modelos import eliminarModelo, crearModelo
import pyodbc
import os


def mostrarMenu():
    db=conectar_sql_server()
    if db is None:
        return
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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
                eliminarModelo(db)
            elif opcion == 2:
                crearModelo(db)
            elif opcion == 3:
                extraerInformacion(db)
            elif opcion == 4:
                cargarInformacion(db)
            elif opcion == 5:
                mostrarMenuConsultas(db)
            elif opcion == 6:
                print("Bye :D")
                break  
            else:
                print("Opción inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        input("Presiona cualquier tecla para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
