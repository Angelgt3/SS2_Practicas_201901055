import csv
import os

def extraerInformacion(db):
    ruta_archivo = input("Ingrese la ruta del archivo: ")
    
    if not os.path.isfile(ruta_archivo):
        print("El archivo no existe. Verifica la ruta e inténtalo de nuevo.")
        return

    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)
        cursor = db.cursor()
        contador = 0

        for fila in lector_csv:
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
