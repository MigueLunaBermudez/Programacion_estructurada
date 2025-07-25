"""

 dict.- 
  Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

  Tambien se conoce como un arreglo asosiativo u Objeto JSON

  El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")



pais1= {
          "nombre": "Mexico",
          "Capital": "CDMX",
          "poblacion" : 12000000,
          "Idioma" : "Español",
          "status" : True,
          }

pais2= {
          "nombre": "Brasil",
          "Capital": "Brasilia",
          "poblacion" : 14000000,
          "Idioma" : "Portuges",
          "status" : True,
          }

pais3= {
          "nombre": "Canada",
          "Capital": "Otawua",
          "poblacion" : 10000000,
          "Idioma" : ["ingles", "Frances"],
          "status" : True,
          }

#Funciones u operaciones con los dicciopnarios u objetos

print(pais1)

for i in pais1:
  print(f"{i} = {pais1[i]}")

#Agregar un atributo a un diccionario

pais1["altitud"]=3000

for i in pais1:
  print(f"{i} = {pais1[i]}")

#Quitar atributo en particular

pais1.pop("status")

for i in pais1:
  print(f"{i} = {pais1[i]}")