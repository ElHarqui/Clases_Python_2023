""" 4. Una tienda de autopartes necesita un programa para catalogar sus productos ,crear la
clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
tener un método para agregar productos y otra para mostrar toda la lista de productos """
import os
class Producto :
  def __init__(self,nombre : str = "sin nombre",precio= 0,calidad= 0,cantidad = 0):
    self.nombre = nombre
    self.precio = precio # S/. 
    self.calidad = calidad #baja(1)- media(2) - alta(3) 
    self.cantidad = cantidad
  def __str__(self):
    return self.nombre
    

alternador = Producto("alternador",100,3,3)
ejes = Producto("ejes",200,2,5)
balancines = Producto("balancines",50,2,4)
viela = Producto("viela",20,1,7)
ListaProductos = [alternador,ejes,balancines,viela]

class Catalogo :
  def __init__(self,ListProduct) :
    self.ListProduct = ListProduct
    
  def AddProduct (self,nombre= "sin nombre"):
    while True:
      try:
        nuevo = ""
        a = nombre
        b = int(input("Ingrese precio : "))
        c = int(input("Ingrese calidad [1/2/3] : " ))
        d = int(input("Ingrese cantidad : "))
        if b>=0 and c>=0 and d>=0 and c<=3 :
          nuevo = Producto(a,b,c,d)
          self.ListProduct.append(nuevo) 
          print("Se agrego producto al catalogo")
          break
        else:
          print("Error, Coloque datos denuevo ")
      except Exception as e:
        print(e)
  def MostCatag (self):
    a = len(self.ListProduct)
    templist = list()
    print("\t\tCATALOGO")
    for i in range (0,a,1):
      #tmpstr = str(self.ListProduct[i])# LO use para crear una lista  pero luego se me ocurrio otra cosa
      #templist.append(tmpstr)
      print(f"{i+1}.- {str(self.ListProduct[i])}")
    print("")
TiendaRoberto = Catalogo(ListaProductos) #creamos el objeto del catalogo
menu = "\t\tMENU\n1.- Mostrar Lista\n2.- Agregar producto\n3.- Salir\n\n>> "

#AQUI COMIENZA EL MENU
def program_3():
  while True:
    try:
      UsuSelec =int(input(menu))
      if UsuSelec == 1 :
        TiendaRoberto.MostCatag()
        os.system("pause")
      elif UsuSelec == 2 :
        tempnomb = input("Ingrese nombre del producto: ")
        TiendaRoberto.AddProduct(tempnomb)
        os.system("pause")
      elif UsuSelec == 3 :
        break
    except Exception as e:
      print(e)
      print("Intente denuevo")
      print("")
