from peliculas import *

opcion=True
while opcion:
    borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::..." 
            "\n 1.- Crear  " 
            "\n 2.- Borrar "
            "\n 3.- Mostrar " 
            "\n 4.- Agregar caracteristicas " 
            "\n 5.- Modificar caracteristicas " 
            "\n 6.- Borrar Caracteristicas " 
            "\n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            borrarPantalla()
            print(".::📝 Crear Peliculas📝 ::.") 
            crearPeliculas()
        case "2":
            borrarPantalla()
            print(".:: Borrar Peliculas ::.") 
            borrarPeliculas()
        case "3":
            borrarPantalla()
            print(".:: Mostrar Peliculas ::.") 
            mostrarPeliculas()
            esperarTecla()
        case "4":
            borrarPantalla()
            print(".:: Agregar Caracteristicas ::.")
            agregarCaracteristicaPeliculas()

        case "5":
            borrarPantalla() 
            print(".:: Modificar Caracteristicas ::.") 
            modificarCaracteristicaPeliculas()
            
        case "6":
            borrarPantalla() 
            print(".:: Borrar Caracteristicas ::.") 
            borrarCaracteristicaPeliculas()
            
        case "7":
            borrarPantalla()
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            borrarPantalla() 
            input("Opción invalida vuelva a intentarlo ... por favor")