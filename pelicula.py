class Pelicula:
    contador_peliculas = 0 # Atributo de clase para contar el número de pel películas creadas

    # Constructor de la clase Pelicula
    def __init__(self, nombre, director, año, duracion, genero):
        self.__nombre = nombre # Atributo privado
        self.director = director
        self.año = año 
        self.__duracion = duracion # Atributo privado
        self.genero = genero

        Pelicula.contador_peliculas += 1 # Incrementa el contador de películas cada vez que se crea una nueva instancia

    # Método de clase para obtener el contador de películas
    @classmethod
    def obtener_contador(cls):
        return cls.contador_peliculas # Devuelve el número total de películas creadas
    
    # Método estático para verificar si el nombre de una película es válido
    @staticmethod
    def es_pelicula_valida(nombre):
        return isinstance(nombre, str) and len(nombre) > 0

    def __init__(self, nombre):
        self.__nombre = nombre # Atributo privado
    
    # Getter para obtener el nombre de la pelicula
    def get_nombre(self): # Método **getter** que permite acceder a valor del atributo privado "Titulo".
        return self.__nombre # devuelve el valor del atributo privado.
    
    # Setter para modificar el nombre de manera controlada
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0: # Verificar si el 'Nuevo nombre' es cadena y mayor a 0.
            self.__nombre = nuevo_nombre # Cambia el valor del atributo privado.
        else:
            print('Error: El nombre no puede estar vacío.')

    # Getter para obtener la duración
    def get_duracion(self):
        # Método que retorna la duración de la película.
        return self.__duracion

    # Setter para modificar la duración de manera controlada
    def set_duracion(self, nueva_duracion):
        if nueva_duracion > 0:
            self.__duracion = nueva_duracion
        else:
            print('Error: La duración debe ser positiva.') # Mnsaje de error si la validación falla

# Método para mostrar la información de la película
    def mostrar_info(self):
        print(f'Película: {self.__nombre}, Director: {self.director}, Año: {self.año}, Duración: {self.__duracion}, Género: {self.genero}')


mi_pelicula = Pelicula('nombre') # Creación de objeto de la clase Película