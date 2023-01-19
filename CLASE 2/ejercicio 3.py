""" 3. Definir una función que retorne el mayor valor al ingresar 2 números.
"""

print("\t\tLa maquina te devolvera el valor mas grande ")
while True : 
  Num1 = input("Ingrese primer numero : ")
  if Num1.isnumeric : 
    Num1 = int(Num1)
    break
  else: 
    print("ERROR, intenta denuevo ")
  
while True : 
  Num2 = input("Ingrese segundo numero : ")
  if Num2.isnumeric : 
    Num2 = int(Num2)
    break
  else: 
    print("ERROR, intenta denuevo ")

if Num1 > Num2 :
  print(f"El mayor numero es {Num1}")
elif Num1 < Num2 : 
  print(f"El mayor numero es {Num2}")
else:
  print(f"ambos numeros son iguales ({Num2})")
