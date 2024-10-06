SELECT 
    Estado_vuelo, 
    COUNT(*) AS CantidadVuelos
FROM 
    Detalle_Vuelo
GROUP BY 
    Estado_vuelo;
