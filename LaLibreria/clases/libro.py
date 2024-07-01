class Libro:

  def __init__(self, titulo,precio, autor, idioma, editorial, anio_publicacion, stock,categoria):
    self.titulo = titulo 
    self.precio = precio
    self.autor = autor
    self.idioma = idioma
    self.editorial = editorial
    self.anio_publicacion = anio_publicacion
    self.stock = stock
    self.categoria = categoria

  def ingresar_a_base(self):
    conexion=Conexion('libreria.db')
    resultado=conexion.agrega_libro()
    conexion.cerrar_conexion()
    return resultado



#METODOS
#def getTitulos(self):
#  return self.titulo
#def getPrecio(self):
#  return self.precio
#def getAutor(self):
#  return self.autor
#def getIdioma(self):
#  return self.idioma
#def getEditorial(self):
#  return self.editorial
#def getAnio_publicacion(self):
#  return self.anio_publicacion
#def getStock(self):
#  return self.stock
#def getCategoria(self):
#  return self.categoria

#def mostrarLibro(self):
#  print("\nTitulo: " + self.getTitulo()
#        + "\nPrecio: " + self.getPrecio() 
#        + "\nAutor: " + self.getAutor() 
#        + "\nIdioma: " + self.getIdioma() 
#        + "\nEdtorial:" + self.getEditorial() 
#        + "\nAnio de publicacion: " + self.getAnio_publicacion() 
#        + "\nStock: " + self.getStock() 
#       + "\nCategoria: " + self.getCategoria())

#def modificarLibro(self):
  #aca crear el metodo para modificar los datos del libro

#def ajustarPrecio(self, precio):
  #self.precio = precio
  #aca crear el metodo para modificar el precio