SELECT TOP 5 
    A.Pais, 
    COUNT(*) AS CantidadVisitas
FROM 
    Vuelos V
JOIN 
    Aeropuertos A ON V.IdAeropuerto = A.IdAeropuerto
GROUP BY 
    A.Pais
ORDER BY 
    CantidadVisitas DESC;
