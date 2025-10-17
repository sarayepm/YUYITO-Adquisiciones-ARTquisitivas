import oracledb

class cconexion():
    def conexionYuyito():
        try:
            conexion=oracledb.connect( # Hace la conexión con Oracle
            user='YUYITO',
            password='1234',
            dsn='localhost:1521/xepdb1') # Conecta a un servidor local
            return conexion
        
        except oracledb.Error as error:
            print ("Error al conectar a la base de datos {}".format(error))    
            return conexion

    conexionYuyito()