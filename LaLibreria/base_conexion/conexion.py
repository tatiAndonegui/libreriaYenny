import sqlite3
from clases.libro import Libro

class Conexion:

#constructor de conexion a la bd    
    def __init__(self,libreria_bd):
        self.conexion=sqlite3.connect(libreria_bd)
        self.cursor=self.conexion.cursor()

    def retornar_cursor(self):
        return self.conexion.cursor()


#tabla libro

#crea tabla libro
    def crea_tabla_libro(self):
        cursor=self.retornar_cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS libro (id_libro INTEGER PRIMARY KEY AUTOINCREMENT, titulo_libro TEXT NOT NULL, precio_libro INTEGER NOT NULL,autor_libro TEXT, idioma_libro TEXT, editorial_libro TEXT,anio_publicacion_libro TEXT, stock_libro INTEGER NOT NULL, pk_id_categoria_libro INTEGER)")

#crea Insert de tabla libro
    def agrega_libro(self,titulo,precio, autor, idioma, editorial, anio_publicacion, stock,categoria):
        cursor=self.retornar_cursor()
        cursor.execute("INSERT INTO libro (titulo_libro,precio_libro, autor_libro, idioma_libro, editorial_libro, anio_publicacion_libro, stock_libro,pk_id_categoria_libro) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (titulo,precio, autor, idioma, editorial, anio_publicacion, stock,categoria))
        self.conexion.commit()
        

#cierra la conexion a la bd
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()