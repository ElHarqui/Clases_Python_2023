""" 3 Realizar una función que pase un entero por valor y lo multiplique por 2 y otra función """
def infimultidos(): 
  while True:
    try:
      a = int(input(" Ingrese valor : "))
      b = int(input(" Ingrese numero de veces a multiplicar : "))
      c = 0
      while True:
        if c == b :
          print(a)
          break
        else : 
          c = c+1
          a=a*2
      break
    except Exception as e:
      print(e)

def SumaProgre():
  while True:
    try:
      a= int(input(" Ingrese numero maximo de la suma : "))
      a = a+1
      b = 0
      c = 1
      while (c != a):
        b= b+c
        c = c+1
      print(b)
      break
    except Exception as e:
      print(e)

def program_2():
  menu = "\t\t\t MENU\n 1.-Multiplicador por 2 (N veces)\n 2.-Suma progresiva hasta N\n  "
  print(menu)
  while True:
    try:
      c = input("Elija el numero de lo que desee hacer : ")
      dicci2 = {
        "1" : infimultidos,
        "2" : SumaProgre
      }
      dicci2[c]()
      break
    except Exception as e:
      print(e)
