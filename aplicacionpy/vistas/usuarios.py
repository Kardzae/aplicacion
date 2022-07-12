
from tkinter import *

from tkinter.font import BOLD
from controladores.logicaUsuarios import Usuarios

class User():
    def __init__(self,ventana):
        #creando la ventana para el login
        self.logiUser=Usuarios()        
        self.ventana=ventana
        #Poner direccion en donde se encuentra la imagen para poner el icono en la ventana
        self.ventana.iconbitmap("imagenes/login_icon.ico")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.title("Iniciar Sesion")
        self.ventana.geometry("800x570")
        self.ventana.resizable(0,0)
        #variables de nombre de usuario y contraseña
        self.nombre=StringVar()
        self.password=StringVar()
        #frame dentro de la ventana
        self.frame=Frame(self.ventana ,height = 50,  bd=0, bg='#fcfcfc')
        self.frame.pack(expand=True,fill='both',padx=10,pady=10)
        self.frame2=Frame(self.ventana ,height = 50,  bd=0, bg='#fcfcfc')
        self.frame2.pack(expand=True,fill='both',padx=20,pady=20)
        self.mensaje=Label(self.frame2,padx=300,font=5,fg="red" ,height = 50,  bd=0, bg='#fcfcfc')
        self.mensaje.grid(row=0,column=5,columnspan=2,sticky=W+E)
        #título del login
        Label(self.frame,text="Iniciar Sesion",font=('Times', 25,BOLD), bg='#fcfcfc', fg="black",height="3",padx=10,width="450").pack()
        #imagen
        imagen=PhotoImage(file="imagenes/iconoED.gif")
        imagen=imagen.subsample(3,3)
        lblImage=Label(self.frame,image=imagen)
        lblImage.pack()
        Label(self.frame,text="Nombre de usuario",font=('Times',15,BOLD), bg='#fcfcfc', fg="black",height="3").pack()
        #entradas de texto
        self.entryUser=Entry(self.frame,font=("Times",12),textvariable=self.nombre)
        self.entryUser.config(justify="center")
        self.entryUser.pack()
        Label(self.frame,text="Inserte su contraseña",font=("Times",15,BOLD), bg='#fcfcfc', fg="black",height="3").pack()
        self.entryPassword=Entry(self.frame,font=("Times",12),textvariable=self.password)
        self.entryPassword.pack()
        self.entryPassword.config(show="*",justify="center")
        Label(self.frame,text="", bg='#fcfcfc', fg="black" ).pack()
        self.boton=Button(self.frame, text="Acceder", font=("Times",15) , bg='#fcfcfc', fg="black",width=15,height=0, command=lambda:self.logiUser.validacion(self.nombre.get(),self.password.get(),self.ventana))
        self.boton.pack()
        Label(self.frame,text="", bg='#fcfcfc', fg="black" ).pack()
        self.ventana.mainloop()
       
      


