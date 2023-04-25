import psycopg2 as bd
import sys

class Conexion:
    _DATABASE = 'Test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Xevaxtiam1'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                user=cls._USERNAME,
                password=cls._PASSWORD, 
                port=cls._DB_PORT, 
                database=cls._DATABASE)
                print('Conexión exitosa')
                return cls._conexion
            except Exception as e:
                print(f'Ocurrió un error al obtener la conexión: {e}')
                sys.exit()
        else:
            return cls._conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print('Cursor exitoso')
                return cls._cursor
            except Exception as e:
                print(f'Ocurrió un error al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor