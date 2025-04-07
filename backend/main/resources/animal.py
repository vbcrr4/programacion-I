from flask_restful import Resource
from flask import request

ANIMALES = {
    1:{'nombre':'Pepe', 'raza':'Obejero Aleman'},
    2:{'nombre':'Juanchi', 'raza':'Caniche'}
}

#Definir el recurso Animal
class Animal(Resource):
    def get(self, id):
        if int(id) in ANIMALES:
            return ANIMALES[int(id)]
        
        return 'El id es inexistente', 404
        
    def delete(self, id):
        if int(id) in ANIMALES:
            del ANIMALES[int(id)]
            return 'Eliminado con exito', 204
        
        return 'El id a eliminar es inexistente', 404
    
    def put(self, id):
        if int(id) in ANIMALES:
            animal = ANIMALES[int(id)]
            data = request.get_json()
            animal.update(data)
            return 'Animal editado con exito', 201
        
        return 'El id que intentan editar es inexistente', 404

class Animales(Resource):
    
    # Método GET: Obtiene todos los animales registrados
    def get(self):  # Corregido typo (original decía 'seft')
        """
        Retorna:
            dict: Diccionario completo con todos los animales registrados
            Ejemplo: {1: {nombre: 'Pepe',...}, 2: {nombre: 'Juanchi',...}}
        """
        return ANIMALES
    
    # Método POST: Crea un nuevo animal en el registro
    def post(self):
        """
        Pasos:
            1. Obtiene datos del animal desde el body de la solicitud (JSON)
            2. Genera un nuevo ID autoincremental basado en el máximo existente
            3. Agrega el nuevo animal al diccionario ANIMALES
            4. Retorna el animal creado con código 201 (Created)
            
        Returns:
            tuple: (dict, int) - Animal creado y código HTTP 201
        """
        animal = request.get_json()  # Obtiene datos del request
        
        # Genera nuevo ID (máximo ID existente + 1)
        # Advertencia: Si se eliminan registros podría causar IDs duplicados
        id = int(max(ANIMALES.keys())) + 1
        
        ANIMALES[id] = animal  # Almacena el nuevo animal
        
        return ANIMALES[id], 201  # Retorna animal creado + código HTTP 201