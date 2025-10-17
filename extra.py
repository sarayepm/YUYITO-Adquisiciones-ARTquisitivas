import time, tkinter as tk, recursos as re
from tkinter import *; from tkinter import ttk, messagebox; from rich import *; from PIL import Image, ImageTk; from os import system as sys; from recursos import *
# from conexion import *; from login import *; from otrostrabajadores import *; from adquisiciones import *; from sqlfun import *; from admin import *

# python.exe -m pip install --upgrade pip
# pip install fpdf rich win10toast_click pillow

sys("cls")


def openGif(nGif, win, ms, X, Y):
    animacion = []
    gif = Image.open(nGif)
    try:
        while True:
            frame = ImageTk.PhotoImage(gif.copy(), master=win)  # <-- master=win
            animacion.append(frame)
            gif.seek(len(animacion))
    except EOFError:
        pass

    lbl_gif = tk.Label(win)
    lbl_gif.place(x=X, y=Y)

    def update(ind):
        frame = animacion[ind]
        lbl_gif.config(image=frame)
        ind = (ind + 1) % len(animacion)
        win.after(ms, update, ind)
    update(0)

def aperturaApp(name):
	try:
		confirm = tk.Tk()
		confirm.title(f"Espera - {name}")
		confirm.geometry("512x512")
		
		def abrir():
			panDeApertura = tk.Toplevel(confirm)
			panDeApertura.title(f"Abiendo aplicación - {name}")
			panDeApertura.geometry("1920x1080")
			Label(panDeApertura, text=f"Abriendo {name}", font = ("Arial", 32)).pack(pady = 10)
			progress = ttk.Progressbar(panDeApertura, orient="horizontal", length = 500, mode = "determinate")
			confirm.withdraw()
			openGif(re.flor, panDeApertura, 100, 700, 150)
			progress.pack(pady = 50)
			progress.start()
			def run_progress(i=0):
					if i <= 100:
							progress['value'] = i
							panDeApertura.update_idletasks()
							panDeApertura.after(40, run_progress, i+1)  # 40 ms ≈ 0.04 s
					else:
							progress.stop()
			progress.start()
			run_progress()
			panDeApertura.mainloop()
		# Pantalla de carga
		Button(confirm, text = "✨ Iniciar app ✨", font = ("Times", 24, "italic"), background = "#a4e68a", height = 1, width = 15, command = abrir).pack()
		confirm.mainloop()

	except Exception as ex: 
		print(f"Error: {ex}")
		messagebox.showerror("ERROR", "Hubo un error al ejecutar esta acción, informe de esto al desarrollador.")

def pronto(name):
	try:
		pant = tk.Tk()
		pant.title(f"Pronto... - {name}")
		pant.geometry("1920x1080")

		AdquiArt = Label(pant, anchor=W, text= "PRÓXIMAMENTE", font=("Arial", 32)).pack(pady=20)

		Label(pant, text= f"""Saludos, usuario de {name}.
Sabemos que esta función es importante,
pero actualmente está en desarrollo.""", font=("Arial", 20)).pack()
		
		Label(pant, text= "Se recomienda regresar a la pantalla principal hasta nuevo aviso.", fg="red", font=("Arial", 18, "bold")).pack(pady = 25)
		openGif(re.clubP, pant, 50, 1350, 80)
		openGif(re.chamba, pant, 100, 700, 300)

		pant.mainloop()
	except Exception as ex: 
		print(f"Error: {ex}")
		messagebox.showerror("ERROR", "Hubo un error al ejecutar esta acción, informe de esto al desarrollador.")
		sys("cls")

# pronto("ADQUISICIONES ARTQUISITIVAS")
# aperturaApp("ADQUISICIONES ARTQUISITIVAS")