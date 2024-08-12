SELECT 
    A.Pais, 
    COUNT(*) AS CantidadVuelos
FROM 
    Vuelos V
JOIN 
    Aeropuertos A ON V.IdAeropuerto = A.IdAeropuerto
GROUP BY 
    A.Pais;
