""" 8. para la pregunta 5 al importar la funciones usar el manejo de errores (try ,except) y en las
sentencias de “ else “ imprimir la ruta del directorio de trabajo os.getcwd() y en la sentencia
finally imprimir “proceso terminado” """
#COPIA DE LA PREGUNTA 5

import os
def program_7():
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
    else: 
      print (os.getcwd())
    finally:
      print(">>proceso terminado\n")
