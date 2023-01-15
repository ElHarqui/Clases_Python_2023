"""7. Realiza un programa que lea 2 números por teclado y determine los siguientes
aspectos:
● Si los dos números son iguales
● Si los dos números son diferentes
● Si el primero es mayor que el segundo
● Si el segundo es mayor o igual que el primero"""

num1_7 = int(input("ingrese numero 1 : ")) 
num2_7 = int(input("ingrese numero 2 : "))

if num1_7 != num2_7 :
  if num1_7 < num2_7:
    print(f'el numero {num2_7} es mayor')
  else:
    print(f'el numero {num1_7} es mayor')
else: 
  print(f'ambos numeros son iguales ')

