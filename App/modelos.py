import pyodbc

def CrearModelo(db,opcion):
    try:
        cursor = db.cursor()
        with open(opcion+'.sql', 'r') as file:
            consulta_sql = file.read()
        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila)
        cursor.close()
    except pyodbc.Error as e:
        print("Error al ejecutar la consulta")
