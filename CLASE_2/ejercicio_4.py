""" 4. Definir una función que imprima los argumentos ingresados desde línea de comandos
Nota: Usar import sys.argv => *args """
import sys
def FunImpArgIng():
  if len(sys.argv)==1 :
    print("\n>>>>>Para ingresar argumentos escribir primero \"python CLASE_2\\ejercicio_4.py\"(Ubicacion del archivo + nombre) seguido de los argumentos \n ")
  else: 
    print(f"\n{sys.argv[1::]}\n")  
  
FunImpArgIng()
#python CLASE_2\\ejercicio_4.py arg1 arg2