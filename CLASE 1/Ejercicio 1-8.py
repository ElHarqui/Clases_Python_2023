#Peralta Silvano, Sebastian Leonardo
#1.Realizar un programa que ingrese sus datos personales e imprimirlos.

nombre = input('Ingrese nombre : ')
edad = input('Ingrese edad : ')
dni = input('Ingrese Nº de DNI : ')
print(nombre, edad, dni)

#2.Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el teclado.
radio = int(input(' Ingrese tamaño del radio : '))
ArCir = (radio ** 2) * 3.1416
ArTri = ((radio/2)**2)*3* (3**0.5)
ArCua = ( radio**2 )*2
print(f" El area del circulo es {ArCir}, el del triangulo {ArTri} y el del cuadrado inscrito es {ArCua}")


#3.Ingrese 3 valores y realice las operaciones de suma ,resta ,multiplicación, división y división entera.

vaL1=int(input('Ingrese valor 1 : '))
vaL2=int(input('Ingrese valor 2 : '))
vaL3=int(input('Ingrese valor 3 : '))

suma = vaL1+ vaL2 + vaL3
resta = vaL1 - vaL2 - vaL3
multi = (vaL1 + vaL2)* vaL3
divid = (vaL1 +vaL2)/ vaL3
dividEN = (vaL1 +vaL2)// vaL3
print(suma,'\n' , resta, '\n' ,multi, '\n' , divid ,'\n',  dividEN)

#4.Ingrese un valor e imprima el tipo de dato.
valR = int(input('ingrese dato : '))
print(type(valR))

"""5. Realice un programa que imprima la ubicación de su carpeta donde se encuentra
trabajando.
Nota : agregar el siguiente código
1. import sys
2. variable =sys.argv[0]"""
import sys
variable = sys.argv[0]
print("AQUI COMIENZA \n\t ",variable)

"""6.Realice un programa que calcule la suma de los números hasta el valor ingresado.
Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5."""
"""6.Realice un programa que calcule la suma de los números hasta el valor ingresado.
Ejemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5."""

ValIng1 = int(input(" Ingrese valor para la suma : "))
suma =0
n = 0
while n <= ValIng1 : 
   suma += n
   n +=1
print(suma)

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

"""8.Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas"""

contrasave = input("(1) ingrese nueva contraseña : ")
contrasave =  contrasave.lower() 
usuacontra = input('(2) Ingrese denuevo la contraseña : ')
usuacontra = usuacontra.lower()
if contrasave != usuacontra :
  print(f'Las contraseñas no coinciden \n{contrasave} \n{usuacontra}')
else: 
  print(' La contraseña se guardo correctamente')

