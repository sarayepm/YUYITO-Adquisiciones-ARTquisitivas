import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pkg_resources")
warnings.filterwarnings("ignore", category=DeprecationWarning)
import time, fpdf, rich, random, os, datetime, tkinter as tk, sqlfunci
from tkinter import *; from tkinter import ttk, messagebox; from rich import *; from fpdf import *; from os import system as sys; from sqlfunci import *

# python.exe -m pip install --upgrade pip
# pip install fpdf rich win10toast_click pillow winotify

class adquisisiones:
	global muestra
	muestra  = None

	global tree
	tree = None

def mainPageAd(name):
	mainpage = tk.Tk()
	mainpage.title(f"Página principal (adquisición) - {name}")
	def solicitudes():
		try:
			muestra = tk.Tk()
			sys("cls")
			def soliMuest():
				muestra.title(f"Solicitudes de la empresa - {name}")
				muestra.geometry("1920x1080")

				AdquiArt = Label(muestra, anchor = W, text =  f"{name}", font = ("Arial", 26))
				AdquiArt.pack(pady = 10)

				tree = ttk.Treeview(muestra, columns = ("ID","Producto","Stock","Departamento solicitante","Solicitador","Estado"),show = 'headings', height = 5) # Con esto creamos una tabla
				tree.column("#1", anchor = W) # Asigna columnas
				tree.heading("#1", text = "ID") # Asigna nombre a los encabezados de las columnas
				tree.column("#2", anchor = W)
				tree.heading("#2", text = "Producto")
				tree.column("#3", anchor = W)
				tree.heading("#3", text = "Stock")
				tree.column("#4", anchor = W)
				tree.heading("#4", text = "Departamento solicitante")
				tree.column("#5", anchor = W)
				tree.heading("#5", text = "Solicitador")
				tree.column("#6", anchor = W)
				tree.heading("#6", text = "Estado")
				for row in solicitud.mostrarSolicitud():
					tree.insert("","end", values=row)    
				tree.pack()
				muestra.mainloop()
		except Exception as ex: 
			print(f"Error: {ex}")
			messagebox.showerror("ERROR", "Hubo un error al ejecutar esta acción, informe de esto al desarrollador.")

			sys("cls")
	Button(mainpage, text = "Gestionar solicitudes", command = solicitudes()).pack()
	mainpage.mainloop()
mainPageAd("ADQUISICIONES ARTQUISITIVAS")