"""
List (Array)
SOn collectiones o conjunto de datos /valores bajo un mismo nombre,
para acceder a los valores se hace un indice numerico.

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite miembros duplicados
"""

import os
os.system("cls")

#Funciones mas comunes en las listas.

paises=["Mexico", "Brasil", "España", "Canada"]
num=[23,45,8,24], 23,56
varios=["hola", 2.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(num)
print(varios)

#Recorrer el contenido
for i in paises:
    print (i)
    

#2da forma
for i in range(0-4):
    print(paises[i])

os.system("cls")

paises.sort ()
print(paises)

#dar la vuelta las listas
varios.reverse()
print(varios)

paises.reverse()
print(paises)

#Buscar un elemento dentro de una lista
t="España" in paises
print(t)

#Insertar, añadir, agregar un elemento a una lista
os.system("cls")

print(paises)
paises.append("Mèxico")

#2da forma
paises.insert(1,"Mexico")
print(paises)

#Borrar, eliminar, suprimir, quitar un elemento de la lista

os.system("cls")
print(paises)

#1er forma
paises.pop(0)
print(paises)

paises.sort()

#obtener el indice o la posicion en la que se encuentra un elemnto
os.system("cls")
print(paises)

pocision=paises.index("Canada")
print(pocision)

#Contaar el numero de veces que un elemento se encuentra en una lista
os.system("cls")
print(num)

cuantas=num.count(23)
print(cuantas)

cuantas=num.count(233)
print(cuantas)

#Unir el contenido de una lista en otra
os.system("cls")
print(num)
numeros2=[100,200]
print(numeros2)

#Crear un programa que una las listas numero 1 y 2 e imprima el contenido de la lista resultant en forma decendente

num.extend(numeros2)
num.sort()
num.revere()
print(num)