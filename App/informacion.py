from datetime import datetime
import csv
import os

def extraerInformacion(db):
    RutaArchivo = input("Ingrese la ruta del archivo: ")
    
    if not os.path.isfile(RutaArchivo):
        print("El archivo no existe. Verifica la ruta e inténtalo de nuevo.")
        return

    with open(RutaArchivo, mode='r', encoding='utf-8') as archivo:
        ArchivoCSV = csv.reader(archivo)
        encabezados = next(ArchivoCSV)
        cursor = db.cursor()
        contador = 0

        for fila in ArchivoCSV:
            cursor.execute("""
                INSERT INTO DatosTemporales (PassengerID, FirstName, LastName, Gender, Age, Nationality, AirportName,
                AirportCountryCode, CountryName, AirportContinent, Continents, DepartureDate, ArrivalAirport, PilotName, FlightStatus)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, fila)
            
            contador += 1
            if contador % 5000 == 0:
                print('No. Datos:', contador)
        
        db.commit()
        print("Datos extraídos e insertados en la tabla temporal. Total:", contador)
        cursor.close() 

def TrasformarDatos(fila):
    fila = [str(elemento).strip() if elemento is not None else None for elemento in fila]
    if fila[1] is not None:
        fila[1] = fila[1].title()  # Nombre
    if fila[2] is not None:
        fila[2] = fila[2].title()  # Apellido
    if fila[3] is not None:
        fila[3] = fila[3]          # Género
    if fila[5] is not None:
        fila[5] = fila[5].title()  # Nacionalidad
    #print("fila[1]:"+fila[1])
    #print("fila[2]:"+fila[2])
    #print("fila[3]:"+fila[3])
    #print("fila[5]:"+fila[5])
    #print("fila[6]:"+fila[6])
    #print("fila[7]:"+fila[7])
    #print("fila[8]:"+fila[8])
    #print("fila[9]:"+fila[9])
    #print("fila[10]:"+fila[10])
    #print("fila[12]:"+fila[12])
    #print("fila[13]:"+fila[13])
    #print("fila[14]:"+fila[14])
    fechaSucia = fila[12]  
    if fechaSucia is not None:
        try:
            if '-' in fechaSucia:
                fecha = datetime.strptime(fechaSucia, '%m-%d-%Y')
            else:
                fecha = datetime.strptime(fechaSucia, '%m/%d/%Y')
            fila[12] = fecha.strftime('%Y-%m-%d') 
        except ValueError:
            print(f"Error al procesar la fecha: {fechaSucia}. Se asignará NULL.")
            fila[12] = None  
    return fila




def cargarInformacion(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM DatosTemporales")
    datosTemp = cursor.fetchall()
    contador = 0 
    for fila in datosTemp:
        FilaLimpia = TrasformarDatos(list(fila)) 

        #print(FilaLimpia[0], FilaLimpia[1], FilaLimpia[2], FilaLimpia[3], FilaLimpia[4], FilaLimpia[5])
        #print(FilaLimpia[6], FilaLimpia[7], FilaLimpia[8], FilaLimpia[9], FilaLimpia[10], FilaLimpia[11])
        #print(FilaLimpia[12], FilaLimpia[13], FilaLimpia[14], FilaLimpia[15])

        try:
            # Tabla pasajeros
            cursor.execute("""
                INSERT INTO Pasajeros 
                (IdPasajero, Nombre, Apellido, Genero, Edad, Nacionalidad)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (FilaLimpia[1], FilaLimpia[2], FilaLimpia[3], FilaLimpia[4], FilaLimpia[5], FilaLimpia[6]))

            # Tabla Aeropuertos
            cursor.execute("""
                INSERT INTO Aeropuertos 
                (Nombre, IdPais, Pais, IdContinente, Continente)
                VALUES (?, ?, ?, ?, ?)
            """, (FilaLimpia[7], FilaLimpia[8], FilaLimpia[9], FilaLimpia[10], FilaLimpia[11]))    

            # Tabla Detalle_Vuelo
            cursor.execute("""
                INSERT INTO Detalle_Vuelo 
                (fecha_salida, aeropuerto_llegada, piloto, Estado_vuelo)
                VALUES (?, ?, ?, ?)
            """, (FilaLimpia[12], FilaLimpia[13], FilaLimpia[14], FilaLimpia[15]))

            # Tabla Vuelos
            # Obtener el IdPasajero
            cursor.execute("SELECT IdPasajero FROM Pasajeros WHERE IdPasajero = ?", (FilaLimpia[1],))
            IdPasajero = cursor.fetchone()
            # Obtener el IdAeropuerto
            cursor.execute("SELECT IdAeropuerto FROM Aeropuertos WHERE Nombre = ?", (FilaLimpia[7],))
            IdAeropuerto = cursor.fetchone()
            # Obtener el IdDetalle_Vuelo
            cursor.execute("SELECT IdDetalle_Vuelo FROM Detalle_Vuelo WHERE fecha_salida = ?", (FilaLimpia[12],))
            IdDetalle_Vuelo = cursor.fetchone()
            if IdPasajero and IdAeropuerto and IdDetalle_Vuelo:
                cursor.execute("""
                    INSERT INTO Vuelos 
                    (IdPasajero, IdAeropuerto, IdDetalle_Vuelo)
                    VALUES (?, ?, ?)
                """, (IdPasajero[0], IdAeropuerto[0], IdDetalle_Vuelo[0]))
            else:
                print("No se pudieron obtener todos los IDs necesarios.")
        
        except pyodbc.Error as e:
            print(f"Error al insertar la fila: {FilaLimpia}. Error: {e}")
            errores += 1
        contador += 1
        if contador % 1000 == 0:
            db.commit()
            print('No. Datos:', contador)

    
    print("Datos cargados al modelo. Total:", contador)
    cursor.close()