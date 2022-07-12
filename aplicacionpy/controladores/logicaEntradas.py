from cgitb import text
from tkinter import *
from modelo.variables import conn,cur
from tkinter import messagebox
import pandas as pd

class logicaEntradas:
    def llenarEntradas(self,tree):
        registros=tree.get_children()
        for reg in registros:
            tree.delete(reg)
        cur.execute("SELECT * FROM entradas ORDER BY id_entradas DESC")
        for datos in cur:
            tree.insert("",0,text=datos[0],values=(datos[1],datos[2],datos[3],datos[4]))

    def buscarEntrada(self,tree,id):
        registros = tree.get_children()
        for reg in registros:
            tree.delete(reg)
            cur.execute(f"SELECT * FROM entradas WHERE Codigo = {id}")
        for datos in cur:
            tree.insert("",0,text=datos[0],values=(datos[1],datos[2],datos[3],datos[4]))
        if (not tree.get_children()):
            self.llenarEntradas(tree)
            messagebox.showerror(message="La entrada del producto solicitada no existe.",title="Mensaje del Sistema")

    def eliminarEntrada(self,tree,id):
        try: 
            cur.execute(f"DELETE FROM entradas WHERE id_entradas = {id}")
            conn.commit()
            self.llenarEntradas(tree)
            messagebox.showinfo(message="La entrada del producto ha sido eliminada correctamente.",title="Mensaje del Sistema")
        except:
            messagebox.showerror(message="Por favor seleccione una entrada del producto a eliminar.",title="Mensaje del Sistema")        
    
    def añadir(self,Codigo,nombre,cantidadE,tree):
        try:
            cur.execute(f"INSERT INTO entradas VALUES(NULL,{Codigo},'{nombre}',{cantidadE},CURRENT_DATE())")
            conn.commit()
            cur.execute(f"SELECT Cantidad, Entradas from productos WHERE Codigo={Codigo}")
            for c in cur:
                cantidad=c[0]
                entradas=c[1]
            cur.execute(f"UPDATE `productos` SET `Cantidad`={cantidad}+{cantidadE}, `Entradas`={entradas}+{cantidadE} WHERE Codigo={Codigo}")
            conn.commit()
            self.llenarEntradas(tree)
            messagebox.showinfo(message="La entrada del producto ha sido añadida correctamente.",title="Mensaje del Sistema")
        except:
            messagebox.showerror(message="Para ingresar una nueva entrada por favor llene los campos necesarios (todos)",title="Mensaje del Sistema")
    
    def editarEntrada(self,id_entradas,nombre,entradas,fecha,id,tree):
        if not id_entradas and not nombre and not entradas and not fecha:
            messagebox.showerror(message="Por favor llene al menos un campo para editar la entrada.",title="Mensaje del Sistema")
            return    
        cur.execute(f"SELECT id_entradas, Nombre, Entradas, Fecha_entradas FROM entradas WHERE id_entradas={id}")
        listado=[id_entradas,nombre,entradas,fecha]
        for dato in cur.fetchall():
            for i in range(len(listado)):
                if(not listado[i]):
                    listado[i]=dato[i]
        try:
            cur.execute(f"UPDATE `entradas` SET `Codigo`={listado[0]}, `Nombre`='{listado[1]}',`entradas`={listado[2]},`Fecha_entradas`='{listado[3]}' WHERE id_entradas={id}")
            conn.commit()
            self.llenarEntradas(tree)
            messagebox.showinfo(message="La entrada ha sido modificada correctamente.",title="Mensaje del Sistema")
        except:     
            messagebox.showerror(message="Este codigo de entrada ya está asociado",title="Mensaje del Sistema")

    def exportarEntradas(self,consulta,tree,nombreEntradas):
        try:
            if(tree.get_children()):
                cur.execute(consulta)
                datos=[]
                for entrada in cur:
                    obj={"id_entradas":entrada[0],"Codigo":entrada[1],"Nombre":entrada[2],"Entradas":entrada[3],"fecha":entrada[4]}
                    datos.append(obj)    
                df=pd.DataFrame(datos)
                df.to_excel(f"{nombreEntradas}.xlsx")
                messagebox.showinfo(message="La lista ha sido exportada a un archivo excel correctamente",title="Mensaje del Sistema")
            else:
                messagebox.showerror(message="Por favor, escriba en la tabla por lo menos un producto para poder ser exportada",title="Mensaje del Sistema")
        except:
            messagebox.showerror(message="Por favor, escriba el nombre para exportar el archivo excel de su respectiva tabla",title="Mensaje del Sistema")
