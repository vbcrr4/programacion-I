from flask_restful import Resource
from flask import request

#creando PRODUCTOS
PRODUCTOS = {
    1:{'nombre':'hamburgesa','precio':'5000'},
    2:{'nombre':'papas fritas','precio':'2000'},
    3:{'nombre':'nuggets','precio':'3000'}
}


class Producto(Resource):
    def get(self, id):
        if int(id) in PRODUCTOS:
            return PRODUCTOS[int(id)]
        
        return 'El id es inexistente', 404
        
    def delete(self, id):
        if int(id) in PRODUCTOS:
            del PRODUCTOS[int(id)]
            return 'Eliminado con exito', 204
        
        return 'El id a eliminar es inexistente', 404
    
    def put(self, id):
        if int(id) in PRODUCTOS:
            producto = PRODUCTOS[int(id)]
            data = request.get_json()
            producto.update(data)
            return 'producto editado con exito', 201
        
        return 'El id que intentan editar es inexistente', 404
    
class Productos(Resource):

    def get(self):
        return PRODUCTOS
    
    def post(self):

        producto = request.get_json()
        id = int(max(PRODUCTOS.keys()))+1
        PRODUCTOS = producto
