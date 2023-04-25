import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='Xevaxtiam1',
    host='127.0.0.1',
    port='5432',
    database='Test_db'
)

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, mail) VALUES(%s, %s, %s)'
    valores = ('Hernando', 'Lara', 'jlara@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, mail = %s WHERE id_persona = %s'
    valores = ('Yusley', 'Perez', 'jp@mail.com', 1)
    cursor.execute(sentencia, valores)
    
    conexion.commit()
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()