""" 6.Imprima el nombre del archivo en ejecución """
import sys
def program_5():
  ListTemp =sys.argv[0].split("/")
  NumLoop = len(ListTemp)
  print(f"\n\nEl nombre del archivo es {ListTemp[NumLoop-1]}\n\n")
