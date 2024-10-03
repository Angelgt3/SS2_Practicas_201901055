import pyodbc

def conectar_sql_server():
    try:
        conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=Localhost\SQLEXPRESS;'
            'DATABASE=SEMI2_practica1;'
            'UID=admin;'
            'PWD=201901055'
        )
        print("Conexión exitosa a SQL Server.")
        return conexion
    except pyodbc.Error as e:
        print("Error al conectar a SQL Server:")
        print(e.args)
        return None
