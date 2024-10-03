SELECT TOP 5 
    A.Nombre AS Aeropuerto, 
    COUNT(*) AS CantidadPasajeros
FROM 
    Vuelos V
JOIN 
    Aeropuertos A ON V.IdAeropuerto = A.IdAeropuerto
GROUP BY 
    A.Nombre
ORDER BY 
    CantidadPasajeros DESC;
