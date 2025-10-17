import time, fpdf, rich, random, os, datetime,tkinter as tk
from tkinter import *; from tkinter import ttk, messagebox; from rich import *; from win10toast_click import ToastNotifier; from fpdf import *; from os import system as sys
def ordenDeCompra(name):
    try:
        orden = tk.Tk()
        orden.title(f"Generador de órden de compra - {name}")
        orden.geometry("1920x1080")
        progress = ttk.Progressbar(orden, orient = "horizontal", length = 250, mode = "determinate")

        def descargaOrden():
            progress.pack(pady = 10)
            progress.start()
            for i in range(101):
                time.sleep(0.04)  
                progress['value'] = i
                orden.update_idletasks()
            progress.stop()
            orden.destroy()

            # Crear pdf
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("helvetica", style="B", size=16)
            pdf.cell(40, 10, "ORDEN DE COMPRA")

            # Lo que va a diferenciar de documentos
            ahora = datetime.datetime.now()
            difA = ahora.strftime("%Y") # Definimos año de creación de documento
            difM = ahora.strftime("%m") # Definimos mes de creación de documento
            difD = ahora.strftime("%d") # Definimos día de creación de documento
            difH = ahora.strftime("%H") # Definimos hora de creación de documento
            difMin = ahora.strftime("%M") # Definimos minuto de creación de documento
            difS = ahora.strftime("%S") # Definimos segundo de creación de documento
            diferenciador = f"{difA}{difM}{difD}-{difH}{difMin}{difS}"
            # Va a poner 20250820-121900 (por ejemplo) después del nombre

            ordenName = f"Orden_de_compra_{diferenciador}"
            pdf.output(f"{ordenName}.pdf")

            # Apertura de documento
            def aperturaOrden():
                os.startfile(f"{ordenName}.pdf") # Va a buscar el documento para abrirlo

            time.sleep(1)
            print(f"Tu Orden de compra ya está listo y descargado. :)") # Mensaje en consola para desarrollador

            # Notificación para abrir el documento
            toasterO = ToastNotifier() # Invoca a la notificación de escritorio
            toasterO.show_toast (
                    "Documento listo",
                    "Haz clic para abrir el archivo PDF.",
                    duration=10,
                    callback_on_click = aperturaOrden # Al hacer click, abre el pdf
            )

        Label(orden, text = "↓↓↓ Descargue su orden de compra aquí.", fg = "#80e3e8", font = ("Arial", 30)).pack(pady = 10)
        Button(orden, text = "→ • Descargar", command = descargaOrden, width = 20, height = 2, fg = "Red", cursor = "hand2", overrelief = "flat").pack(pady = 10)
        orden.mainloop()
        sys("cls")
    except Exception as ex: 
        print(f"Error: {ex}")
        messagebox.showerror("ERROR", "Hubo un error al ejecutar esta acción, informe de esto al desarrollador.")

# ordenDeCompra("ADQUISICIONES ARTQUISITIVAS")