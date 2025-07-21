from peliculas import *

import mysql.connector

opcion=True
while opcion:
    borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::..." 
            "\n 1.- Crear  " 
            "\n 2.- Borrar "
            "\n 3.- Mostrar " 
            "\n 4.- Modificar" 
            "\n 5.- Buscar" 
            "\n 6.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            borrarPantalla()
            print(".::📝 Crear Peliculas📝 ::.") 
            crearPeliculas()
            esperarTecla()
        case "2":
            borrarPantalla()
            print(".:: Borrar Peliculas ::.") 
            borrarPeliculas()
            esperarTecla()
        case "3":
            borrarPantalla()
            print(".:: Mostrar Peliculas ::.") 
            mostrarPeliculas()
            esperarTecla()
        case "4":
            borrarPantalla()
            print(".:: Modificar peliculas::.")
            modificarPeliculas()
            esperarTecla()
            
        case "5":
            borrarPantalla()
            print(".:: Buscar peliculas ::.")
            buscarPeliculas()
            esperarTecla()
            
        case "6":
            borrarPantalla()
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            borrarPantalla() 
            input("Opción invalida vuelva a intentarlo ... por favor")