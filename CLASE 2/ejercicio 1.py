""" 1.Realizar un Menú Iterativo que tenga las siguientes opciones(Solo poner el número de la
pregunta):
- Realizar un programa que dibuje un cuadrado en consola con *, usando bucles.
- Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e
imprimir el número
- Iterar una lista de elementos que contengan nombre y edad e imprimir solo los
mayores de edad.
Nota : cada elemento de la lista puede ser otra lista [[nombre,edad],.... ] """

# Elegir MENU 
msg = "\t\t\tMenú\n 1.- Impresor de cuadrados en consola \n 2.- Identificar multiplos de 2 en una lista \n 3.- Identificador de mayores de edad"
print(msg)

# SUBPROGRAMA 1
def SubProm1():
  while(True):
    Tama_Cua = input('Ingrese un solo numero para el tamaño de los lados : ')
    if Tama_Cua.isnumeric():
      Tama_Cua = int(Tama_Cua)
      break
    else:
      print('Error, Digite denuevo')
  impA = str('■ ')
  impB = str('  ')
  for i in range (0,Tama_Cua,1 ) :
    if i==0 or i== (Tama_Cua -1):
      print(impA*(Tama_Cua))
    else :
      impB = impB*(Tama_Cua-2)
      print(f"{impA}{impB}{impA}")
      impB = str('  ')
# SUBPROGRAMA 2
def SubProm2():
  print("gaaaa")

# SUBPROGRAMA 3
def SubProm3():
  print("gaaaa")

# EJECUTAR 
while(True):
  Program = input("Coloque el numero de lo que desea hacer (1-3) : ")
  if Program.isnumeric():
    Program = int(Program)
    if Program == 1 :
      SubProm1()
      break
    elif Program == 2 :
      SubProm2()
      break
    elif Program == 3 :
      SubProm3()
      break
    else: 
      print("ERROR, VUELVA A DIGITAR UN NUMERO")
  else:
    print('Error, Digite denuevo')
