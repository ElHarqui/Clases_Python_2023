""" 2.Realizar un programa que realice las siguientes funciones de string al texto.
-split
-join
-count
-find
-uppercase
-lowercase
texto=”Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos
y los mezcló de tal manera que logró hacer un libro de textos especimen.” """

texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando uimpresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textosy los mezcló de tal manera que logró hacer un libro de textos especimen."
import os
import time
def uno(a):
  print("\t>1<\n")
  a = a.split()
  return a
#print(uno(texto))
def dos(a):
  print("\t>2<\n")
  a = list(a)
  b = input(" Ingrese tipo de separado : ")
  a = b.join(a)
  return a
#print(dos(texto))
def tres(a):
  print("\t>3<\n")
  a = list(a)
  b = input(" Ingrese lo que desea contar de la lista : ")
  a = a.count(b)
  return a
#print(tres(texto))
def cuatro(a):
  print("\t>4<\n")
  b= input(" Ingrese lo que desea buscar en el string : ")
  a = a.find(b)
  return a
#print(cuatro(texto))
def cinco(a):
  print("\t>5<\n")
  a= a.upper()
  return a
#print(cinco(texto))
def seis(a):
  print("\t>6<\n")
  a= a.lower()
  return a
#print(seis(texto))

def program_1(): 
  global texto
  
  print(f"\n{texto}\n")
  #os.system("pause")
  time.sleep(2)
  menu = "\t\t\t MENU\n 1.- split\n 2.- join\n 3.- count\n 4.- find\n 5.- uppercase\n 6.- lowercase\n"
  print(menu)
  while True:
    try:
      c = input("Elija el numero de lo que desee hacer con el texto: ")
      dici = { 
              "1" : uno,
              "2" : dos,
              "3" : tres,
              "4" : cuatro,
              "5" : cinco,
              "6" : seis}
      print(dici[c](texto))
      break
    except Exception as a:
      print(a)
      print("Error, intente denuevo")
program_1()