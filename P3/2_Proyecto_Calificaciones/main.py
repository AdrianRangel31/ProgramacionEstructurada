from calificaciones import *

#Proyecto 3
#Crear un proyecto que permita gestionar calificaciones, colocar un mennu de opciones

def main():
    

    opcion=True
    while opcion:
        rsp = menu_Principal()
        match rsp:
            case "1":
                agregar_Calificaciones()
                esperarTecla()
            case "2":
                mostrar_Calificaciones()
                esperarTecla()
            case "3":
                calcular_Promedios()
                esperarTecla()
            case "4":
                borrarPantalla()
                buscarAlumno()
                esperarTecla()
            case "5":
                borrarPantalla()
                modificarAlumno()
                esperarTecla()
            case "6":
                borrarPantalla()
                borrarAlumno()
                esperarTecla()
            case "7":
                borrarPantalla()
                print("✅Cerrando el programa...")
                opcion=False
            case _:
                borrarPantalla() 
                input("\n\t 📛 Opción invalida vuelva a intentarlo ... por favor 📛")

if __name__=="__main__":
    main()