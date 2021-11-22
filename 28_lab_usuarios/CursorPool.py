from logger_base import log
from Conexion import Conexion

class CursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metedo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug(f'Se ejecuta metodo __exit__')

        if exc_val:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion, se hace rollback: {exc_val} {exc_type} {exc_tb}')
        else:
            self._conexion.commit()
            log.debug(f'Commit de la transaccion')

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
        

if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM usuarios')
        log.debug(cursor.fetchall())