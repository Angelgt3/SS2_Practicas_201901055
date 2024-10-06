USE SEMI2_practica1;

-- Eliminar tabla Vuelos si existe
IF OBJECT_ID('dbo.Vuelos', 'U') IS NOT NULL
    DROP TABLE dbo.Vuelos;

-- Eliminar tabla Detalle_Vuelo si existe
IF OBJECT_ID('dbo.Detalle_Vuelo', 'U') IS NOT NULL
    DROP TABLE dbo.Detalle_Vuelo;

-- Eliminar tabla Aeropuertos si existe
IF OBJECT_ID('dbo.Aeropuertos', 'U') IS NOT NULL
    DROP TABLE dbo.Aeropuertos;

-- Eliminar tabla Pasajeros si existe
IF OBJECT_ID('dbo.Pasajeros', 'U') IS NOT NULL
    DROP TABLE dbo.Pasajeros;

-- Eliminar tabla DatosTemporales si existe
IF OBJECT_ID('dbo.DatosTemporales', 'U') IS NOT NULL
    DROP TABLE dbo.DatosTemporales;
