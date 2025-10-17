import conexion, time, os, rich, datetime
from conexion import *

try:
	miResultado 			= None
	class usuario:
		def mostrarUsuarios():
			global miResultado
			try:
				cone 		= cconexion.conexionYuyito()
				cursor 		= cone.cursor()
				sql 		= """SELECT NRUT ||'-'|| DVRUT AS RUT, PNOMBRE ||' '|| SNOMBRE ||' '|| APPATERNO ||' '|| APMATERNO AS "TRABAJADOR",
								TAGNAME ||'(@' || USERNAME ||')' AS "USUARIO",
								CORREOUS AS CORREO, PASSWORDUS AS "CONTRASEÑA", dt.NOMBREDEPTRA AS DEPARTAMENTO
								FROM USUARIO NATURAL JOIN TRABAJADOR tra
								LEFT JOIN DEPARTAMENTO_TRA dt ON (tra.DEPARTAMENTO = dt.IDDEPTRA)
								ORDER BY IDUSER"""
				cursor.execute(sql)
				miResultado = cursor.fetchall()
				cone.commit()
				cone.close
				return miResultado
			except oracledb.Error as error:
				print("Error de extraer datos", error)
				return
		def verificarUsuarios():
			global miResultado
			try:
				cone 		= cconexion.conexionYuyito()
				cursor 		= cone.cursor()
				sql 		= "SELECT * FROM USUARIO ORDER BY USERNAME"
				cursor.execute(sql)
				miResultado = cursor.fetchall()
				cone.commit()
				cone.close
				return miResultado
			except oracledb.Error as error:
				print("Error de extraer datos", error)
				return

	class solicitud:
		def mostrarSolicitud():
			global miResultado
			try:
				cone 		= cconexion.conexionYuyito()
				cursor 		= cone.cursor()
				sql 		= "select * from solicitud order by id_soli"
				cursor.execute(sql)
				miResultado = cursor.fetchall()
				cone.commit()
				cone.close
				return miResultado
			except oracledb.Error as error:
				print("Error de extraer datos", error)
				return
		def agregarSolicitud():
			global miResultado
			try:
				cone 		= cconexion.conexionYuyito()
				cursor 		= cone.cursor()
				ahora 		= datetime.datetime.now()
				difA 		= ahora.strftime("%Y") # Definimos año de creación de documento
				difM 		= ahora.strftime("%m") # Definimos mes de creación de documento
				difD 		= ahora.strftime("%d") # Definimos día de creación de documento
				difH 		= ahora.strftime("%H") # Definimos hora de creación de documento
				difMin 		= ahora.strftime("%M") # Definimos minuto de creación de documento
				difS 		= ahora.strftime("%S") # Definimos segundo de creación de documento
				fecha 		= f"{difA}-{difM}-{difD}, {difH}:{difMin}:{difS}"
				id 			= 0
				if id:
					id+=1
				sql = f"insert into solicitud values ({id}, :2, :3, :4, {fecha})"
			except oracledb.Error as error:
				print(f"Error: {error}")
	print("[green]Clases activas[/green]")
except Exception as ex:
	print(f"[red]Hay un error: {ex}[/red]")