peliculas=[]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  peliculas.append(input("Ingresa el nombre: ").upper().strip())
  input("La operacion se realizó con exito")

def consultarPeliculas():
  borrarPantalla()
  print(".:: Consultar Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
        print(f"{i+1}: {peliculas[i]}")
  else:
    print("No hay peliculas")
  esperarTecla()

def vaciarPeliculas():
    borrarPantalla()
    print("Borrar todas las peliculas del sistema")
    resp=input("Deseas borrar todas las peliculas?").upper
    if resp == "SI":
       peliculas.clear()
       input("La operacion se realizó con exito")

def buscarPeliculas():
    borrarPantalla()
    print("Buscar peliculas")
    pelicula_buscar=input("Ingrese el nombre de la pelicula\n").upper().strip()
    encontro=0
    if not (pelicula_buscar in peliculas):
       print("No se encuentra la pelicula a buscar")

    else:
        for i in range(0,len(peliculas)):
          if pelicula_buscar == peliculas[i]:
            print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla {i}")
            encontro+=1        
        
        print(f"Tenemos {encontro} pelicula(s) con este titulo")
        
    esperarTecla()

def borrarPeliculas():
    borrarPantalla()
    print("Buscar peliculas")
    pelicula_buscar=input("Ingrese el nombre de la pelicula\n").upper().strip()
    borradas=0
    if not (pelicula_buscar in peliculas):
       print("No se encuentra la pelicula a buscar")
    else:
        rsp = "SI"
        while rsp == "SI" and pelicula_buscar in peliculas:
           if pelicula_buscar in peliculas:
              rsp=input("Deseas quitar o borrar la pelicula del sistema(Si/No)?\n").upper()
              if rsp =="SI":
                indice = peliculas.index(pelicula_buscar)
                peliculas.remove(pelicula_buscar)
                print(f"La pelicula que se borro es{pelicula_buscar} y estaba en la casilla {indice+1}")
                borradas+=1
              else:
                esperarTecla()
        print(f"Se borraron {borradas} pelicula(s) con este titulo")
        
    esperarTecla()

def modificarPelicula():
        modificar = input("Cuál desea modificar?\n->")
        try:
            indice = peliculas.index(modificar)
            nuevo_nombre = input("Ingrese el nombre que desea cambiar\n->")
            peliculas[indice] = nuevo_nombre
            print(peliculas)
        except ValueError:
            print("Esta pelicula no existe")

          