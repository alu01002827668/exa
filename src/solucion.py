#!/src/bin/python

#solucion de la aproximacion 

import modulo, math 
import time, timeit
import matplotlib.pylab as pl

lista_tiempo = []
lista_entrada = [1,2,3,4,5]
lista_resultado = []

for i in lista_entrada:
  start=time.time()
  x = modulo.factorial(i)
  lista_resultado = lista_resultado + [x]
  finish=time.time()-start
  print 'La aproximacion de ',i,'es  ', x
  print 'El tiempo que se tardo ha sido %14.13f' %finish
  lista_tiempo = lista_tiempo + [finish]

print lista_resultado

  
