"""1.En el archivo main.py crear la condición __name__==’__main__’ ejecutar los demás
problemas."""
from ejercicio_1 import program_1
from ejercicio_2 import program_2
from ejercicio_3 import program_3
from ejercicio_4 import program_4
from ejercicio_5 import program_5
from ejercicio_6 import program_6
from ejercicio_7 import program_7

dicimain = {
  "1" : program_1,
  "2" : program_2,
  "3" : program_3,
  "4" : program_4,
  "5" : program_5,
  "6" : program_6,
  "7" : program_7
  }
if __name__ == '__main__':
  while True:
    try:
      menu = "Que ejercicio desea ejecutar ? (1-7) : "
      Usumain = input(menu) 
      dicimain[Usumain]()
    except Exception as e:
      print(e)

#FUNCIONES  EJERCICIO 4 / 7 

def RecursivSuma (num : int):
  if num >0:
    num = num + RecursivSuma(num-1)
  return num

def Division(num1 : int , num2 : int) :
  try:
    num3 = num1 / num2
    return num3
  except Exception as e:
    print("ERROR, No se puede dividir")