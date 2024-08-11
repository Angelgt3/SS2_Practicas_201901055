USE SEMI2_practica1;
GO

-- Eliminar tabla si existe
IF OBJECT_ID('dbo.Pasajeros', 'U') IS NOT NULL
    DROP TABLE dbo.Pasajeros;
GO
-- Crear tabla de Pasajeros
CREATE TABLE Pasajeros (
    IdPasajero VARCHAR(100) PRIMARY KEY,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Genero VARCHAR(20),
    Edad INT,
    Nacionalidad VARCHAR(100)
);
GO

-- Eliminar tabla si existe
IF OBJECT_ID('dbo.Aeropuertos', 'U') IS NOT NULL
    DROP TABLE dbo.Aeropuertos;
GO
-- Crear tabla de Aeropuertos
CREATE TABLE Aeropuertos (
    IdAeropuerto INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(100),
    IdPais VARCHAR(100),
    Pais VARCHAR(100),
    IdContinente VARCHAR(10),
    Continente VARCHAR(50)
);
GO

-- Eliminar tabla si existe
IF OBJECT_ID('dbo.Detalle_Vuelo', 'U') IS NOT NULL
    DROP TABLE dbo.Detalle_Vuelo;
GO
-- Crear tabla de Detalle_Vuelo
CREATE TABLE Detalle_Vuelo (
    IdDetalle_Vuelo INT IDENTITY(1,1) PRIMARY KEY,
    fecha_salida DATE,
    aeropuerto_llegada VARCHAR(100),
    piloto VARCHAR(100),
    Estado_vuelo VARCHAR(10)
);
GO

-- Eliminar tabla si existe
IF OBJECT_ID('dbo.Vuelos', 'U') IS NOT NULL
    DROP TABLE dbo.Vuelos;
GO
-- Crear tabla de Vuelos
CREATE TABLE Vuelos (
    IdVuelo INT IDENTITY(1,1) PRIMARY KEY,
    IdPasajero VARCHAR(100) FOREIGN KEY REFERENCES Pasajeros(IdPasajero), 
    IdAeropuerto INT FOREIGN KEY REFERENCES Aeropuertos(IdAeropuerto),
    IdDetalle_Vuelo INT FOREIGN KEY REFERENCES Detalle_Vuelo(IdDetalle_Vuelo)
);
GO

CREATE TABLE DatosTemporales (
    IdVuelo INT IDENTITY(1,1) PRIMARY KEY,
    PassengerID VARCHAR(100),
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Gender VARCHAR(10),
    Age INT,
    Nationality VARCHAR(100),
    AirportName VARCHAR(100),
    AirportCountryCode VARCHAR(100),
    CountryName VARCHAR(100),
    AirportContinent VARCHAR(100),
    Continents VARCHAR(100),
    DepartureDate VARCHAR(100),
    ArrivalAirport VARCHAR(100),
    PilotName VARCHAR(100),
    FlightStatus VARCHAR(100)
)