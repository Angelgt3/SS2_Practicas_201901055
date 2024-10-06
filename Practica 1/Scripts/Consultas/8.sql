SELECT TOP 5 
    A.Continente, 
    COUNT(*) AS CantidadVisitas
FROM 
    Vuelos V
JOIN 
    Aeropuertos A ON V.IdAeropuerto = A.IdAeropuerto
GROUP BY 
    A.Continente
ORDER BY 
    CantidadVisitas DESC;
