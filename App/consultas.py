import pyodbc
import os

def mostrarMenuConsultas(db):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("----- Menú -----")
        print("1. Consulta 1")
        print("2. Consulta 2")
        print("3. Consulta 3")
        print("4. Consulta 4")
        print("5. Consulta 5")
        print("6. Consulta 6")
        print("7. Consulta 7")
        print("8. Consulta 8")
        print("9. Consulta 9")
        print("10. Consulta 10")
        print("11. Regresar")
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion >= 1 and opcion <=10:
                os.system('cls' if os.name == 'nt' else 'clear')
                consulta(db,opcion)
            elif opcion == 11:
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        input("Presiona cualquier tecla para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')


def consulta(db, opcion):
    try:
        cursor = db.cursor()
        ruta_sql = os.path.join('Scripts', 'Consultas', f'{opcion}.sql')
        with open(ruta_sql, 'r') as file:
            consulta_sql = file.read()
        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()
        
        for fila in resultados:
            print(fila)
        cursor.close()

    except Exception as e:
        print("Error inesperado")


