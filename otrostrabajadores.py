import time, tkinter as tk, os
from tkinter import *; from tkinter import ttk, messagebox; from os import system as sys; from rich import *; from sqlfunci import *

# python.exe -m pip install --upgrade pip
# pip install fpdf rich win10toast_click pillow

veri_win = False

def soliWin(name):
	try:
		sys("cls")
		muestra = tk.Tk()
		muestra.title(f"Envío de solicitudes - {name}")
		muestra.geometry("1920x1080")

		AdquiArt = Label(muestra, anchor=tk.W,
					text = f"{name}",
					font =("Arial", 26),
					width = 100)
		AdquiArt.pack(padx = 20, pady = 20)

		Label(muestra, text ="Solicitud de productos", font=("arial", 20)).pack()
		Label(muestra, text ="(Los campos con * son OBLIGATORIOS)", fg = "red", font = ("Arial", 10, "bold")).pack()
		labelProdName = Label(muestra, text="Ingrese un producto (*)", width=30, font=("arial", 14))
		textBoxProdName = Entry(muestra, width=40, font=("Arial", 12, "italic"))

		stockVeri = DoubleVar()
		stockReque = Scale(muestra, variable = stockVeri, from_ = 0, to = 100, orient = HORIZONTAL, width = 20, length = 367)

		labelReque = Label(muestra, text = "Requerimientos específicos", width = 30, font = ("arial", 14))
		textBoxReque = Entry(muestra, width = 40, font = ("Arial", 12, "italic"))

		progress = ttk.Progressbar(muestra, orient="horizontal", length = 250, mode = "determinate")
		def envio_soli(): # Con esto enviamos la solicitud a Adquisición, tendrá más sentido al integrar la base de datos.
			global veri_win
			if not veri.get():
				print("[bold red]ERROR:[/bold red] El pedido [bold red]NO[/bold red] está verificado")
				messagebox.showwarning("¡Espera, artista!", "No has verificado que de verdad quieres el pedido.")
				return
			else:
				if textBoxProdName.get().strip() == "" or stockReque.get() == 0:
					print("[bold red]ERROR:[/bold red] Hay un espacio [bold red]obligatorio[/bold red] vacío")
					messagebox.showwarning("¡Un momento!", "No puedes dejar valores obligatorios vacíos")
					return
				else:
					ask = messagebox.askquestion("Confirmar envío de solicitud", "¿Estás seguro de la solicitud?") # NOTA: tratar de ajustar para que al presionar "NO" no se muestre la pantalla de carga
					# Nota: ya está.
					# Aquí creamos una pantalla de carga
					if ask != "yes":
						return
					else:
						progress.pack(pady=10)
						progress.start()
						for i in range(101):
							time.sleep(0.04)  
							progress['value'] = i
							muestra.update_idletasks()
						progress.stop()
						solicitud.agregarSolicitud()
						muestra.destroy()
						veri_win = True
						print("[bold green]SOLICITUD ENVIADA[/bold green]")
						messagebox.showinfo("¡Felicidades, artista!", "Se ha enviado la notifición, observa su estado en la aplicación.")

		veri = IntVar() # Con esto se verifica si la casilla fue seleccionada o no
		checkVeri = Checkbutton(muestra, text = "Presiona esta casilla para demostrar que este es el pedido que quieres. (*)", font = ("arial", 14), variable = veri, cursor="hand2")
		labelProdName.pack()
		textBoxProdName.pack()
		Label(muestra, text="Stock (*)", width=40, font=("Arial", 12)).pack()
		stockReque.pack()

		labelReque.pack()
		textBoxReque.pack()

		checkVeri.pack()

		soliAcepta = tk.Button(muestra, text = "Confirmar", height = 2, width = 40, command = envio_soli, cursor="hand2")
		soliAcepta.pack()
		
		muestra.mainloop()
		sys("cls")
	except Exception as ex: 
		print(f"Error: {ex}")
		messagebox.showerror("ERROR", "Hubo un error al ejecutar esta acción, informe de esto al desarrollador.")

soliWin("ADQUISICIONES ARTQUISITIVAS")