
'''lista=[
    ["Ruben", 10.0,8.9,9.2],
    ["Andres", 10.0,10.0,10.0],
    ["maria", 10.0,10.0,10.0]
]'''

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")
    
def menu_principal():
    print("\n\t\t\t..::: CINEPOLIS CLON:::....\n\t\t..::: Sistema de Gestión de calificaciones.:::...\n\n\t\t-1.--Agregar--\n\t\t-2.--Mostrar--\n\t\t-3.--calcular promedio --\n\t\t-4.--SALIR--")
    opcion = input("\n\t\t Elige una opción (1-4): ").upper()
    return opcion
    
def agregar_calificaciones(Lista):
    borrarPantalla()
    print("\n\t\t\t..::: Agregar Calificaciones :::...\n")
    nombre = input("\n\t\tIngrese el nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        bandera=True
        while bandera:
            try:
                #calificaciones.append(float(input(f"\n\t\tIngrese la calificación {i} del alumno {nombre}: ")))
                cali= float(input(f"\n\t\tIngrese la calificación {i} del alumno {nombre}: "))
                if cali < 0 and cali > 10:
                    calificaciones.append(cali)
                    bandera = False
                    print("\n\t\tError: La calificación debe estar entre 0 y 10.")
                else:
                    print("\n\t ingrese un valor comprendido entre 0 y 10")
            except ValueError:
                print("\n\t\tError: Debe ingresar un número válido para la calificación.")
    Lista.append([nombre] + calificaciones)
    print(f"\n\t\tAccion realizada con exito.")
    
    
def mostrar_calificaciones(Lista):
    borrarPantalla()
    print("\n\t\t\t..::: Mostrar Calificaciones :::...\n")
    if len(Lista) == 0:
        print(f"{'Nombre':<15}{'calificacion1':<10}{'calificacion2':<10}{'calificacion3':<10}")
        print("-"*50)
        for fila in Lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print("-"*50)
            print(f"son {len(Lista)} alumnos")
        else:
            print("\n\t\tNo hay calificaciones en el sistemas.")
        
def calcular_promerios(Lista):
    borrarPantalla()
    print("\n\t\t\t..::: Calculat promedios :::...\n")
    if len(Lista) == 0:
        print(f"{'Nombre':<15}{'promedio':<10}")
        print("-"*30)
        for fila in Lista:
            print(f"{fila[0]:<15}{sum(fila[1])/len(fila[1])}")
            print("-"*30)
            print(f"son {len(Lista)} alumnos")
        else:
            print("\n\t\tNo hay calificaciones en el sistemas.")