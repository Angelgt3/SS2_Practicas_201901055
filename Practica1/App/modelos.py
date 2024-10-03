import pyodbc
import os

def eliminarModelo(db):
    try:
        cursor = db.cursor()
        ruta_sql = os.path.join('Scripts', 'Modelo', 'eliminarModelo.sql')
        
        with open(ruta_sql, 'r', encoding='utf-8') as file:
            eliminar_sql = file.read()
        
        cursor.execute(eliminar_sql)
        db.commit()
        print("Modelo eliminado correctamente.")
        cursor.close()
    except Exception as e:
        print("Error inesperado:", e)


def crearModelo(db):
    try:
        cursor = db.cursor()
        ruta_sql = os.path.join('Scripts', 'modelo', 'crearModelo.sql')
        
        with open(ruta_sql, 'r', encoding='utf-8') as file:
            crear_sql = file.read()
        
        cursor.execute(crear_sql)
        db.commit()
        print("Modelo creado correctamente.")
        cursor.close()
    except Exception as e:
        print("Error inesperado:", e)
