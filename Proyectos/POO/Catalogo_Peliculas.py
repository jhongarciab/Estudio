import os

class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Nombre: {self.nombre}'
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

class Catalogo:
    ruta = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta, 'a', encoding='utf-8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta, 'r', encoding='utf-8') as archivo:
            print('Catálogo de películas'.center(60, '-'))
            print(archivo.read())

    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta)
        print(f'Archivo eliminado: {cls.ruta}')

opcion = None
while opcion != "0":
    print(
        '''
        Catálogo de Películas

        0 - Salir
        1 - Añadir película
        2 - Listar películas
        3 - Eliminar película
        '''
    )
    opcion = input("Elige una opción: ")
    if opcion == "0":
        print("Hasta luego")
    elif opcion == "1":
        nombre = input("Introduce el nombre de la película: ")
        pelicula = Pelicula(nombre)
        Catalogo.agregar_pelicula(pelicula)
    elif opcion == "2":
        Catalogo.listar_peliculas()
    elif opcion == "3":
        Catalogo.eliminar()
    else:
        print("Opción no válida")