SELECT 
    FORMAT(fecha_salida, 'MM-yyyy') AS MesAnio, 
    COUNT(*) AS CantidadVuelos
FROM 
    Detalle_Vuelo
GROUP BY 
    FORMAT(fecha_salida, 'MM-yyyy')
ORDER BY 
    MesAnio;
