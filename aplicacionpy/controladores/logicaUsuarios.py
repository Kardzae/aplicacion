from .logicaP import logicaProductos
from modelo.variables import conn, cur
from tkinter import *
from tkinter import messagebox
from vistas.productos import interfaz

class Usuarios:
  def validacion(self,name,pswd,ventana):
    cur.execute(f"SELECT * FROM `usuarios` WHERE nombre ='{name}' AND password = '{pswd}'")
    if(cur.fetchall()):
      vent=Tk()
      ventana.destroy()
      interfaz(vent,logicaProductos)
    else:
      messagebox.showerror(message="Usuario no valido",title="Mensaje del Sistema") 