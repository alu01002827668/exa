#!/src/bin/python

#Aproximacion de factorial

import math

def factorial(n):
  a = n**n*math.e**(-n)
  b = math.sqrt((2*math.pi*n))
  resultado = a*b
  return resultado
  
if __name__ =="__main__":
  
  n = float(raw_input("Ingrese el numero: "))
  
  res = factorial(n)
  print "la aproximacion es ", res