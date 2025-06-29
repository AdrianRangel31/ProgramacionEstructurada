from peliculas import *

opcion=True
while opcion:
    borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            borrarPantalla()
            print(".:: Agregar Peliculas ::.") 
            agregarPeliculas()
            
        case "2":
            borrarPantalla()
            print(".:: Eliminar Peliculas ::.") 
            borrarPeliculas()
        case "3":
            borrarPantalla()
            print(".:: Modificar Peliculas ::.") 
            

        case "4":
            borrarPantalla()
            print(".:: Consultar Peliculas ::.")
            consultarPeliculas()
              
        case "5":
            borrarPantalla() 
            print(".:: Buscar Peliculas ::.") 
            buscarPeliculas()
            
        case "6":
            borrarPantalla() 
            print(".:: Vacias Peliculas ::.") 

            vaciarPeliculas()
            
        case "7":
            borrarPantalla()
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            borrarPantalla() 
            input("Opción invalida vuelva a intentarlo ... por favor")