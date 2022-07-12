import mariadb

class Conexion:
    def __init__(self):
        try:
            self.connec=mariadb.connect(host="localhost",user="root",password="",db="ed_inventario")
            self.curs=self.connec.cursor()
        except mariadb.Error as e:
            print("Error de conexión: ",e)    
  