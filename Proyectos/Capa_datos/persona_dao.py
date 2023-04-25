from conexion import Conexion
from persona import Persona

class PersonaDAO:
    '''
    DAO: Data Access Object
    CRUD: Create, Read, Update, Delete
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, mail) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, mail=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for i in registros:
                persona = Persona(i[0], i[1], i[2], i[3])
                personas.append(persona)
            return personas
        
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.mail)
                cursor.execute(cls._INSERTAR, valores)
                print(f'Persona agregada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.mail, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                print(f'Persona actualizada: {persona}')
                return cursor.rowcount
            
    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                print(f'Persona eliminada: {persona}')
                return cursor.rowcount
    