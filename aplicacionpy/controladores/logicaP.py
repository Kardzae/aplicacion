from optparse import TitledHelpFormatter
from modelo.variables import conn,cur
from tkinter import messagebox
from tkinter import *
import pandas as pd
import mariadb

class logicaProductos:
  
  def eliminar(self,codigo,tree):
      try: 
        cur.execute(f"DELETE FROM productos WHERE Codigo = {codigo}")
        conn.commit()
        self.llenarTabla(tree)
        messagebox.showinfo(message="El producto ha sido eliminado correctamente.",title="Mensaje del Sistema")
      except:
        messagebox.showerror(message="Por favor seleccione el producto a eliminar.",title="Mensaje del Sistema")

  def Ordenardesc(self,tree):
    registros = tree.get_children()
    for reg in registros:
      tree.delete(reg)
      cur.execute("SELECT * FROM `productos` ORDER BY `productos`.`Cantidad` DESC")
    for datos in cur:
      tree.insert("",0,text=datos[0],values=(datos[1],datos[3],datos[4],datos[2],datos[5], datos[6]))

  def OrdenarAsc(self,tree):
    registros = tree.get_children()
    for reg in registros:
      tree.delete(reg)
      cur.execute("SELECT * FROM `productos` ORDER BY `productos`.`Cantidad` ASC")
    for datos in cur:
      tree.insert("",0,text=datos[0],values=(datos[1],datos[3],datos[4],datos[2],datos[5], datos[6]))

  def llenarTabla(self,tree):
    registros = tree.get_children()
    for reg in registros:
      tree.delete(reg)
    cur.execute("SELECT * FROM productos ORDER BY Codigo DESC")
    for datos in cur:
      tree.insert("",0,text=datos[0],values=(datos[1],datos[3],datos[4],datos[2],datos[5],datos[6]))

  def consultar(self,tree,entrada):
    registros = tree.get_children()
    for reg in registros:
      tree.delete(reg)
      cur.execute(f"SELECT * FROM productos WHERE Codigo = '{entrada}' ")
    for datos in cur:
      tree.insert("",0,text=datos[0],values=(datos[1],datos[3],datos[4],datos[2],datos[5],datos[6]))
    if (not tree.get_children()):
      self.llenarTabla(tree)
      messagebox.showerror(message="El Producto solicitado no existe.",title="Mensaje del Sistema") 

  def insertar(self,codigo, nombre, cantidad, precio, costo, entradas, salidas,tree):
      cur.execute(f"SELECT * FROM productos WHERE Nombre='{nombre}'")
      try:
        if cur.fetchall():      
          messagebox.showerror(message="El producto ya existe.",title="Mensaje del Sistema")   
        else:
          if(not entradas):
            entradas=0
          if (not salidas):
            salidas=0   
          cur.execute(f"INSERT INTO `productos`(`Codigo`, `Nombre`, `Cantidad`, `Precio`, `Costo`, `Entradas`, `Salidas`) VALUES ({codigo},'{nombre}',{cantidad},{precio},{costo},{entradas},{salidas})")
          conn.commit()
          self.llenarTabla(tree)
          messagebox.showinfo(message="El producto ha sido añadido correctamente.",title="Mensaje del Sistema")
      except mariadb.IntegrityError:
        messagebox.showerror(message="Esta clave de producto ya existe",title="Mensaje del Sistema")
      except:
        messagebox.showerror(message="Para ingresar un nuevo producto llene los respectivos campos: Codigo, Nombre, Cantidad, Precio, Costo.",title="Mensaje del Sistema")

  def modificar(self,Nombre,Cantidad,Precio,costo,Entradas,Salidas,oldNombre,tree):
      if not Nombre and not Cantidad and not Precio and not costo and not Entradas and not Salidas:
        messagebox.showerror(message="Por favor no deje los campos vacíos",title="Mensaje del Sistema")
        return
      cur.execute(f"SELECT * FROM `productos` WHERE Nombre='{oldNombre}' AND Entradas={Entradas} AND Salidas={Salidas}")
      lista=[Nombre,Cantidad,Precio,costo,Entradas,Salidas]
      #for dato in cur.fetchall():
      #  for i in range(len(lista)):
      #    if(not lista[i]):
      #      lista[i]=dato[i]
      #if lista[5]==dato[5]:
      #  Entradas=0
      #else:
      #  Entradas=lista[5]
      #if lista[6]==dato[6]:
      #  Salidas=0 
      #else:
      #  Salidas=lista[6]
      if cur.fetchall():  
        try:
          cur.execute(f"UPDATE `productos` SET `Nombre`='{lista[0]}',`Cantidad`={lista[1]},`Precio`={lista[2]},`Costo`={lista[3]},`Entradas`={lista[4]},`Salidas`={lista[5]} WHERE Nombre='{oldNombre}'")
          conn.commit()
          self.llenarTabla(tree)
          messagebox.showinfo(message="El producto ha sido modificado correctamente.",title="Mensaje del Sistema")   
        except:
          messagebox.showerror(message="Este codigo ya esta siendo usado en otro producto.",title="Mensaje del Sistema")
      else:
        cur.execute(f"SELECT Entradas FROM productos WHERE Entradas={Entradas} AND Nombre='{oldNombre}'")
        if cur.fetchall():
          Entradas=0
        cur.execute(f"SELECT Salidas FROM productos WHERE Salidas={Salidas} AND Nombre='{oldNombre}'")
        if cur.fetchall():
          Salidas=0  
        try:
          cur.execute(f"UPDATE `productos` SET `Nombre`='{lista[0]}',`Cantidad`={lista[1]}+{Entradas}-{Salidas},`Precio`={lista[2]},`Costo`={lista[3]},`Entradas`={lista[4]},`Salidas`={lista[5]} WHERE Nombre='{oldNombre}'")
          conn.commit()
          self.llenarTabla(tree)
          messagebox.showinfo(message="El producto ha sido modificado correctamente.",title="Mensaje del Sistema")
        except:
          messagebox.showerror(message="Este codigo ya esta siendo usado en otro producto.",title="Mensaje del Sistema")
        
  def exportarTabla(self,query,tree,name):
    try:
      if(tree.get_children()):
        cur.execute(query)
        datos=[]
        for producto in cur:
          obj={"Codigo":producto[0], "Nombre":producto[1], "Cantidad":producto[2], "Precio":producto[3], "Costo": producto[4],"Entradas":producto[5], "salidas":producto[6]}
          datos.append(obj)    
        df=pd.DataFrame(datos)
        df.to_excel(f"{name}.xlsx")
        messagebox.showinfo(message="La lista ha sido exportada a un archivo excel correctamente",title="Mensaje del Sistema")
      else:
        messagebox.showerror(message="Por favor, escriba en la tabla por lo menos un producto para poder ser exportada",title="Mensaje del Sistema")
    except:
      messagebox.showerror(message="Por favor, escriba un nombre de tabla para exportar",title="Mensaje del Sistema")
  def Crear_usuario(self,nombre, password):
    cur.execute(f"SELECT * FROM usuarios WHERE nombre='{nombre}'")
    if (not nombre and not password):
      messagebox.showerror(message="Por favor llene los campos necesarios",title="Mensaje del Sistema")
    else:
      if cur.fetchall():      
        messagebox.showerror(message="Este nombre de usuario ya existe.",title="Mensaje del Sistema")   
      else:
        cur.execute(f"INSERT INTO `usuarios`(`codigo`, `nombre`, `password`) VALUES (NULL,'{nombre}','{password}')")
        conn.commit()
        messagebox.showinfo(message="El usuario ha sido creado correctamente.",title="Mensaje del Sistema")
      
       
    

  
