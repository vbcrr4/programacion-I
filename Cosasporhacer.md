# Este es un listado de todas las cosas que hay que hacer (Para el final)
## NO BORRAR LAS LÍNEAS CUANDO SE COMPLETAN TAREAS, TACHARLAS USANDO DOS ONDAS ~ ~~ texto ~~
1- Hay una gran cantidad de código repetido en el sector panel.html, buscar una manera de eliminar el boilerplate
2- Estándarizar los botones usados, algunos son app-button y otros app-action-bttn
    2.1- Esto sucede en los botones "anterior" y "siguiente" en el menú principal
3- Intentar que la card principal ocupe toda la pantalla
4- Arreglar las imágenes del menú principal
5- Que los botones "siguiente" y "anterior" no estén fuera de la pantalla
6- Que en cualquier pestaña no se scrollee la pantalla, sino adentro de la card principal
7- En Panel de Empleado,:
    7.1 En cargar nuevo pedido, que al hacer click en productos, salgan todos los productos disponibles
        7.1.1 Agregar pedido falla
        7.1.2 Que al agregar pedido, se necesita saber que usuario es del pedido, agregar una lista que muestre los usuarios
        7.1.3 Que no te deje agregar pedidos, a menos que seas cliente
        7.1.4 Agregar un mensaje de error al agregar un pedido
    7.2- En verificar stock que diga el número de todos los productos disponibles
8- En perfil
    8.1- que si el usuario es empleado o admin, no tenga un listado de pedidos (Se asume que estos usuarios no deben hacer pedidos)
    8.2- que el texto "miembro desde ..." muestre correctamente el horario o la fecha (Esto ocurre tmb en el campo Registrado)
9-En Panel Admin
    9.1- En pestaña gestión menú
        9.1.1- El botón de "editar" no hace nada
        9.1.2- El botón de "Borrar" no hace nada, y cierra la sesión del usuario
        9.1.3- Los productos no muestran las categorías que tienen
        9.1.4- El buscador de categoría debería desplegar las categorías disponibles en los productos
    9.2- En pestaña Nuevo Producto
        9.2.1- La pestaña no agrega productos nuevos
    9.3- En pestaña Pedidos
        9.3.1- El botón ver detalle no hace nada, y te manda al lobby
        9.3.2- El botón Confirmar no hace nada y te manda al lobby
        9.3.3- Que hace el botón confirmar? Desde un punto de vista de diseño,
    9.4- En pestaña Usuarios
        9.4.1- Debería mostrar la foto de perfil de usuario 
    9.5- En pestaña promociones
        9.5.1- Te manda al inicio de sesión, cuando envía la promoción
        9.5.2- Comprobar si realmente se envía la promoción 
10- Agregar productos a la db que tengan otra categoría excepto "Food"
