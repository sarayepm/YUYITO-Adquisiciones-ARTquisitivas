import time, tkinter as tk
from tkinter import *; from tkinter import ttk, messagebox; from rich import *; from PIL import Image, ImageTk; from os import system as sys; from extra import *
# from conexion import *; from login import *; from otrostrabajadores import *; from adquisiciones import *; from sqlfun import *; from admin import *

# python.exe -m pip install --upgrade pip
# pip install fpdf rich win10toast_click pillow winotify

def mainPage(name):
	try:
		pass
	except Exception as ex:
		print(f"Error: {ex}")
		messagebox.showerror("ERROR", "Hubo un error al ejecutar esta acción, informe de esto al desarrollador.")
# mainPage("ADQUISICIONES ARTQUISITIVAS")