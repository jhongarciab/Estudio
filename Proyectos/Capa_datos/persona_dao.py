from conexion import Conexion
from cursordelpool import CursorDelPool
from persona import Persona

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, mail) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, mail=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.mail)
            cursor.execute(cls._INSERTAR, valores)
            print(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.mail, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            print(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            print(f'Objeto eliminado: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
    # Actualizar un registro
    persona1 = Persona(1,'Juan', 'Perez', 'jperez@mail.com')
    personas_actualizadas = PersonaDAO.actualizar(persona1)
    print(f'Personas actualizadas: {personas_actualizadas}')

    # Eliminar un registro
    persona1 = Persona(id_persona=15)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    print(f'Personas eliminadas: {personas_eliminadas}')

    # Insertar un registro
    persona1 = Persona(nombre='Alejandra', apellido='Tellez', mail='atellez@mail.com')
    personas_insertadas = PersonaDAO.insertar(persona1)
    print(f'Personas insertadas: {personas_insertadas}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        print(persona)