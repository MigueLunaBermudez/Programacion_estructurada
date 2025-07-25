
lista=[]

def borrarPantalla():
    import os
    os.system("cls")
    
def menu_principal():
     print("\n\t\t\t..::: CINEPOLIS CLON:::....\n\t\t..::: Sistema de Gestión de Calificaciones.:::...\n\n\t\t-1.--Agregar--\n\t\t-2.--Mostrar--\n\t\t-3.--Calcular Promedios--\n\t\t-4.--SALIR--\n\t\t")
     opcion = input("\n\t\t Elige una opción (1-4): ").upper()
     return opcion
 
def agregar_calificaciones(lista):
    borrarPantalla()
    
    print("Agregar Calificaciones")
    nombre=input("Nombre del Alumno")
    calificaciones=[]
    for i in range (1,4):
        try:
            calificaciones.append=(float(input(f"CAlificaciones {i}: ")))
        except ValueError:
            print("Ingrese una valor numerico")
    input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
    
