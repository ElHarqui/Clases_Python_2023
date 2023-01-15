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
