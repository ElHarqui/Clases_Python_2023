""" 2.Realizar un Programa que simule funcionalidades de una Biblioteca, definir la biblioteca
como un diccionario.
2.1 La biblioteca deberá tener las siguientes operaciones:
- Obtener la lista de categorías de libros.
-Obtener nombres de los libros y autores.
-poder cambiar el estado de un libro a prestado
-Lista de usuarios de la biblioteca. """
#BIBLIOTECA> Categorias > LIBROS >  
# ESTADO DEL LIBRO
# NOMBRE Y AUTOR 
## ver categorias : elegir una  : ver nombres de libros junto a su autor : elegir un libro para prestamo.
import os
Bibliotecaria = {
  'Categoria' : {
    'terror'  : [["juan","Lalalele" , 'disponible']], 
    'comedia' : [["rodrigo","Libro 2" , 'disponible']],
    'romance' : [["antonio","Libro 3" , 'disponible']],
    },
  }
#saludo
print("\t\tBienvenido a la biblioteca virtual")
os.system("pause")

#Obtener lista de categorias de libros
templist1 = list(Bibliotecaria['Categoria'].keys()) 
tempnum1 = len(templist1)
print('\tLISTA DE CATEGORIAS')
for i in range (0,tempnum1,1):
  print(f"{i+1}.- {templist1[i]}")


#Obtener nombres de los libros y autores
while True:
  tempnum2= input('Ingrese nombre o numero de la categoria deseada : ')
  if tempnum2.isnumeric():
    tempnum2 = int(tempnum2)
    if tempnum2 >=0 and tempnum2 <= tempnum1 :
      tempnum2 = tempnum2 -1
      UsuCat = templist1[tempnum2] 
      break
    else:
      print("error, intente denuevo")
  else:
    UsuCat= tempnum2.lower()
    if UsuCat in templist1:
      break
    else:
      print("error, intente denuevo")
tempnum1 = len(Bibliotecaria['Categoria'][UsuCat])
print("\tLista de Autores y Titulos de los libros")
for x in range (0,tempnum1,1) :
  if Bibliotecaria['Categoria'][UsuCat][x][2] == 'disponible':
    print(f"{x+1}.-\t\t {Bibliotecaria['Categoria'][UsuCat][x][0]} : {Bibliotecaria['Categoria'][UsuCat][x][1]}")
  else:
    print(f"{x+1}.-\t {Bibliotecaria['Categoria'][UsuCat][x][0]} : {Bibliotecaria['Categoria'][UsuCat][x][1]} : {Bibliotecaria['Categoria'][UsuCat][x][2]}")

# Cambiar estado de un libro a prestado 
while True: 
  UsuPres = input("Elija el numero un libro que desea : ")
  if UsuPres.isnumeric():
    UsuPres = int(UsuPres)
    UsuPres = UsuPres-1
    if UsuPres >=0 and UsuPres <=tempnum1:
      if Bibliotecaria['Categoria'][UsuCat][UsuPres][2] == 'disponible':
        print("El libro esta disponible")
        break
      else:
        print('Error, El libro no esta disponible')
while True:   
  UsuPres1  = input(" Desea alguilar el libro ? (SI/NO): ").lower()
  if UsuPres1 == "si" :
    Bibliotecaria['Categoria'][UsuCat][UsuPres][2] = 'NO disponible'
    print("Usted acaba de alquilar un libro")
  elif UsuPres1 == "no":
    print("Que tenga buen dia!")
    break
  else:
    print("error, intente denuevo")

