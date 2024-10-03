SELECT 
    Genero, 
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Pasajeros) AS Porcentaje
FROM 
    Pasajeros
GROUP BY 
    Genero;
