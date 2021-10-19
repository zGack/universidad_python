class Pelicula:
    def __init__(self, pelicula):
        self._pelicula = pelicula

    @property
    def pelicula(self):
        return self._pelicula

    @pelicula.setter
    def pelicula(self, pelicula):
        self._pelicula = pelicula

    def __str__(self):
        print(f'Pelicula: {self._pelicula}')
