SELECT 'Pasajeros' AS Tabla, COUNT(*) AS Cantidad FROM Pasajeros
UNION ALL
SELECT 'Aeropuertos' AS Tabla, COUNT(*) AS Cantidad FROM Aeropuertos
UNION ALL
SELECT 'Detalle_Vuelo' AS Tabla, COUNT(*) AS Cantidad FROM Detalle_Vuelo
UNION ALL
SELECT 'Vuelos' AS Tabla, COUNT(*) AS Cantidad FROM Vuelos;
