from flask_restful import Resource
from flask import request

#creando usuarios
USUARIOS = {
    1:{'nombre':'nehuen','rol':'admin'},
    2:{'nombre':'franco','rol':'cliente'},
    3:{'nombre':'valentin','rol':'Dueno'}
}

# definir el recurso usuario

class Usuario(Resource):
    def get(self, id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        
        return 'El id es inexistente', 404
        
    def delete(self, id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)]
            return 'Eliminado con exito', 204
        
        return 'El id a eliminar es inexistente', 404
    
    def put(self, id):
        if int(id) in USUARIOS:
            animal = USUARIOS[int(id)]
            data = request.get_json()
            animal.update(data)
            return 'Animal editado con exito', 201
        
        return 'El id que intentan editar es inexistente', 404