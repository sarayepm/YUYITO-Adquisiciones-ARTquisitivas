from tkinter import *; from tkinter import ttk, messagebox; from rich import *; from win10toast_click import ToastNotifier; from fpdf import *; from os import system as sys
from sqlfunci import *; from adquisiciones import *; from otrostrabajadores import *; from extra import *

class formularioUsuario:
		global adminPage
		adminPage  = None

		global users
		users 	   = None

def mainAdmin(name):
	try:
		adminPage = tk.Tk()
		adminPage.title(f"Pantalla del admin - {name}")
		adminPage.geometry("1920x1080")

		def crearUser():
			panCrear = tk.Tk()
			panCrear.title(f"Creador de usuarios - {name}")
			adminPage.geometry("1920x1080")
			
			panCrear.mainloop()
			# pronto(name)

		def borrarUser():
			messagebox.askyesno("¿Estas seguro, artista jefe?", "¿Estás seguro de eliminar a {name}?")
		def enterProfile():
			pronto(name)
		Label(adminPage, text = "USUARIOS", font = ("Arial", 45)).pack(pady = 50)
		users = ttk.Treeview(adminPage, columns = ("Rut", "Trabajador", "Edad", "Usuario", "Correo", "Contraseña", "Departamento"))
		users.column("#0", anchor =	W)
		users.heading("#0", text  =	"ID")
		users.column("#1", anchor =	W)
		users.heading("#1", text  =	"Rut")
		users.column("#2", anchor =	W)
		users.heading("#2", text  =	"Trabajador")
		users.column("#3", anchor =	W)
		users.heading("#3", text  =	"Edad")
		users.column("#4", anchor =	W)
		users.heading("#4", text  =	"Usuario")
		users.column("#5", anchor =	W)
		users.heading("#5", text  =	"Correo")
		users.column("#6", anchor =	W)
		users.heading("#6", text  =	"Contraseña")
		users.column("#7", anchor =	W)
		users.heading("#7", text  =	"Departamento")
		for row in solicitud.mostrarSolicitud():
			users.insert("","end", values = row)    
		users.pack()
		notiBar = Message(adminPage)

		Button(adminPage, text = "Crear un usuario", command = crearUser).pack()
		Button(adminPage, text = "Eliminar usuario", command = borrarUser).pack()
		Button(adminPage, text = "Ingresar perfil ", command = enterProfile).pack()

		adminPage.mainloop()
		sys("cls")
	except Exception as ex: 
		print(f"Error: {ex}")
		messagebox.showerror("ERROR", "Hubo un error al ejecutar esta acción, informe de esto al desarrollador.")
						
	def actualizarTreeView():
		global tree

		try:
				#Borrar todos los elementos actuales del treeview
				tree.delete(*tree.get_children())
				# obtener los nuevos valores
				datos = usuario.mostrarUsuarios()

				# insertar los nuevos datos en el treeview

				for row in usuario.mostrarUsuarios():
						tree.insert("","end",values=row)
						
		except ValueError as error:
				print("Error al actualizar la tabla{}".format(error))

	def seleccionarRegistro(event):
		try:
				#obtener el id del elemento seleccionado
				itemSeleccionado = users.focus()
				if itemSeleccionado:
						# obtener los valores por columnas
						values = users.item(itemSeleccionado)['values']
						# Establecer los valores en los widgets
		except ValueError as error:
				print ("Error al seleccionar registro {}".format(error))

mainAdmin("ADQUISICIONES ARTQUISITIVAS")