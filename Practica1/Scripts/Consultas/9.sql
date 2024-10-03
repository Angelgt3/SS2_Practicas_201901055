SELECT TOP 5 
    P.Edad, 
    P.Genero, 
    COUNT(*) AS CantidadViajes
FROM 
    Vuelos V
JOIN 
    Pasajeros P ON V.IdPasajero = P.IdPasajero
GROUP BY 
    P.Edad, P.Genero
ORDER BY 
    CantidadViajes DESC;
