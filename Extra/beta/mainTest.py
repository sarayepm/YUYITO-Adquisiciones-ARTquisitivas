import tkinter as tk, time, random
import funcionesYClases, menu
from fpdf import FPDF
from tkinter import *; from plyer import *; from rich import *
# python.exe -m pip install --upgrade pip
# pip install plyer fpdf colorama rich win10toast_click

r = tk.Tk()
r.title('Prueba')
r.geometry("1000x500")
nombrePDF = tk.StringVar()
n = 0
def hacerPdf():
    global nombrePDF
    global n
    nomPDF = nombrePDF.get()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=16)
    pdf.cell(40, 10, "Hello World!")
    if nomPDF == True:
        pdf.output(f"{nomPDF}({n+1}).pdf")
    else:
        pdf.output(f"{nomPDF}.pdf")
    time.sleep(1)
    print(f"{nomPDF} ya está listo y descargado. :)")
    notification.notify(
        title = "¡Oye!",
        message = f"Tu archivo {nomPDF}.pdf ya está descargado, revisa en la carpeta del proyecto",
        app_name='Adquisiciones ARTquisitivas',
        app_icon='adquisiciones.ico',
        timeout=2,
        ticker='Ohno',
        toast=False
    )
    r.destroy()
entryPDF = tk.Entry(r,textvariable = nombrePDF, font=('calibre',10,'normal'))
button = tk.Button(r, text='Descargar pdf', width=25, command=hacerPdf)
# button2 = tk.Button(r, text='Abrir documento', command=r.destroy)
entryPDF.pack()
button.pack()
r.mainloop()