
#diccionario u objeto para almacenar los atributos (Nombre, categoria, clasificación, genéro, idioma)

peliculas={
        "nombre":"",
        "categoria":"",
        "clasificacion":"",
        "genero":"",
        "idioma":""

}
def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def crearPeliculas():
  borrarPantalla()
  print(".:: 📝Alta de Peliculas📝 ::. ")
  
  peliculas.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
  peliculas.update({"categoria":input("Ingresa el categoria: ").upper().strip()})
  peliculas.update({"clasificacion":input("Ingresa el clasificacion: ").upper().strip()})
  peliculas.update({"genero":input("Ingresa el genero: ").upper().strip()})
  peliculas.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
  input("La operacion se realizó con exito✅")

def mostrarPeliculas():
   borrarPantalla()
   print(".:: Alta de Peliculas ::. ")
   print(peliculas)
   if len(peliculas)>0:
    for i in peliculas:
      print(f"\t {(i)} : {peliculas[i]}")

def vaciarPeliculas():
  borrarPantalla()
  print(".:: Borrar o quitar todas las Peliculas ::. ")
  resp = input("¿Deseas quitar o borrar todas las peliculas del sistema?(Si/no)")
  if resp=="si":
    peliculas.clear()
    input("La operacion se realizó con exito")
    
def borrarPeliculas():
    borrar = input("Cuál desea eliminar?\n->")
    try:
        peliculas.remove(borrar)
    except ValueError:
        print("Esta pelicula no existe")
      

def agregarCaracteristicaPeliculas():
  print("Agregar caracteristicas")
  atributo = input("Ingresa la nueva caracteristica de la pelicula").lower().strip()
  valor = input("Ingresa el valor de la caracteristica de la pelicula").upper().strip()
  peliculas[atributo] = valor
  print("La operación se realizo con exito")


def borrarCaracteristicaPeliculas():
   borrarPantalla()
   print("Borrar caracteristicas de peliculas")
   if len(peliculas)>0:
      print("Valores actuales")
      try:
        for i in peliculas:
          print(f"{(i)} : {peliculas[i]}")
          resp = input("Desea borrar una caracteristica?(Si/No)\n").lower().strip()
          if resp =="si":
            atributo = input("Escribe la caracteristica que deseas borrar o quitar: ").lower().strip()
          
            peliculas.pop(atributo)
          borrarPantalla()
      except KeyError:
        print("Este atributo no existe")
        esperarTecla()
      except RuntimeError:
        print("La operación se ha realizado con exito")
        esperarTecla()
         
   else:
      print("No hay peliculas en el sistema")
      esperarTecla()

      
def modificarCaracteristicaPeliculas():
   borrarPantalla()
   print("Modificar caracteristicas de peliculas")
   if len(peliculas)>0:
      print("Valores actuales")
      for i in peliculas:
         print(f"{(i)} : {peliculas[i]}")
         resp = input("Desea modificar una caracteristica?(Si/No)").lower().strip()
         if resp =="si":
          peliculas.update({i: input("El nuevo valor: ").upper().strip()})
          print("La operación se ha realizado con exito")
          esperarTecla()
         borrarPantalla()
   else:
      print("No hay peliculas en el sistema")
      esperarTecla()




""" def modificarCaracteristicaPeliculas():
  print("Modificar caracteristicas")
  print(peliculas.keys())
  clave = input("Ingresa la caracteristica de la pelicula a modificar").lower().strip()
  nuevaclave = input("Ingresa la modificacion de la caracteristica").lower().strip()
  if clave in peliculas:
        peliculas[nuevaclave] = peliculas.pop(clave)
        print("La operación se realizo con exito")
  else:
     print("La clave ingresada no existe")

def borrarCaracteristicaPeliculas():
  print("Borrar caracteristicas")
  print(peliculas.keys())
  clave = input("Ingresa la caracteristica de la pelicula a borrar").lower().strip()
  if clave in peliculas:
        peliculas.pop(clave)
        print("La operación se realizo con exito")
  else:
     print("La clave ingresada no existe")
 """

 



