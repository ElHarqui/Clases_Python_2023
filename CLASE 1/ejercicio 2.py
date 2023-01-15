#2.Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el teclado.
radio = int(input(' Ingrese tamaño del radio : '))
ArCir = (radio ** 2) * 3.1416
ArTri = ((radio/2)**2)*3* (3**0.5)
ArCua = ( radio**2 )*2
print(f" El area del circulo es {ArCir}, el del triangulo {ArTri} y el del cuadrado inscrito es {ArCua}")


