class Pelicula:
    contador_peliculas = 0 # Atributo de clase para contar el número de pel películas creadas

    # Constructor de la clase Pelicula
    def __init__(self, nombre, director, año, duracion, genero):
        self.__nombre = nombre # Atributo privado
        self.director = director
        self.año = año 
        self.duracion = duracion 
        self.genero = genero
        
        Pelicula.contador_peliculas += 1 # Incrementa el contador de películas cada vez que se crea una nueva instancia

    @classmethod
    def obtener_contador(cls):
        return cls.contador_peliculas

    @staticmethod
    def es_pelicula_valida(nombre):
        return isinstance(nombre, str) and len(nombre) > 0

    def __init__(self, nombre):
        self.__nombre = nombre # Atributo privado

    def get_nombre(self): # Método **getter** que permite acceder a valor del atributo privado "Titulo".
        return self.__nombre # devuelve el valor del atributo privado

# Método para mostrar la información de la película
    def mostrar_info(self):
        print(f'Película: {self.__nombre}, Director: {self.director}, Año: {self.año}')

