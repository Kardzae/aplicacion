from tkinter import *
from modelo.variables import conn,cur
from tkinter import messagebox
import pandas as pd

class logicaSalidas:
    def llenarSalida(self,tree1):
        registros=tree1.get_children()
        for reg in registros:
            tree1.delete(reg)
        cur.execute("SELECT * FROM salidas ORDER BY id_salidas DESC")
        for datos in cur:
            tree1.insert("",0,text=datos[0],values=(datos[1],datos[2],datos[3],datos[4]))

    def buscarSalida(self,tree1,id):
        registros = tree1.get_children()
        for reg in registros:
            tree1.delete(reg)
            cur.execute(f"SELECT * FROM salidas WHERE Codigo = {id}")
        for datos in cur:
            tree1.insert("",0,text=datos[0],values=(datos[1],datos[2],datos[3],datos[4]))
        if (not tree1.get_children()):
            self.llenarSalida(tree1)
            messagebox.showerror(message="La salida del producto solicitada no existe.",title="Mensaje del Sistema")

    def eliminarSalida(self,tree1,id):
        try: 
            cur.execute(f"DELETE FROM salidas WHERE id_salidas = {id}")
            conn.commit()
            self.llenarSalida(tree1)
            messagebox.showinfo(message="La salida del producto ha sido eliminada correctamente.",title="Mensaje del Sistema")
        except:
            messagebox.showerror(message="Por favor seleccione una salida del producto a eliminar.",title="Mensaje del Sistema")        
    
    def añadirSalida(self,Codigo,nombre,cantidadE,factura,cliente,telefono,tree1):
        try:
            cur.execute(f"INSERT INTO salidas VALUES(NULL,{Codigo},'{nombre}',{cantidadE},CURRENT_DATE())")
            conn.commit()
            cur.execute(f"SELECT Cantidad, Salidas from productos WHERE Codigo={Codigo}")
            for c in cur:
                cantidad=c[0]
                entradas=c[1]
            cur.execute(f"UPDATE `productos` SET `Cantidad`={cantidad}-{cantidadE}, `Salidas`={entradas}+{cantidadE} WHERE Codigo={Codigo}")
            conn.commit()
            cur.execute(f"INSERT INTO `clientes`(`ID`, `No.Factura`, `Nombre`, `Telefono`) VALUES (NULL,{factura},'{cliente}','{telefono}')")
            conn.commit()
            self.llenarSalida(tree1)
            messagebox.showinfo(message="La salida del producto ha sido añadida correctamente.",title="Mensaje del Sistema")
        except:
            messagebox.showerror(message="Por favor llene los campos necesarios para registrar la salida (todos)", title="Error")
    
    def editarSalida(self,id_salidas,nombre,entradas,fecha,id,tree1):
        if not id_salidas and not nombre and not entradas and not fecha:
            messagebox.showerror(message="Por favor llene al menos un campo para editar la salida.",title="Mensaje del Sistema")
            return    
        cur.execute(f"SELECT id_salidas, Nombre, Salidas, Fecha_salidas FROM salidas WHERE id_salidas={id}")
        listado=[id_salidas,nombre,entradas,fecha]
        for dato in cur.fetchall():
            for i in range(len(listado)):
                if(not listado[i]):
                    listado[i]=dato[i]
        try:
            cur.execute(f"UPDATE `salidas` SET `Codigo`={listado[0]}, `Nombre`='{listado[1]}',`salidas`={listado[2]},`Fecha_salidas`='{listado[3]}' WHERE id_salidas={id}")
            conn.commit()
            self.llenarSalida(tree1)
            messagebox.showinfo(message="La salida ha sido modificada correctamente.",title="Mensaje del Sistema")
        except:     
            messagebox.showerror(message="Este codigo de salida ya está asociado",title="Mensaje del Sistema")

    def exportarSalidas(self,consulta,tree1,nombreSalidas):
        try:
            if(tree1.get_children()):
                cur.execute(consulta)
                datos=[]
                for entrada in cur:
                    obj={"id_salidas":entrada[0],"Codigo":entrada[1],"Nombre":entrada[2],"Salidas":entrada[3],"fecha":entrada[4]}
                    datos.append(obj)    
                df=pd.DataFrame(datos)
                df.to_excel(f"{nombreSalidas}.xlsx")
                messagebox.showinfo(message="La lista ha sido exportada a un archivo excel correctamente",title="Mensaje del Sistema")
            else:
                messagebox.showerror(message="Por favor, escriba en la tabla por lo menos un producto para poder ser exportada",title="Mensaje del Sistema")
        except:
            messagebox.showerror(message="Por favor, escriba el nombre de su respectiva tabla de salidas para exportar a archivo excel",title="Mensaje del Sistema")

