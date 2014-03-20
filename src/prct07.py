#!/usr/bin/python
#!encoding: UTF-8
import modulo
#Programa principal 
tupla = (10, 20, 30, 40)
lista = []
for i in tupla:
  valor_pi = modulo.calcular_pi (i)#llamada a la función
  lista.append (valor_pi)
print lista
pi35 = []
for i in tupla:
  pi35.append (modulo.PI35DT)
dif35 = []
for i in range (len (tupla)):
  dif35.append (abs(pi35[i] - lista[i]))
print "i \tPI35DT   \tlista i   \tPI35DT - lista i"
for i in range (len(tupla)):
  print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1, pi35[i], lista[i], dif35[i])
 
#¿Cuál es el número máximo de elementos de la t-upla?: dependiendo de la máquina que tengamos
#¿Se pueden definir los elementos de lat-upla en notación científica?:tupla = (1e1,1e2,1e3,1e4,1e5,1e6,1e7,1e8)
#¿Qué significado tiene la extension.pyc?: cuando hago un python de modulo.py el ejecutable lo convierte en .pyc
#Cuánto tiempo se invierte?¿Cómo lo mediría?:en cada iteracion hay que tomarse el tiempo inicial y el final para saber el tiempo

#Para saber más
print "Pasando la salida a una matriz..."
print "i\tPI35DT\t\t lista i\t\t PI35DT - lista i", #
matriz = []
for i in range (len (tupla)):
  matriz.append ([i+1, pi35[i], lista[i], dif35[i]])
for i in range (len (tupla)):
  print
  print matriz[i][0], #
  for j in range (1,4):
    print "\t%1.10f" % matriz[i][j], #