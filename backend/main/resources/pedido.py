from flask_restful import Resource
from flask import request

PEDIDOS = { 1:{'id_user:':1, 'created_at:':'01/02/25',
              'status':'Entregado', 'total':10000},
            2:{'id_user:':2, 'created_at:':'01/02/25',
              'status':'Entregado', 'total':20000},
            3:{'id_user:':3, 'created_at:':'01/02/25',
              'status':'Entregado', 'total':30000}}
class Pedido(Resource):
    def get(self,id):
        if int(id) in PEDIDOS:
            return PEDIDOS[id]
        return 'El id es inexistente', 404
    
    def delete(self,id):
        if int(id) in PEDIDOS:
            del PEDIDOS[id]
            return 'Eliminado con éxito', 204
        return 'El id a eliminar es inexistente', 404
    
    def put(self,id):
        if int(id) in PEDIDOS:
            pedido = PEDIDOS[id]
            data = request.get_json()
            pedido.update(data)
            return 'producto editado con éxito', 204
        return 'El producto que intenta editar es inexistente', 404
    
    def post(self):
        producto = request.get_json()
        id = int(max(PEDIDOS.keys()))+1
    


        