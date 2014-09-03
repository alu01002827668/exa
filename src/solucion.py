#!/src/bin/python

#solucion de la aproximacion 

import modulo, math 
import time, timeit
import matplotlib.pylab as pl
import numpy as np

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
  
  
f=open("factorial.tex", 'a')
f.write(str(lista_entrada))
f.write('\n')
f.write(str(lista_resultado))
f.write('\n')
f.write(str(lista_tiempo))

f.close()
pl.figure(figsize =(8,6), dpi = 80)
pl.subplot(1,1,1)
x=np.linspace(0,5.5,256, endpoint= True)
y=np.linspace(0.000003,0.000015, 256, endpoint= True) 
a=lista_resultado
b=lista_tiempo
pl.xticks([1, 2, 3, 4, 5],[r'$1$',r'$2$',r'$3$',r'$4$',r'$5$'])
pl.yticks([1, 2, 3, 4, 5],[r'$1$',r'$2$',r'$3$',r'$4$',r'$5$'])

pl.title('Tiempo repecto a los resultados') 
pl.xlabel('Aproximacion')
pl.ylabel('Tiempo')
pl.xlim(0,5.5)
pl.ylim(0.000003,0.000015)


pl.plot(a,b,color="blue", linewidth=3.5, linestyle="-")

pl.savefig("factorial.eps", dpi=72)
pl.show()