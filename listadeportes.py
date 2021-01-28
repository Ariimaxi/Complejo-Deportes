from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title("Complejo Deportes")

# --------------------------- BASE DE DATOS SQLITE--------------------#
def ConexionBBDD():
    miConexion = sqlite3.connect("USUARIOS COMPLEJO DEPORTES.db")

    miCursor = miConexion.cursor()

    try:
        miCursor.execute(
            """
             CREATE TABLE DATOS USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_USUARIO VARCHAR(50), APELLIDO_USUARIO VARCHAR (50), DNI_USUARIO VARCHAR (20), DIRECCION VARCHAR(50), COMENTARIOS VARCHAR (100)
             
             """
        )

        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("Atencion!", "La BBDD ya existe")


def SalirAplicacion():
    valor = messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")

    if valor == "yes":
        root.destroy()


# -------------------- Limpiar CAMPOS ----------------------------#


def limpiarCampos():

    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDNI.set("")
    miDireccion.set("")
    textoComentario.delete(1.0, END)


# -------------------- FUNCIONES DEL CRUD  --------------------------------#
def crear():
    miConexion = sqlite3.connect("USUARIOS COMPLEJO DEPORTES.db")

    miCursor = miConexion.cursor()

    miCursor.execute(
        "INSERT INTO DATOSUSUARIOS VALUES (NULL, '"
        + miNombre.get()
        + "' , '"
        + miApellido.get()
        + "' , '"
        + miDNI.get()
        + "' , '"
        + miDireccion.get()
        + "' , '"
        + textoComentario.get("1.0", END)
        + "')"
    )

def leer():

    miConexion = sqlite3.connect("Usuarios_Complejo_Deportes.db")

    miCursor = miConexion.cursor()

    miCursor.execute ("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())

    elUsuario=miCursor.fetchall()

    for usuario in elUsuario: 

        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miDNI.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()


def actualizar():

     miConexion = sqlite3.connect("USUARIOS COMPLEJO DEPORTES.db")

     miCursor = miConexion.cursor()

     miCursor.execute(
        "UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=' " + miNombre.get() + "' , APELLIDO='" + miApellido.get() + "', DNI='" + miDNI.get() + "', DIRECCION='" + miDireccion.get() + "', COMENTARIOS= '"+ textoComentario.get("1.0", END) + "' WHERE ID=" + miID.get())
    )


def eliminar():

    miConexion = sqlite3.connect("USUARIOS COMPLEJO DEPORTES.db")

     miCursor = miConexion.cursor()

     miCursor.execute(
        "DELETE FROM DATOSUSUARIOS  WHERE ID=" + miID.get())

     miConexion.commit()

     messagebox.showinfo("BBDD", "Registro borrado con exito")



    
    
# -------------------Elementos BARRA SUPERIOR--------------------#
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=ConexionBBDD)
bbddMenu.add_command(label="Salir", command=SalirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


# ----------------------Comienzo de CAMPOS---------------------#

miFrame = Frame(root)
miFrame.pack()

miID = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miDNI = StringVar()
miDireccion = StringVar()

cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="black")

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDNI = Entry(miFrame, textvariable=miDNI)
cuadroDNI.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# ---------------------- LABELS -------------------------#

idLabel = Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

NombreLabel = Label(miFrame, text="Nombre:")
NombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel = Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

DNILabel = Label(miFrame, text="Documento:")
DNILabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

DireccionLabel = Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

ComentariosLabel = Label(miFrame, text="Comentarios:")
ComentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# -------------------------- BOTONES -------------------------------#

miFrame2 = Frame(root)
miFrame2.pack()

botonCrear = Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer = Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar = Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar = Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()