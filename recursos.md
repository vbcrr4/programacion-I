# usuarios

GET: Obtener listado de usuarios. Rol: ADMIN
POST: Crear un usuario. Rol: ADMIN

# obtener usuario

GET: . Obtener un usuario. Rol: ADMIN
PUT: Editar un usuario. Rol: ADMIN
DELETE: Eliminar un usuario (cambiar de estado o suspender). Rol: ADMIN/ENCARGADO

# productos
GET: obtener una lista de productos Rol: USER/ADMIN/ENCARGADO
POST: crear un producto Rol: ADMIN

# obtener productos

GET: Obtener un producto. Rol: USER/ADMIN/ENCARGADO
PUT: Editar un producto.  Rol: ADMIN/ENCARGADO
DELETE: Eliminar un producto Rol: ADMIN

# Logout

POST: invalida token actual Rol: USER/ADMIN/ENCARGADO

# Login
POST: loguear un usuario Rol: USER/ADMIN/ENCARGADO

# Pedidos

GET: Obtener todos los pedidos Rol: ADMIN/ENCARGADO
POST: Crear un pedido Rol: USER/ADMIN/ENCARGADO

# Obtener ID del pedido

GET: Obtener un pedido Rol: USER/ADMIN/ENCARGADO
PUT: Modificar pedido Rol: USER(si cancela)/ADMIN/ENCARGADO
DELETE: Eliminar pedido Rol: USER(si cancela)/ADMIN/ENCARGADO

# Menu
GET: Obtener listado de productos. Rol Administrador
POST: Agregar un nuevo producto al menú. Rol Administrador
PUT: Editar un producto. Rol Administrador
DELETE: Eliminar un producto. Rol Administrador/Empleado

# Informes

Table user {
  id integer [primary key]
  name varchar(100)
  cellphone varchar(20) [unique, not null]
  email varchar(100) [unique, not null]
  password varchar(255) [not null]
  address varchar(255) 
  rol enum("client", "admin") [not null]                #???? q hace el enum
  state enum( "active", "blocked") [default: "active"]
  created_at timestamp                                   # que mierda hace timestamp
}

Table product {
  id integer [primary key]
  name varchar(100) [unique, not null]
  description text
  price decimal(10,2) [not null]            # que significa el (10,2)
  available boolean [default: true]
  category varchar(50) [not null]
  image_url varchar(255)                    # no entiendo
  popularity integer [default: 0]           # tampoco entiendo
}


Table order {
  id integer [primary key]
  user_id integer [not null]
  created_at timestamp
  status enum("pending", "preparing", "ready", "delivered", "canceled") [not null]
  total float [not null]
}

Table order_details {
  id integer [primary key]
  order_id integer [not null]
  product_id integer [not null]
  quantity integer [not null]
  price decimal(10,2) [not null]
  subtotal decimal(10,2) [not null]
}

Table rating {
  id integer [primary key]
  user_id integer [not null]
  product_id integer [not null]
  rating integer
  comment text
  date timestamp
}

Table notification {
  id integer [primary key]
  user_id integer [not null]
  message text [not null]
  sent_date timestamp
  status enum("pending", "sent", "failed") [default: "pending"]
}

Ref Client_Order: order.user_id > user.id
Ref Client_Rating: rating.user_id > user.id
Ref Rating_Product: rating.product_id > product.id
Ref notificacion_cliente: notification.user_id > user.id
Ref Order_Details_Order: order_details.order_id > order.id
Ref Order_Details_Product: order_details.product_id > product.id