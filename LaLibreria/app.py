import sqlite3
from base_conexion.conexion import Conexion
from clases.libro import Libro
from clases.categoria import Categoria


conexion=Conexion(libreria_bd="libreria.db")
conexion.crea_tabla_libro()
conexion.agrega_libro("Cartas para Julia", 10000,"Maria Ines Falconi","Español", "Santillana","2016",15,3)


