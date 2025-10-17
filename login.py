import time, tkinter as tk
from tkinter import *; from tkinter import ttk, messagebox; from rich import *; from PIL import Image, ImageTk; from os import system as sys;
from sqlfunci import *

def loginScreen(name):
  sys("cls")
  loginRu = tk.Tk()
  loginRu.title(f"Iniciar sesión - {name}")
  loginRu.geometry("1920x1080")
  
  rut_var   = tk.StringVar()
  ps_var    = tk.StringVar()
  email_var = tk.StringVar()
  user_var  = tk.StringVar()
  rut       = rut_var.get()
  passW     = ps_var.get()
  email     = email_var.get()
  userN     = user_var.get()

  Label(loginRu, text    = "INICIA SESION", font = ("Arial", 32)).pack(pady = 20)
  Label(loginRu, text    = "Ingrese su rut", font = ("Arial", 14)).pack()
  Entry(loginRu, width   = 25, font = ("Arial", 14), textvariable = rut_var).pack(pady = 5)
  Label(loginRu, text    = "Contraseña", font = ("Arial", 14)).pack(pady = 5)
  Entry(loginRu, width   = 25, font = ("Arial", 14), show = "*", textvariable = ps_var).pack()
  Button(loginRu, text   = "Iniciar sesion", width = 30, height = 2).place(x = 852, y = 270)

  def emailLogin(name):
    loginEm = tk.Tk()
    loginEm.geometry("1920x1080")
    loginEm.title(f"Iniciar sesión - {name}")
    Label(loginEm, text  = "INICIA SESION", font = ("Arial", 32)).pack(pady = 20)
    Label(loginEm, text  = "Ingrese su rut", font = ("Arial", 14)).pack()
    Entry(loginEm, width = 25, font = ("Arial", 14), textvariable = rut_var).pack(pady = 5)
    Label(loginEm, text  = "Contraseña", font = ("Arial", 14)).pack(pady = 5)
    Entry(loginEm, width = 25, font = ("Arial", 14), show = "*", textvariable = ps_var).pack()
    Button(loginEm, text = "Iniciar sesion", width = 30, height = 2).place(x = 852, y = 270)
    Button(loginEm, text = "Ingresar con usuario", relief = tk.FLAT, command = userLogin(name)).place(x = 910, y = 320)
    Button(loginEm, text = "Ingresar con rut", relief = tk.FLAT, command = loginEm.destroy()).place(x = 908, y = 350)
    loginEm.mainloop()

  def userLogin(name):
    loginUs = tk.Tk()
    loginUs.geometry("1920x1080")
    loginUs.title(f"Iniciar sesión - {name}")
    Label(loginUs, text  = "INICIA SESION", font = ("Arial", 32)).pack(pady = 20)
    Label(loginUs, text  = "Ingrese su rut", font = ("Arial", 14)).pack()
    Entry(loginUs, width = 25, font = ("Arial", 14), textvariable = rut_var).pack(pady = 5)
    Label(loginUs, text  = "Contraseña", font = ("Arial", 14)).pack(pady = 5)
    Entry(loginUs, width = 25, font = ("Arial", 14), show = "*", textvariable = ps_var).pack()
    Button(loginUs, text = "Iniciar sesion", width = 30, height = 2).place(x = 852, y = 270)
    Button(loginUs, text = "Ingresar con rut", relief = tk.FLAT, command = loginUs.destroy()).place(x = 908, y = 350)
    Button(loginUs, text = "Ingresar con correo", relief = tk.FLAT, command = emailLogin(name)).place(x = 910, y = 320)
    loginUs.mainloop()
  
  Button(loginRu, text   = "Ingresar con correo", relief = tk.FLAT, command = emailLogin(name)).place(x = 910, y = 320)
  Button(loginRu, text   = "Ingresar con usuario", relief = tk.FLAT, command = userLogin(name)).place(x = 908, y = 350)
  loginRu.mainloop()
  sys("cls")
loginScreen("ADQUISICIONES ARTQUISITIVAS")
sys("cls")