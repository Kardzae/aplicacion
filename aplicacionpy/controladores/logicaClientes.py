from logging import raiseExceptions
from modelo.variables import cur, conn
from tkinter import messagebox
import pandas as pd
class logicaClientes:
    def llenarClientes(self, tree):
        registros=tree.get_children()
        for reg in registros:
            tree.delete(reg)
        cur.execute("SELECT * FROM clientes ORDER BY ID DESC")
        for datos in cur:
            tree.insert("",0,text=datos[0],values=(datos[1],datos[2], datos[3]))

    def buscarCliente(self,tree,id):
        registros = tree.get_children()
        for reg in registros:
            tree.delete(reg)
            cur.execute(f"SELECT * FROM clientes WHERE ID = {id}")
        for datos in cur:
            tree.insert("",0,text=datos[0],values=(datos[1],datos[2],datos[3]))
        if (not tree.get_children()):
            self.llenarClientes(tree)
            messagebox.showerror(message="El cliente solicitado aún no ha sido registrado",title="Mensaje del Sistema")
    
    def eliminarCliente(self,tree,id):
        try: 
            cur.execute(f"DELETE FROM clientes WHERE ID = {id}")
            conn.commit()
            self.llenarClientes(tree)
            messagebox.showinfo(message="Los datos del cliente se han eliminado",title="Mensaje del Sistema")
        except:
            messagebox.showerror(message="Por favor seleccione un cliente a eliminar sus datos.",title="Mensaje del Sistema")  

    def añadirCliente(self,factura,nombre,telefono,tree):
        try:
            cur.execute(f"INSERT INTO `clientes`(`ID`, `No.Factura`, `Nombre`, `Telefono`) VALUES (NULL,{factura},'{nombre}','{telefono}')")
            conn.commit()
            self.llenarClientes(tree)
            messagebox.showinfo(message="El cliente se ha añadido correctamente.",title="Mensaje del Sistema")
        except:
            messagebox.showerror(message="Para ingresar un nuevo cliente por favor llene los campos necesarios (todos)",title="Mensaje del Sistema")  

    def editarCliente(self,id, factura, nombre, telefono, tree):
        if not factura or not nombre or not telefono:
            messagebox.showerror(message="Por favor no deje campos vacios", title="ERROR")
            return
        cur.execute(f"UPDATE `clientes` SET `No.Factura`={factura},`Nombre`='{nombre}',`Telefono`='{telefono}' WHERE ID={id}")
        conn.commit()
        self.llenarClientes(tree)
        messagebox.showinfo(message="Cliente actualizado con éxito", title="Mensaje del sistema")
        
    def exportarClientes(self, consulta, tree, nombreTabla):
        try:
            if(tree.get_children()):
                cur.execute(consulta)
                datos=[]
                for entrada in cur:
                    obj={"ID":entrada[0],"No. factura":entrada[1],"Nombre":entrada[2],"telefono":entrada[3]}
                    datos.append(obj)    
                df=pd.DataFrame(datos)
                df.to_excel(f"{nombreTabla}.xlsx")
                messagebox.showinfo(message="La lista ha sido exportada a un archivo excel correctamente",title="Mensaje del Sistema")
            else:
                messagebox.showerror(message="Por favor, escriba en la tabla por lo menos un dato de algun cliente para exportar", title="Mensaje del sistema")
        except:
            messagebox.showerror(message="Por favor, escriba un nombre para exportar la tabla de clientes", title="Mensaje del sistema")