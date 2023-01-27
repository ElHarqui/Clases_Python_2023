""" 7.Programa que tenga una clase Producto el cual solo tiene el atributo de nombre ,codigo
el cual tiene la siguiente estructura ‘PAIS-LOTE-AÑO’ ejemplo : ‘PERU-0001-2023’ crear un
método que permita imprimir el objeto de forma literal (__str__) y que me permita identificar
el país de origen , el numero de lote .
"""
class Producto :
  def __init__ (self,nombre : str = "PAIS-LOTE-AÑO") :
    self.codigo = nombre
  def __str__(self) : 
    templist = self.codigo.split("-")
    return f"El pais de origen es \"{templist[0]}\" y el numero de lote \"{templist[1]}\""
def program_6():
  print(Producto())
