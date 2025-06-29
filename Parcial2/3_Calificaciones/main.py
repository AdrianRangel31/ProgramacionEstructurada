from calificaciones import *
#Proyecto 3
#Crear un proyecto que permita gestionar calificaciones, colocar un mennu de opciones

def main():
    datos = []

    opcion=True
    while opcion:
        rsp = menu_Principal()
        match rsp:
            case "1":
                agregar_Calificaciones(datos)
                esperarTecla()
            case "2":
                mostrar_Calificaciones(datos)
                esperarTecla()
            case "3":
                calcular_Promedios(datos)
                esperarTecla()
            case "4":
                borrarPantalla()
                buscarAlumno(datos)
            case "5":
                borrarPantalla()
                print("✅Cerrando el programa...")
                opcion=False
            case _:
                borrarPantalla() 
                input("\n\t 📛 Opción invalida vuelva a intentarlo ... por favor 📛")

if __name__=="__main__":
    main()