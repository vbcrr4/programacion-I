# Rest

-  es una arquitectura de software para aplicaciones web

- Relacion cliente servidor  : el cliente esta separado del servidor

- Sin estado : Comunicacion entre el cliente y el servidor sin estado, lo cual quiere decir que no almacena informacion del cliente en solicitudes como GET

# HTTP

- Que es ?  
HTTP es un protocolo de la capa de aplicación (modelo OSI) que define cómo se estructuran y transmiten los mensajes entre clientes y servidores.
- Para que sirve
Permite solicitar y entregar recursos web, como páginas HTML, imágenes, archivos CSS/JS, o datos de APIs.
- Solicitud (Request)
Método HTTP: Indica la acción a realizar:

GET: Obtener un recurso (ej: cargar una página).

POST: para crear un recurso del servidor (ej: formulario de login).

PUT, DELETE, PATCH: Para actualizar, eliminar o modificar recursos.

URL: Dirección del recurso (ej: https://ejemplo.com/ruta).

Headers: Metadatos (ej: tipo de contenido aceptado, cookies).

Body (opcional): Datos enviados al servidor (ej: en POST).

- Respuesta (Response)
Código de estado: Indica el resultado de la solicitud:

200 OK: Éxito.

404 Not Found: Recurso no encontrado.

500 Internal Server Error: Fallo del servidor.

Headers: Metadatos (ej: tipo de contenido, cookies).

Body: Contenido solicitado (ej: HTML, JSON).

- ¿Por qué es Importante Aprender HTTP?
Es esencial para desarrollo web, APIs, y debugging.

Entenderlo ayuda a resolver errores comunes (ej: 404, CORS).

Base para aprender protocolos más avanzados (HTTP/2, WebSockets).

- Ejemplo de JSON

{
  "nombre": "Carlos",
  "edad": 30,
  "esEstudiante": false,
  "hobbies": ["fútbol", "lectura"],
  "direccion": {
    "calle": "Av. Siempreviva 123",
    "ciudad": "Buenos Aires"
  }
}

- ¿Para qué se usa JSON?
APIs REST: Intercambiar datos entre cliente y servidor.

Almacenamiento: Guardar configuraciones o datos en archivos.

Comunicación entre servicios: En microservicios o aplicaciones distribuidas.

Bases de datos NoSQL: Como MongoDB o Firebase usan JSON (o su versión binaria, BSON).