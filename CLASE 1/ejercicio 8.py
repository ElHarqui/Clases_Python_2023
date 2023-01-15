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