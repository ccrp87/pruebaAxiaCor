# pruebaAxiaCor

## Enlaces de la API


###Crear usuario
(POST)/api/usuario/
{
    "nombre":"Felipe",
    "apellidos":"Gonzalez",
    "correo":"felipe.gonzalez@axiacore.com"
}

### Crear tarjeta
(POST) /api/tarjeta/
{
    "numero":"5424427427538352",
    "fecha_vencimiento":"2023-02-23"
}

(POST) /api/tarjeta/asociar_tarjeta/
{
    "usuarioid":"1",
    "tarjetauuid":"d2dfcc4b-7984-4c7a-95cc-1c2ff6ea38ec"
}

