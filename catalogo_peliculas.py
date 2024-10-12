import os
from pelicula import Pelicula

class catalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre.lower().replace(' ', '_')}.txt"

    def agregar(self, pelicula):
        try:
            with open(self.ruta_archivo, 'a') as archivo:
                archivo.write(f'{pelicula.get_nombre()}\n')
        print(f"Película '{pelicula.get_nombre()}' agregada al catálogo.")
        except IOError:
        print(f"Error al agregar la película al catálogo '{self.nombre}'.")
        

    def listar(self):
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                peliculas = archivo.readlines()
                if not peliculas:
                    print(f"'El catálogo '{self.nombre}' está vacío.")
                else:

    def eliminar(self):
        if os.pathexists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"Catálogo '{self.nombre}' elimnado.")
        else:
            print(f"El catálogo '{self.nombre}' no existe.")