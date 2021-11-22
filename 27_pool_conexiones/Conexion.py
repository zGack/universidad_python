from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CNX = 1
    _MAX_CNX = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool == None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CNX, cls._MAX_CNX,
                                                        host = cls._HOST,
                                                        user = cls._USERNAME,
                                                        password = cls._PASSWORD,
                                                        port = cls._DB_PORT,
                                                        database = cls._DATABASE)
                log.debug(f'Creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrior un error al abotener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f'Se ha cerrado el pool de conexiones')
    
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    # conexion3 = Conexion.obtenerConexion()
    # conexion4 = Conexion.obtenerConexion()
    # conexion5 = Conexion.obtenerConexion()
    # conexion6 = Conexion.obtenerConexion()