"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
""""
import os
os.system("clear")



paises={"Mexico", "Brasil", "España", "Canada"}
print(paises)

varios = {True, "Cadena", 23, 3.1416}
print(varios)

paises.add ("México")
print(paises)

varios.pop()
print(varios)

varios.remove("Cadena")
print(varios)

"""

""""
Ejemplo: Crear un progroma que soliite los email demlos alumnos de la utd almacenar en una lista 
y posteriormente mostrar en pantalla los email sin duplicados.
"""


"""
def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Solicitar al usuario un número
numero = int(input("Ingresa un número para calcular su factorial: "))
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es: {resultado}")





def solicitar_emails(lista=None):
    if lista is None:
        lista = []
    email = input("Ingresa un email de alumno de la UTD (o escribe 'salir' para terminar): ")
    if email.lower() == "salir":
        return lista
    lista.append(email)
    return solicitar_emails(lista)

def eliminar_duplicados(lista):
    return list(set(lista))

def mostrar_emails(lista, index=0):
    if index < len(lista):
        print(lista[index])
        mostrar_emails(lista, index + 1)

def main():
    emails = solicitar_emails()
    emails_unicos = eliminar_duplicados(emails)
    print("\nCorreos electrónicos sin duplicados:")
    mostrar_emails(emails_unicos)

# Ejecutar el programa
main()
"""
emails= []
resp ="si"

while resp == "si":
  emails.append(input("Escribe un email: "))
  resp=input("¿Deseas agregar otro email?").lower()
  
print(emails)
emails_set=set(emails)
print(emails_set)
emails=list(emails_set)
print(emails)