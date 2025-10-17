from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from usuarios import *
from conexion import *


class formularioUsuario:

    global ventana
    venta = None

    global textBoxUsuario
    textBoxUsuario = None

    global textBoxPassword
    textBoxPassword = None

    global textBoxNombre
    textBoxNombre = None

    global tree
    tree = None


def formulario():
    global ventana
    global textBoxUsuario
    global textBoxPassword
    global textBoxNombre
    global tree
    
    try:
        ventana = Tk() # Crea la ventana
        ventana.geometry("1000x300") # Muestra la ventana de dicho tamaño
        ventana.title("Formulario Pyhton") # Nombre de la app
        ventana.iconbitmap(default="adquisiciones.ico") # Ícono

        groupBox = LabelFrame(ventana,text="Datos de Usuarios", padx=5, pady=5) #Le da nombre al widget donde estarán los datos
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        labelUsuario= Label(groupBox, text="Usuario", width=13, font=("arial",12)).grid(row=0, column=0)
        textBoxUsuario = Entry(groupBox)
        textBoxUsuario.grid(row=0, column=1)

        labelPassword= Label(groupBox, text="Password", width=13, font=("arial",12)).grid(row=1, column=0)
        textBoxPassword = Entry(groupBox)
        textBoxPassword.grid(row=1, column=1)

        labelNombre= Label(groupBox, text="Nombre", width=13, font=("arial",12)).grid(row=2, column=0)
        textBoxNombre = Entry(groupBox)
        textBoxNombre.grid(row=2, column=1)
                    
        Button(groupBox,text="Guardar", width=10, command=guardarRegistro).grid(row=4, column=0)
        Button(groupBox,text="Modificar", width=10, command=modificarRegistro).grid(row=4, column=1)
        Button(groupBox,text="Eliminar", width=10, command=eliminarRegistro).grid(row=4, column=2)

        groupBox=LabelFrame(ventana, text="Lista de Usuarios",padx=5, pady=5,)
        groupBox.grid(row=0, column=1, padx=5, pady=5)

        tree = ttk.Treeview(groupBox, columns=("Usuario","Password","Nombre"),show='headings', height=5,)       
        tree.column("#1", anchor=W)
        tree.heading("#1", text="Usuario")
        tree.column("#2", anchor=W)
        tree.heading("#2", text="Password")
        tree.column("#3", anchor=W)
        tree.heading("#3", text="Nombre")
                                
        # Agregar datos a la tabla
        # mostrar tabla

        for row in cusuarios.mostrarUsuarios():
            tree.insert("","end", values=row)
        
        # ejecutar la función de hacer click y mostrar los resultados en los entry
        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)
        
        tree.pack()

        ventana.mainloop()
    except ValueError as error:
        print("Error al mostrar la interfa, error: {}".format(error))

def guardarRegistro():
    global textBoxUsuario, textBoxPassword, textBoxNombre
    try:
        if textBoxUsuario is None or textBoxPassword is None or textBoxNombre is None:
            print ("Los Widgets no estan inicializados")
            return
        
        usuario = textBoxUsuario.get()
        password = textBoxPassword.get()
        nombre = textBoxNombre.get()
        cusuarios.ingresarUsuarios(usuario,password, nombre)
        messagebox.showinfo("Información", "Los datos fueron guardados")

        actualizarTreeView()

        #limpiar campos
        textBoxUsuario.delete(0,END)
        textBoxPassword.delete(0,END)
        textBoxNombre.delete(0,END)
    except ValueError as error:
        print ("Error al ingresar los datos {}".format(error))


def actualizarTreeView():
    global tree

    try:
        #Borrar todos los elementos actuales del treeview
        tree.delete(*tree.get_children())
        # obtener los nuevos valores
        datos = cusuarios.mostrarUsuarios()

        # insertar los nuevos datos en el treeview

        for row in cusuarios.mostrarUsuarios():
            tree.insert("","end",values=row)
            
    except ValueError as error:
        print("Error al actualizar la tabla{}".format(error))

def seleccionarRegistro(event):
    try:

        #obtener el id del elemento seleccionado
        itemSeleccionado = tree.focus()
        if itemSeleccionado:
            # obtener los valores por columnas
            values = tree.item(itemSeleccionado)['values']
            # Establecer los valores en los widgets
            
            textBoxUsuario.delete(0,END)
            textBoxUsuario.insert(0, values[0])

            textBoxPassword.delete(0,END)
            textBoxPassword.insert(0, values[1])
            
            textBoxNombre.delete(0,END)
            textBoxNombre.insert(0, values[2])
    except ValueError as error:
        print ("Error al seleccionar registro {}".format(error))

def modificarRegistro():
    global textBoxUsuario, textBoxPassword, textBoxNombre
    try:
        if textBoxUsuario is None or textBoxPassword is None or textBoxNombre is None:
            print ("Los Widgets no estan inicializados")
            return
        
        usuario = textBoxUsuario.get()
        password = textBoxPassword.get()
        nombre = textBoxNombre.get()
        cusuarios.modificarUsuarios(usuario,password, nombre)
        messagebox.showinfo("Información", "Los datos fueron actualizados")

        actualizarTreeView()

        #limpiar campos
        textBoxUsuario.delete(0,END)
        textBoxPassword.delete(0,END)
        textBoxNombre.delete(0,END)
    except ValueError as error:
        print ("Error al modificar los datos {}".format(error))

def eliminarRegistro():
    global textBoxUsuario, textBoxPassword, textBoxUsuario
    try:
        if textBoxUsuario is None:
            print ("Los Widgets no estan inicializados")
            return
        
        usuario = textBoxUsuario.get()
        cusuarios.eliminarUsuarios(usuario)
        messagebox.showinfo("Información", "Los datos fueron eliminados")

        actualizarTreeView()

        #limpiar campos
        textBoxUsuario.delete(0,END)
        textBoxPassword.delete(0,END)
        textBoxNombre.delete(0,END)
    except ValueError as error:
        print ("Error al eliminar los datos {}".format(error))



formulario()


