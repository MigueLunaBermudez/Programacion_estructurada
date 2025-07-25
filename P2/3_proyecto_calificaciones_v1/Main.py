"""# proyecto-1-
# -Crear-un-proyecto que permita Gestionar (Administrar) peliculas, colocar un-menu-de-opciones para agregar, eliminar, modificar-y-consultar-peliculas..
# Notas:
# 1.--Utilizar funciones y mandar llamar desde otro archivo
# 2.--Utilizar listas para almacenar el nombre y 3 calificaciones de los alumnos

"""

import Calificaciones

def main():
    opcion = True
    datos=[]

    while opcion:
        Calificaciones.borrarPantalla()
        Calificaciones.menu_principal()
        opcion = Calificaciones.menu_principal()
        match opcion:
            case "1":
                Calificaciones.agregar_calificaciones(datos)
                Calificaciones.esperarTecla()
            case "2":
                Calificaciones.mostrar_calificaciones(datos)
                Calificaciones.esperarTecla()
            case "3":
                Calificaciones.calcular_promedios(datos)
                Calificaciones.esperarTecla()
            case "4":
                opcion = False
                Calificaciones.borrarPantalla()
                print("\n\tTerminaste la ejecucion del SW")
            case _:
                opcion = True
                input("\n\tOpción inválida, vuelva a intentarlo.... por favor")
                
if __name__ == "__main__":
    main ()
