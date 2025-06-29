"""Crear un proyecto que permita gestionar (Administrar) peliculas, colocar un menú de opciones
para agregar, eliminar, modificar y consultar peliculas.
Notas:
1.-Utilizar funciones y mandar llamar desde otro archivo
2.-Utilizar listas para almacenar los nombres de peliculas 
"""
from peliculas import *

opc = True
rsp = ""
peliculas = ["Ironman3","Titanic","Spiderman"]
while(opc):
    borrar_pantalla()
    rsp = input("..::Administrador de peliculas::..\n"
          "..a) Agregar peliculas\n"
          "..b) Eliminar peliculas\n"
          "..c) Modificar peliculas\n"
          "..d) Consultar peliculas\n"
          "..e) Ver todos los registros\n"
          "..f) Salir\n->").lower()
    match rsp:
        case "a":
            borrar_pantalla()
            agregar(peliculas)
            mostrar(peliculas)
            esperar()
        case "b":
            borrar_pantalla()
            mostrar(peliculas)
            eliminar(peliculas)
            esperar()
        case "c":
            borrar_pantalla()
            mostrar(peliculas)
            modificar(peliculas)
            esperar()
        case "d":
            borrar_pantalla()
            buscar(peliculas)
            esperar()
        case "e": 
            borrar_pantalla()
            mostrar(peliculas)
            esperar()
        case "f":
            opc=False
            print("Cerrando programa...")
    

