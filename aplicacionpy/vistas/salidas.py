
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from controladores.logicaSalidas import logicaSalidas



class salidas:
    def __init__(self,ventana):
        self.salida=logicaSalidas()
        self.ventana=ventana
        self.ventana.title("Salidas")
        self.ventana.geometry("1030x555")
        self.ventana.config(bg="slategrey")
        self.ventana.resizable(0,0)
        self.ventana.iconbitmap("imagenes/Salidas.ico")
        self.miframe2=LabelFrame(self.ventana, text="Salidas", font=('Times', 10,BOLD),padx=20,pady=20)
        self.miframe2.config(labelanchor=N,width=500)
        self.miframe2.grid(row=0,column=0,columnspan=3)
        Label(self.miframe2,text="Por favor escribir el codigo del producto para poder buscarlo",font=('Times', 10)).grid(row=0,columnspan=2,pady=5,sticky=W+E)
        Button(self.miframe2,text="Buscar",font=('Times', 10,BOLD),command=lambda: self.salida.buscarSalida(self.arbol1,self.entrada2.get())).grid(row=1,column=0)
        self.entrada2=Entry(self.miframe2,width=50)
        self.entrada2.grid(row=1,column=1)
        Button(self.miframe2,text="Añadir una salida", font=('Times', 10,BOLD),command=self.añadirsalida).grid(row=2,columnspan=2,pady=5,sticky=W+E)
        Button(self.miframe2,text="Eliminar una salida", font=('Times', 10,BOLD),command=lambda:self.salida.eliminarSalida(self.arbol1,self.arbol1.item(self.arbol1.selection())["text"])).grid(row=3,columnspan=2,pady=5,sticky=W+E)
        Button(self.miframe2,text="Editar una salida", font=('Times', 10,BOLD),command=self.editarsalida).grid(row=4,columnspan=2,pady=5,sticky=W+E)
        Button(self.miframe2,text="Refrescar", font=('Times', 10,BOLD),command=lambda:self.salida.llenarSalida(self.arbol1)).grid(row=5,columnspan=2,pady=5,sticky=W+E)
        Button(self.miframe2,text="Exportar salidas a un excel", font=('Times', 10,BOLD),command=self.pantallita2).grid(row=6,columnspan=2,pady=5,sticky=W+E)
        #lambda:self.salida.exportarSalidas("SELECT * FROM salidas",self.arbol1)
        self.arbol1=ttk.Treeview(self.ventana,columns=('#1','#2','#3','#4'))
        self.arbol1.grid(row=5,column=0,columnspan=2,padx=2)
        self.arbol1.heading("#0",text="id_salidas",anchor = CENTER)
        self.arbol1.heading("#1",text="Codigo",anchor = CENTER)
        self.arbol1.heading("#2",text="Nombre",anchor = CENTER)
        self.arbol1.heading("#3",text="Salidas",anchor=CENTER)
        self.arbol1.heading("#4",text="Fecha_salidas",anchor = CENTER)
        scroll=Scrollbar(self.ventana,command=self.arbol1.yview)
        scroll.grid(row=5,column=2,sticky="nsew")
        Button(self.ventana,text="Salir de la vista de salidas", font=('Times', 10,BOLD),command=self.ventana.destroy).grid(row=9,column=0,columnspan=2,sticky=W+E)
        self.salida.llenarSalida(self.arbol1)
        self.ventana.mainloop()

    def pantallita2(self):
      #Vista para poner nombre a listas
      self.pantallita2=Toplevel(self.ventana)
      self.pantallita2.geometry("300x200")
      self.pantallita2.title("Titulo de listas")
      self.pantallita2.config(bg="slategrey")
      self.pantallita2.resizable(0,0)
      self.pantallita2.iconbitmap("imagenes/escritura.ico")
      Label(self.pantallita2, text= "Por favor escribir un titulo", font=('Times', 10), bg="slategrey",fg="gray1").pack()
      Label(self.pantallita2, text= "para la lista", font=('Times', 10), bg="slategrey",fg="gray1").pack()
      Label(self.pantallita2, text= " ", bg="slategrey").pack()
      nombreSalidas=Entry(self.pantallita2, width=40)
      nombreSalidas.pack()
      Label(self.pantallita2, text= " ", bg="slategrey").pack()
      Button(self.pantallita2, text="Confirmar", font=('Times', 10), fg="gray1", command=lambda:self.salida.exportarSalidas("SELECT * FROM salidas",self.arbol1,nombreSalidas.get())).pack()
      Label(self.pantallita2, text= " ", bg="slategrey").pack()
      Button(self.pantallita2, text="Cancelar", font=('Times', 10), fg="gray1", command=self.pantallita2.destroy).pack()


    def añadirsalida(self):
      #Vista de la ventana añadir salidar
      self.añadirsalida=Toplevel(self.ventana)
      self.añadirsalida.geometry("400x530")
      self.añadirsalida.title("Añadir Salida")
      self.añadirsalida.config(bg="slategrey")
      self.añadirsalida.resizable(0,0)
      self.añadirsalida.iconbitmap("imagenes/Salidas.ico")
      Label(self.añadirsalida ,text="", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="Por favor llenar las siguientes casillas para",font=('Times',10,), fg="black", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="añadir una nueva salida", font=('Times',10,), fg="black", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="Codigo", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
      Cod_entry = Entry(self.añadirsalida, width = "40")
      Cod_entry.pack()
      Label(self.añadirsalida ,text="", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="Nombre", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
      Nom_entry = Entry(self.añadirsalida, width = "40")
      Nom_entry.pack()
      Label(self.añadirsalida ,text="", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="Salidas", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
      Sal_entry = Entry(self.añadirsalida, width = "40")
      Sal_entry.pack()
      Label(self.añadirsalida ,text="", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="No. factura", font=('Times',10,), fg="black", width = "15", height = "1", bg = "slateGray").pack()
      factura_entry = Entry(self.añadirsalida, width = "40")
      factura_entry.pack()
      Label(self.añadirsalida ,text="", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="Nombre del cliente", font=('Times',10,), fg="black", width = "15", height = "1", bg = "slateGray").pack()
      nombre_entry = Entry(self.añadirsalida, width = "40")
      nombre_entry.pack()
      Label(self.añadirsalida ,text="", bg = "slateGray").pack()
      Label(self.añadirsalida ,text="Telefono del cliente", font=('Times',10,), fg="black", width = "15", height = "1", bg = "slateGray").pack()
      tel_entry = Entry(self.añadirsalida, width = "40")
      tel_entry.pack()
      Label(self.añadirsalida ,text="", bg = "slateGray").pack()
      Button(self.añadirsalida,text="Confirmar",font=('Times',10,), fg="black",width = "12", height = "1", bg = "LightSkyBlue3", command=lambda: self.salida.añadirSalida(Cod_entry.get(),Nom_entry.get(),Sal_entry.get(),factura_entry.get(),nombre_entry.get(),tel_entry.get(),self.arbol1)).pack()
      Label(self.añadirsalida,text="", bg="slateGray" ).pack()
      Button(self.añadirsalida,text="Salir",font=('Times', 10,), fg="black",width = "12", height = "1", bg = "LightSkyBlue3", command=self.añadirsalida.destroy).pack()
    
    def editarsalida(self):
      #Vista de la ventana editar salida
      oldId1=self.arbol1.item(self.arbol1.selection())['text']
      if oldId1:
        self.editarsalida=Toplevel(self.ventana)
        self.editarsalida.geometry("400x415")
        self.editarsalida.title("Editar Salida")
        self.editarsalida.config(bg="slategrey")
        self.editarsalida.resizable(0,0)
        self.editarsalida.iconbitmap("imagenes/Salidas.ico")
        codigo=IntVar(self.editarsalida)
        Nombre=StringVar(self.editarsalida)
        salidas=IntVar(self.editarsalida)
        fecha=StringVar(self.editarsalida)
        codigo.set(self.arbol1.item(self.arbol1.selection())["values"][0])
        Nombre.set(self.arbol1.item(self.arbol1.selection())["values"][1])
        salidas.set(self.arbol1.item(self.arbol1.selection())["values"][2])
        fecha.set(self.arbol1.item(self.arbol1.selection())["values"][3])
        Label(self.editarsalida ,text="", bg = "slateGray").pack()
        Label(self.editarsalida ,text="Por favor llenar las siguientes casillas para",font=('Times',10,), fg="black", bg = "slateGray").pack()
        Label(self.editarsalida ,text="editar una salida", font=('Times',10,), fg="black", bg = "slateGray").pack()
        Label(self.editarsalida ,text="", bg = "slateGray").pack()
        Label(self.editarsalida ,text="Codigo del producto", font=('Times',10,), fg="black", width = "15", height = "1", bg = "slateGray").pack()
        id1_entry = Entry(self.editarsalida, width = "40", textvariable= codigo)
        id1_entry.pack()
        Label(self.editarsalida ,text="", bg = "slateGray").pack()
        Label(self.editarsalida ,text="Nombre", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
        Nomb_entry = Entry(self.editarsalida, width = "40", textvariable= Nombre)
        Nomb_entry.pack()
        Label(self.editarsalida ,text="", bg = "slateGray").pack()
        Label(self.editarsalida ,text="Salidas", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
        Sali_entry = Entry(self.editarsalida, width = "40", textvariable= salidas)
        Sali_entry.pack()
        Label(self.editarsalida ,text="", bg = "slateGray").pack()
        Label(self.editarsalida ,text="Fecha de salidas", font=('Times',10,), fg="black", width = "12", height = "1", bg = "slateGray").pack()
        Fec_entry = Entry(self.editarsalida, width = "40", textvariable= fecha)
        Fec_entry.pack()
        Label(self.editarsalida ,text="", bg = "slateGray").pack()
        Button(self.editarsalida,text="Confirmar",font=('Times',10,), fg="black",width = "12", height = "1", bg = "LightSkyBlue3", command=lambda:self.salida.editarSalida(id1_entry.get(),Nomb_entry.get(),Sali_entry.get(),Fec_entry.get(),oldId1,self.arbol1)).pack()
        Label(self.editarsalida,text="", bg="slateGray" ).pack()
        Button(self.editarsalida,text="Salir",font=('Times', 10,), fg="black",width = "12", height = "1", bg = "LightSkyBlue3", command=self.editarsalida.destroy).pack()
      else:
        messagebox.showerror(message="Por favor elija una salida para editar su información", title="ERROR")
        return
