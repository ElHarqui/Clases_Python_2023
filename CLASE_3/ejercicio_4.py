""" 5.Crear un paquete de programas (módulo) que tenga las siguiente funciones
-Una función recursiva de suma de los n primeros números
-Una función que me permita dividir 2 números.
-importar esos módulos desde el archivo main
"""

import os
def program_4():
  import main as fun
  menu = "\t\tMENU\n1.-suma de los n primeros números\n2.-dividir 2 números\n\n>>"
  while True:
    try:
      Usu = int(input(menu))
      if Usu == 1 :
        a = int(input("Ingrese el valor de N: "))
        print(fun.RecursivSuma(a))
        break
      elif Usu == 2 :
        num1 = int(input("Ingrese valor del numerador : "))
        num2 = int(input("Ingrese valor del denominador : "))
        print(fun.Division(num1, num2))
        break
      else:
        print("ERROR. Ingrese numero valido")
        os.system("pause")
    except:
      print ("\nERROR. intente denuevo\n")
      os.system("pause")
