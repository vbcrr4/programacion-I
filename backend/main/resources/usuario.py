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
            return 'Eliminado con exito', 200
        
        return 'El id a eliminar es inexistente', 404
    
    def put(self, id):
        if int(id) in USUARIOS:
            usuario = USUARIOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return 'Usuario editado con exito', 201
        
        return 'El id que intentan editar es inexistente', 404
    
class Usuarios(Resource):
    def get(self):
        usuarios = db.session.query(UsuarioModel).all()
        return jsonify([usuario.to_json()for usuario in usuarios])
    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        db.session.commit()
        return 'ok', 201

        #id = int(max(USUARIOS.keys())) +1
        #USUARIOS[id] = usuario
        #return USUARIOS[id], 201