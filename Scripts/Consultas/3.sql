 SELECT 
    Nacionalidad,
    FORMAT(fecha_salida, 'MM-yyyy') AS MesAnioo,
    COUNT(*) AS Cantidad
FROM 
    Pasajeros P
JOIN 
    Vuelos V ON P.IdPasajero = V.IdPasajero
JOIN 
    Detalle_Vuelo DV ON V.IdDetalle_Vuelo = DV.IdDetalle_Vuelo
GROUP BY 
    Nacionalidad, FORMAT(fecha_salida, 'MM-yyyy')
ORDER BY 
    Nacionalidad, MesAnioo;
