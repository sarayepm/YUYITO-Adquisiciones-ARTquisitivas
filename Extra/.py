# import tkinter as tk
# import html2text

# h = html2text.HTML2Text()
# # Ignore converting links from HTML
# h.ignore_links = True
# print(h.handle("<p>Hello, <a href='https://www.google.com/earth/'>world</a>!"))
# print(h.handle("<p>Hello, <a href='https://www.google.com/earth/'>world</a>!"))

# # Don't Ignore links anymore, I like links
# h.ignore_links = False
# print(h.handle("<p>Hello, <a href='https://www.google.com/earth/'>world</a>!"))


# # from tkinter import ttk
# # import time

# def start_progress():
#     progress.start()

#     # Simulate a task that takes time to complete
#     for i in range(101):
#       # Simulate some work
#         time.sleep(0.05)  
#         progress['value'] = i
#         # Update the GUI
#         root.update_idletasks()  
#     progress.stop()

# root = tk.Tk()
# root.title("Progressbar Example")

# # Create a progressbar widget
# progress = ttk.Progressbar(root, orient="horizontal", length=100, mode="determinate")
# progress.pack(pady=20)

# # Button to start progress
# start_button = tk.Button(root, text="Start Progress", command=start_progress)
# start_button.pack(pady=10)
# root.mainloop()


# from win10toast_click import ToastNotifier
# import tkinter as tk
# import threading
# import time

# def mostrar_ventana():
#     print("¡Notificación clickeada! Mostrando ventana tkinter...")

#     # Crear una ventana simple con tkinter
#     ventana = tk.Tk()
#     ventana.title("Opciones de la Canción")
#     ventana.geometry("300x200")
    
#     etiqueta = tk.Label(ventana, text="La canción ha terminado.\n¿Qué deseas hacer?", font=("Arial", 12))
#     etiqueta.pack(pady=20)

#     boton1 = tk.Button(ventana, text="Reproducir otra", command=lambda: print("Otra canción"))
#     boton1.pack(pady=5)

#     boton2 = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
#     boton2.pack(pady=5)

#     ventana.mainloop()

# def enviar_notificacion():
#     toaster = ToastNotifier()
#     toaster.show_toast(
#         "Reproductor de Música",
#         "La canción ha terminado. Haz clic para ver más opciones.",
#         duration=1,
#         threaded=True,
#         callback_on_click=mostrar_ventana  # Aquí se llama a tkinter
#     )
# def iniciar_reproductor():
#     print("Reproductor iniciado...")
#     time.sleep(5)  # Simula reproducción de una canción
#     enviar_notificacion()

# # Iniciar reproductor en un hilo separado
# threading.Thread(target=iniciar_reproductor).start()

# # Mantén el programa corriendo hasta que termine la notificación
# while True:
#     time.sleep(1)


# import os
# from win10toast_click import ToastNotifier
# import threading
# import time

# # Ruta al archivo que quieres abrir
# ruta_archivo = "C:\\Users\\PROGRAMACION\\Desktop\\Yuyito\\App\\adquisiciones.ico"  # Usa doble \\ o raw strings

# def abrir_archivo():
#     print("Abriendo archivo...")
#     os.startfile(ruta_archivo)  # Esto abre el archivo con su app predeterminada

# def enviar_notificacion():
#     toaster = ToastNotifier()
#     toaster.show_toast(
#         "Documento listo",
#         "Haz clic para abrir el archivo PDF.",
#         duration=10,
#         threaded=True,
#         callback_on_click=abrir_archivo
#     )

# def tarea():
#     print("Simulando trabajo...")
#     time.sleep(5)  # Simula una tarea previa
#     enviar_notificacion()

# threading.Thread(target=tarea).start()

# while True:
#     time.sleep(1)

# from tkinter import *
# root = Tk()
# root.title('GfG')
# top = Toplevel()
# top.title('Python')
# root.mainloop()

# import tkinter as tk
# from tkhtmlview import HTMLLabel
# import markdown

# md_text = """
# # ¡Hola Mundo!
# Este es un **texto en Markdown** que será mostrado en Tkinter.

# - Lista
# - De
# - Elementos

# [Enlace a OpenAI](https://openai.com)
# """

# html = markdown.markdown(md_text)

# root = tk.Tk()
# root.title("Markdown en Tkinter")

# etiqueta = HTMLLabel(root, html=html)
# etiqueta.pack(padx=20, pady=20)

# root.mainloop()

# import datetime
# print(datetime.datetime.now())

# def mainPage(name):
#     root = tk.Tk()
#     root.title(f"Pronto... - {name}")
#     root.geometry("1280x540")

#     === Cargar GIF animado con Pillow ===
#     gif_path = r"C:\Users\PROGRAMACION\Downloads\Yuyito\App\media\flor.gif"

#     frames = []
#     try:
#         while True:
#             frame = ImageTk.PhotoImage(gif.copy())
#             frames.append(frame)
#             gif.seek(len(frames))  # pasa al siguiente frame
#     except EOFError:
#         pass  # no hay más frames

#     lbl_gif = tk.Label(root)
#     lbl_gif.pack()

#     def update(ind):
#         frame = frames[ind]
#         lbl_gif.config(image=frame)
#         ind = (ind + 1) % len(frames)  # bucle infinito
#         root.after(100, update, ind)   # 100ms = velocidad
#     update(0)

#     root.mainloop()
# mainPage("ADQUISICIONES ARTQUISITIVAS")

# import tkinter as tk
# from tkinter import ttk

# def boton_clicado():
#     print("¡Botón presionado!")

# # Crear la ventana principal
# root = tk.Tk()
# root.title("Botón Plano")

# # Crear un botón con estilo flat
# boton_plano = ttk.Button(root, text="Botón Plano", command=boton_clicado, style="Flat.TButton")

# # Definir el estilo "Flat.TButton" para que sea plano
# style = ttk.Style()
# style.configure("Flat.TButton",
#                 padding=5,
#                 relief="flat",  # Sin relieve o borde visible
#                 foreground="#333333", # Color del texto
#                 background="#EEEEEE") # Color de fondo

# # Crear el botón
# boton_plano.grid(padx=10, pady=10) # Posicionar el botón en la ventana

# # Iniciar el bucle principal de la aplicación
# root.mainloop()

# from winotify import Notification, audio

# from winotify import Notification

# toast = Notification(app_id="windows app",
#                      title="Winotify Test Toast",
#                      msg="New Notification!",
#                      icon=r"C:\Users\PROGRAMACION\Downloads\Yuyito\App\adquisiciones.ico")

# toast.show()

from winotify import Notification

toast = Notification(app_id="windows app", title="Winotify Test Toast", msg="New Notification!", icon=r"c:\path\to\icon.png")
toast.add_actions(label="open github",
                 launch="https://github.com/versa-syahptr/winotify/")

toast.show()