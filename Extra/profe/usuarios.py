from conexion import *

class cusuarios:
    def mostrarUsuarios():
        try:
            cone = cconexion.conexionYuyito()
            cursor = cone.cursor()
            sql = "select * from usuarios order by usuario"
            cursor.execute(sql)
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close
            return miResultado
        except oracledb.Error as error:
            print ("Error de extraer datos", error)
            return

    def ingresarUsuarios(usuario, password, nombre):
        try:
            cone = cconexion.conexionYuyito()
            cursor = cone.cursor()
            sql = "insert into usuarios values (:1,:2,:3)"
            # la variable valores debe ser una tupla
            # como minima expresión es (valor,), la coma hace que sea una tupla
            # las tuiplas son inmutables, no se puede modificar
            valores = (usuario, password, nombre)
            print (sql)
            print (valores)
            cursor.execute(sql,valores)
            cone.commit()
            print (cursor.rowcount, "Registros Ingresados")
            cone.close
        except oracledb.Error as error:
            print ("Error de ingreso de datos", error)

    def modificarUsuarios(usuario, password, nombre):
        try:
            cone = cconexion.conexionYuyito()
            cursor = cone.cursor()
            sql = "update usuarios set usuarios.password = :1,usuarios.nombre = :2 where usuarios.usuario = :3"
            valores = (password, nombre, usuario)
            cursor.execute(sql,valores)
            cone.commit()
            print (cursor.rowcount, "Registro Actualizado")
            cone.close
        except oracledb.Error as error:
            print ("Error de actualización de datos")
        
    def eliminarUsuarios(usuario):
        try:
            cone = cconexion.conexionYuyito()
            cursor = cone.cursor()
            sql = "delete from usuarios where usuarios.usuario = :1"
            valores = (usuario,)
            cursor.execute(sql,valores)
            cone.commit()
            print (cursor.rowcount, "Registro Eliminado")
            cone.close
        except oracledb.Error as error:
            print ("Error de Eliminación de datos")
        
                