
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from controladores.logicaP import *
from .entradas import entradas
from .salidas import salidas
from .clientes import clientes
class interfaz:
    def __init__(self,ventana,logicaProductos):
        #instancia del controlador logicaProductos
        self.logi=logicaProductos()
        #creando la interfaz
        self.ventana=ventana
        self.ventana.title("Inventario")
        self.ventana.geometry("1190x620")
        self.ventana.config(bg="Skyblue4")
        self.ventana.resizable(0,0)
        self.ventana.iconbitmap("imagenes/inventario_icon.ico")
        menubar1 = Menu(self.ventana)
        self.ventana.config(menu=menubar1)
        opciones1 = Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Crear perfil", command=self.crearperfil)
        opciones1.add_command(label="Cambiar color de fondo", command=self.colores)
        opciones1.add_command(label="Asistencia", command=self.asistencia)
        menubar1.add_cascade(label="Configuraciones", menu=opciones1)
        opciones2 = Menu(menubar1, tearoff=0)
        opciones2.add_command(label="Ordenar productos de manera ascendente en base a su cantidad", command=lambda: self.logi.OrdenarAsc(self.tree))
        opciones2.add_command(label="Ordenar productos de manera descendente en base a su cantidad", command=lambda: self.logi.Ordenardesc(self.tree))
        menubar1.add_cascade(label="Ordenar", menu=opciones2) 
        opciones3 = Menu(menubar1, tearoff=0)
        opciones3.add_command(label="Ver clientes", command=self.CLIENTES)
        menubar1.add_cascade(label="Clientes", menu=opciones3) 
        #frame (buscar un producto)
        frame=LabelFrame(self.ventana, text="Ver productos", font=('Times', 10,BOLD),padx=20,pady=20)
        frame.config(labelanchor=N,width=500)
        frame.grid(row=0,column=0,columnspan=3)
        Label(frame,text="Por favor escribir el codigo del producto para poder buscarlo",font=('Times', 10)).grid(row=0,columnspan=2,pady=5,sticky=W+E)
        Label(frame,text="Codigo:",font=('Times', 10)).grid(row=1,column=0)
        self.entrada=Entry(frame,width=50)
        self.entrada.focus()
        self.entrada.grid(row=1,column=1)
        Button(frame,text="Buscar este producto", font=('Times', 10,BOLD),command=lambda: self.logi.consultar(self.tree,self.entrada.get())).grid(row=2,columnspan=2,pady=5,sticky=W+E)
        Button(frame,text="Refrescar", font=('Times', 10,BOLD),command=lambda: self.logi.llenarTabla(self.tree)).grid(row=3,columnspan=2,pady=5,sticky=W+E)
        Button(frame,text="Entradas",font=('Times', 10,BOLD), command=self.ENTRADA).grid(row=4,columnspan=2,pady=5,sticky=W+E)
        Button(frame,text="Salidas",font=('Times', 10,BOLD), command=self.SALIDAS).grid(row=5,columnspan=2,pady=5,sticky=W+E)
        Button(frame,text="Exportar lista de productos a excel",font=('Times', 10,BOLD),command=self.pantallita).grid(row=6,columnspan=2,pady=5,sticky=W+E)
        #tabla de datos
        #lambda:self.logi.exportarTabla("SELECT * FROM productos",self.tree)
        self.tree=ttk.Treeview(self.ventana,columns=('#1','#2','#3','#4','#5','#6'))
        self.tree.column('#0',width=165)
        self.tree.column('#1',width=165)
        self.tree.column('#2',width=165)
        self.tree.column('#3',width=165)
        self.tree.column('#4',width=165)
        self.tree.column('#5',width=165)
        self.tree.column('#6',width=165)
        self.tree.grid(row=5,column=0,columnspan=2,padx=2)
        #titulo en las columnas de la tabla
        self.tree.heading("#0",text="Codigo",anchor = CENTER)
        self.tree.heading("#1",text="Nombre",anchor = CENTER)
        self.tree.heading("#2",text="Precio",anchor = CENTER)
        self.tree.heading("#3", text="Costo",anchor=CENTER)
        self.tree.heading("#4",text="Cantidad",anchor = CENTER)
        self.tree.heading("#5",text="Entradas",anchor = CENTER)
        self.tree.heading("#6",text="Salidas",anchor=CENTER)
        #self.tree.heading("#6",text="Precio total",anchor = CENTER)
        #botones
        Button(self.ventana,text="Borrar un producto", font=('Times', 10,BOLD),command=lambda: self.logi.eliminar(self.tree.item(self.tree.selection())["text"],self.tree)).grid(row=7,column=0,sticky=W+E)
        Button(self.ventana,text="Editar un producto",font=('Times', 10,BOLD),command=self.formulario_editar).grid(row=7,column=1,sticky=W+E)
        Button(self.ventana,text="Insertar un producto", font=('Times', 10,BOLD),command=self.formulario).grid(row=8,column=0,columnspan=2,sticky=W+E)
        Button(self.ventana,text="Salir del inventario", font=('Times', 10,BOLD),command=self.cerrar_sf).grid(row=9,column=0,columnspan=2,sticky=W+E)
        #scroll para tabla
        scroll=Scrollbar(self.ventana,command=self.tree.yview)
        scroll.grid(row=5,column=2,sticky="nsew")
        self.logi.llenarTabla(self.tree)

    def formulario_editar(self):
      #Vista de el formulario editar
      try:
        oldNombre=self.tree.item(self.tree.selection())['values'][0]
        self.formulario_editar=Toplevel(self.ventana)
        self.formulario_editar.geometry("680x600")
        self.formulario_editar.title("Formulario para editar un producto")
        self.formulario_editar.config(bg="Skyblue4")
        self.formulario_editar.resizable(0,0)
        self.formulario_editar.iconbitmap("imagenes/formulario_icon.ico")     
        nombre=StringVar(self.formulario_editar)
        precio=IntVar(self.formulario_editar)
        costo=IntVar(self.formulario_editar)
        cantidad=IntVar(self.formulario_editar)
        entradas=IntVar(self.formulario_editar)
        salidas=IntVar(self.formulario_editar)
        nombre.set(self.tree.item(self.tree.selection())["values"][0])
        precio.set(self.tree.item(self.tree.selection())["values"][1])
        costo.set(self.tree.item(self.tree.selection())["values"][2])
        cantidad.set(self.tree.item(self.tree.selection())["values"][3])
        entradas.set(self.tree.item(self.tree.selection())["values"][4])
        salidas.set(self.tree.item(self.tree.selection())["values"][5])
        main_title = Label(self.formulario_editar, text = "Por favor llenar las casillas para editar el producto", font = ("Times", 12), bg="Skyblue4", fg = "black")
        main_title.grid(row=0,column=1)
        #Codigo_label = Label(self.formulario_editar, text = "Codigo", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
        #Codigo_label.grid(row=1,column=0,pady=25,sticky=W+E, padx=60)
        Nombre_label = Label(self.formulario_editar, text = "Nombre", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
        Nombre_label.grid(row=1,column=0,pady=25,sticky=W+E, padx=60)
        Precio_label = Label(self.formulario_editar, text = "Precio", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
        Precio_label.grid(row=2,column=0,pady=25,sticky=W+E, padx=60)
        Costo_label = Label(self.formulario_editar, text = "Costo", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
        Costo_label.grid(row=3,column=0,pady=25,sticky=W+E, padx=60)
        Cantidad_label = Label(self.formulario_editar, text = "Cantidad",font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
        Cantidad_label.grid(row=4,column=0,pady=25,sticky=W+E, padx=60)
        entradas_label = Label(self.formulario_editar, text = "Entradas", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
        entradas_label.grid(row=5,column=0,pady=25,sticky=W+E , padx=60)
        salidas_label = Label(self.formulario_editar, text = "Salidas", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
        salidas_label.grid(row=6,column=0,pady=25,sticky=W+E, padx=60)
        #Codigo_entry  = Entry(self.formulario_editar,  width = "40", textvariable=codigo)
        Nombre_entry  = Entry(self.formulario_editar,  width = "40", textvariable=nombre)
        Precio_entry = Entry(self.formulario_editar,   width = "40",  textvariable=precio)
        Costo_entry = Entry(self.formulario_editar,   width = "40", textvariable=costo)
        Cantidad_entry = Entry(self.formulario_editar,  width = "40", textvariable=cantidad)
        entradas_entry = Entry(self.formulario_editar, width = "40",  textvariable=entradas)
        Salidas_entry = Entry(self.formulario_editar,  width = "40",  textvariable=salidas)
        Nombre_entry.grid(row=1,column=1,pady=25,sticky=W+E, padx=50)
        Precio_entry.grid(row=2,column=1,pady=25,sticky=W+E, padx=50)
        Costo_entry.grid(row=3,column=1,pady=25,sticky=W+E, padx=50)
        Cantidad_entry.grid(row=4,column=1,pady=25,sticky=W+E, padx=50)
        entradas_entry.grid(row=5,column=1,pady=25,sticky=W+E, padx=50)
        Salidas_entry.grid(row=6,column=1,pady=25,sticky=W+E, padx=50)
        Button(self.formulario_editar,text="Confirmar modificacion", command=lambda:self.logi.modificar(Nombre_entry.get(),Cantidad_entry.get(),Precio_entry.get(),Costo_entry.get(),entradas_entry.get(),Salidas_entry.get(),oldNombre,self.tree), font=('Times', 10,BOLD), fg="gray1",width = "15", height = "0", bg = "white",).grid(row=8,column=1,sticky=W+E)
        Label(self.formulario_editar,text="", bg="Skyblue4" ).grid(row=9,column=1,sticky=W+E)
        Button(self.formulario_editar,text="Cancelar",font=('Times',10,BOLD), fg="gray1",width = "15", height = "0", bg = "white", command=self.formulario_editar.destroy).grid(row=10,column=1,sticky=W+E)
      except IndexError as e:
        messagebox.showerror(message="Por favor seleccione el producto a editar.",title="Mensaje del Sistema")  
    
    def pantallita(self):
      #Vista para poner nombre a listas
      self.pantallita=Toplevel(self.ventana)
      self.pantallita.geometry("300x200")
      self.pantallita.title("Titulo de listas")
      self.pantallita.config(bg="Skyblue4")
      self.pantallita.resizable(0,0)
      self.pantallita.iconbitmap("imagenes/escritura.ico")
      Label(self.pantallita, text= "Por favor escribir un titulo", font=('Times', 10), bg="Skyblue4",fg="gray1").pack()
      Label(self.pantallita, text= "para la lista", font=('Times', 10), bg="Skyblue4",fg="gray1").pack()
      Label(self.pantallita, text= " ", bg="Skyblue4").pack()
      nombre_Tabla = Entry(self.pantallita, width=40)
      nombre_Tabla.pack()
      Label(self.pantallita, text= " ", bg="Skyblue4").pack()
      Button(self.pantallita, text="Confirmar", font=('Times', 10), fg="gray1", command=lambda:self.logi.exportarTabla("SELECT * FROM productos",self.tree,nombre_Tabla.get())).pack()
      Label(self.pantallita, text= " ", bg="Skyblue4").pack()
      Button(self.pantallita, text="Cancelar", font=('Times', 10), fg="gray1", command=self.pantallita.destroy).pack()

    def formulario(self):
      #Vista de el formulario añadir
      self.formulario=Toplevel(self.ventana)
      self.formulario.geometry("680x640")
      self.formulario.title("Formulario para añadir producto")
      self.formulario.config(bg="Skyblue4")
      self.formulario.resizable(0,0)
      self.formulario.iconbitmap("imagenes/formulario_icon.ico")
      main_title = Label(self.formulario, text = "Por favor llenar las casillas para añadir un nuevo producto", font = ("Times", 12), bg="Skyblue4", fg = "black")
      main_title.grid(row=0,column=1)
      Codigo_label = Label(self.formulario, text = "Codigo", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
      Codigo_label.grid(row=1,column=0,pady=25,sticky=W+E, padx=60)
      Nombre_label = Label(self.formulario, text = "Nombre", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
      Nombre_label.grid(row=2,column=0,pady=25,sticky=W+E, padx=60)
      Precio_label = Label(self.formulario, text = "Precio", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
      Precio_label.grid(row=3,column=0,pady=25,sticky=W+E, padx=60)
      Costo_label = Label(self.formulario, text = "Costo", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
      Costo_label.grid(row=4,column=0,pady=25,sticky=W+E, padx=60)
      Cantidad_label = Label(self.formulario, text = "Cantidad",font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
      Cantidad_label.grid(row=5,column=0,pady=25,sticky=W+E, padx=60)
      entradas_label = Label(self.formulario, text = "Entradas", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
      entradas_label.grid(row=6,column=0,pady=25,sticky=W+E , padx=60)
      salidas_label = Label(self.formulario, text = "Salidas", font=('Times', 12,BOLD), bg="Skyblue4",fg="gray1")
      salidas_label.grid(row=7,column=0,pady=25,sticky=W+E, padx=60)
      Codigo_entry  = Entry(self.formulario, width = "40")
      Nombre_entry  = Entry(self.formulario, width = "40")
      Precio_entry = Entry(self.formulario,width = "40")
      Costo_entry = Entry(self.formulario,width = "40")
      Cantidad_entry = Entry(self.formulario,width = "40")
      entradas_entry = Entry(self.formulario,width = "40")
      Salidas_entry = Entry(self.formulario,width = "40")
      Codigo_entry.grid(row=1,column=1,pady=25,sticky=W+E, padx=50)
      Nombre_entry.grid(row=2,column=1,pady=25,sticky=W+E, padx=50)
      Precio_entry.grid(row=3,column=1,pady=25,sticky=W+E, padx=50)
      Costo_entry.grid(row=4,column=1,pady=25,sticky=W+E, padx=50)
      Cantidad_entry.grid(row=5,column=1,pady=25,sticky=W+E, padx=50)
      entradas_entry.grid(row=6,column=1,pady=25,sticky=W+E, padx=50)
      Salidas_entry.grid(row=7,column=1,pady=25,sticky=W+E, padx=50)
      Button(self.formulario,text="Añadir nuevo producto", font=('Times', 10,BOLD), fg="gray1",width = "40", height = "1", bg = "white",command=lambda:self.logi.insertar(Codigo_entry.get(),Nombre_entry.get(),Cantidad_entry.get(),Precio_entry.get(),Costo_entry.get(),entradas_entry.get(),Salidas_entry.get(),self.tree)).grid(row=8,column=1,sticky=W+E)
      Label(self.formulario,text="", bg="Skyblue4" ).grid(row=9,column=1,sticky=W+E)
      Button(self.formulario,text="Cerrar formulario",font=('Times', 10,BOLD), fg="gray1",width = "40", height = "1", bg = "white", command=self.formulario.destroy).grid(row=10,column=1,sticky=W+E)

    def crearperfil(self):
      #Vista de la ventana crear perfil
      self.crearperfil=Toplevel(self.ventana)
      self.crearperfil.geometry("800x520")
      self.crearperfil.title("Crear nuevo usuario")
      self.crearperfil.config(bg="light sea green")
      self.crearperfil.resizable(0,0)
      self.crearperfil.iconbitmap("imagenes/Crear.ico")
      Label(self.crearperfil,text="Crear Nuevo Usuario",font=('Times', 25,BOLD), bg='light sea green', fg="snow",height="3",padx=10,width="450").pack()
      #self.img=PhotoImage(file="imagenes/images.gif")
      #self.img=self.img.subsample(3,3)
      #self.lblImage=Label(self.crearperfil,image=self.img)
      #self.lblImage.pack()
      Label(self.crearperfil,text="", bg='light sea green', fg="snow" ).pack()
      Label(self.crearperfil, text="Ingrese el nombre de usuario y la contraseña que usted desea poner.",font=('Times', 12,BOLD), bg='light sea green', fg="snow").pack()
      Label(self.crearperfil,text="", bg='light sea green', fg="snow" ).pack()
      Label(self.crearperfil,text="Nombre de usuario",font=('Times',13,BOLD), bg='light sea green', fg="snow",height="3").pack()
      newuser_entry=Entry(self.crearperfil, font=("Times",10,BOLD), width = "40")
      newuser_entry.config(justify="center")
      newuser_entry.pack()
      Label(self.crearperfil,text="", bg='light sea green', fg="snow" ).pack()
      Label(self.crearperfil,text="Contraseña",font=('Times',13,BOLD), bg='light sea green', fg="snow",height="3").pack()
      newpass_entry=Entry(self.crearperfil, font=("Times",10,BOLD), width = "40")
      newpass_entry.config(show="*",justify="center")
      newpass_entry.pack()
      Label(self.crearperfil,text="", bg='light sea green', fg="black" ).pack()
      Button(self.crearperfil,text="Guardar", font=("Times",13), bg='light sea green', fg="snow", width= "12", height= "1",command=lambda:self.logi.Crear_usuario(newuser_entry.get(),newpass_entry.get())).pack()
      Label(self.crearperfil,text="", bg='light sea green', fg="black" ).pack()
      Button(self.crearperfil,text="Salir",font=('Times', 13), fg="snow", width = "12", height = "1", bg = "light sea green", command=self.crearperfil.destroy).pack()
   

    def cerrar_sf(self):
      Pregunta=messagebox.askquestion(message="¿Esta seguro que desea salir del inventario?",title="Mensaje del Sistema")
      if Pregunta=="yes":
        self.ventana.destroy()

    def asistencia(self):
      #Vista de la ventana de asistencia
      self.asistencia=Toplevel(self.ventana)
      self.asistencia.geometry("640x200")
      self.asistencia.title("Asistencia")
      self.asistencia.config(bg="light sea green")
      self.asistencia.resizable(0,0)
      self.asistencia.iconbitmap("imagenes/ayuda.ico")
      Label(self.asistencia,text="", bg='light sea green' ).pack()
      Label(self.asistencia, text="Para recibir asistencia o ayuda acerca del software, escribir a los siguientes correos:", bg='light sea green', font=('Times',12), fg="snow").pack()
      Label(self.asistencia, text="emmanuelpp21@gmail.com herjosuee@hotmail.com", bg='light sea green', font=('Times',12), fg="snow").pack()
      Label(self.asistencia,text="", bg='light sea green' ).pack()
      Button(self.asistencia,text="Salir",font=('Times', 12,BOLD), fg="snow", width = "12", height = "1", bg = "light sea green", command=self.asistencia.destroy).pack()
      

    def colores(self):
      #Vista de la ventana cambiar color de fondo
      self.colores=Toplevel(self.ventana)
      self.colores.geometry("400x420")
      self.colores.title("Colores")
      self.colores.config(bg="light sea green")
      self.colores.resizable(0,0)
      self.colores.iconbitmap("imagenes/colores.ico")
      Label(self.colores,text="", bg='light sea green' ).pack()
      Button(self.colores ,text="Rojo", font=('Times',8,BOLD), fg="black", width = "12", height = "1", bg = "SlateGray1", command=self.fijarrojo).pack()
      Label(self.colores,text="", bg='light sea green' ).pack()
      Button(self.colores ,text="Azul", font=('Times',8,BOLD), fg="black", width = "12", height = "1", bg = "SlateGray1", command=self.fijarazul).pack()
      Label(self.colores,text="", bg='light sea green' ).pack() 
      Button(self.colores ,text="Verde", font=('Times',8,BOLD), fg="black", width = "12", height = "1", bg = "SlateGray1", command=self.fijarverde).pack()
      Label(self.colores,text="", bg='light sea green' ).pack() 
      Button(self.colores ,text="Amarillo", font=('Times',8,BOLD), fg="black", width = "12", height = "1", bg = "SlateGray1", command=self.fijaramarillo).pack()
      Label(self.colores,text="", bg='light sea green' ).pack() 
      Button(self.colores ,text="Verde mar claro", font=('Times',8,BOLD), fg="black", width = "12", height = "1", bg = "SlateGray1", command=self.fijarverdemarino).pack()
      Label(self.colores,text="", bg='light sea green' ).pack() 
      Button(self.colores ,text="Cafe", font=('Times',8,BOLD), fg="black", width = "12", height = "1", bg = "SlateGray1", command=self.fijarcafe).pack()
      Label(self.colores,text="", bg='light sea green' ).pack() 
      Button(self.colores ,text="Blanco", font=('Times',8,BOLD), fg="black", width = "12", height = "1", bg = "SlateGray1", command=self.fijarblanco).pack()
      Label(self.colores,text="", bg='light sea green' ).pack() 
      Button(self.colores ,text="Regresar a el color predeterminado", font=('Times',8,BOLD), fg="black", width = "26", height = "1", bg = "SlateGray1", command=self.fijarnormal).pack()
      Label(self.colores,text="", bg='light sea green' ).pack()
      Button(self.colores,text="Salir",font=('Times', 8,BOLD), fg="black",width = "12", height = "1", bg = "SlateGray1", command=self.colores.destroy).pack()
      
    def fijarrojo(self):
      self.ventana.configure(background="red")
    def fijarazul(self):
      self.ventana.configure(background="blue")
    def fijarverde(self):
      self.ventana.configure(background="green")
    def fijaramarillo(self):
      self.ventana.configure(background="yellow")
    def fijarverdemarino(self):
      self.ventana.configure(background="light sea green")
    def fijarcafe(self):
      self.ventana.configure(background="brown")
    def fijarblanco(self):
      self.ventana.configure(background="white")
    def fijarnormal(self):
      self.ventana.configure(background="Skyblue4")

    def ENTRADA(self):
      vent=Tk()
      self.tablaEntradas=entradas(vent)
    
    def SALIDAS(self):
      vent2=Tk()
      self.tablaSalidas=salidas(vent2)

    def CLIENTES(self):
      vent3=Tk()
      self.tablaClientes=clientes(vent3)
            
if __name__ == '__main__':
    window = Tk()
    application = interfaz(window,logicaProductos)
    window.mainloop()