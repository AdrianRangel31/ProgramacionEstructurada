import os

def borrar_pantalla():
    os.system("cls")

def esperar():
    input("Ingrese una tecla para continuar")

def agregar(lista):
    nueva_pelicula = input("Ingrese el nombre de la pelicula\n->") 
    lista.append(nueva_pelicula)
    return lista

def eliminar(lista):
    pelicula = input("Cuál desea eliminar?\n->")
    try:
        lista.remove(pelicula)
    except ValueError:
        print("Esta pelicula no existe")
    return lista

def modificar(lista):
        modificar = input("Cuál desea modificar?\n->")
        try:
            indice = lista.index(modificar)
            nuevo_nombre = input("Ingrese el nombre que desea cambiar\n->")
            lista[indice] = nuevo_nombre
            mostrar(lista)
            return lista
        except ValueError:
            print("Esta pelicula no existe")


def buscar(lista):
    buscar = input("Ingrese la pelicula que desea buscar:\n->")
    print(f"La pelicula {buscar} si existe en el sistema" if buscar in lista else "No existe")  

def mostrar(lista):
    print("Peliculas en existencia")
    if len(lista)>0:
        for i in range(0,len(lista)):
            print(f"\t{i+1}.- {lista[i]}")    
    else:
        print("No hay peliculas")