def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\t\t Oprima cualquier tecla para continuar ...")
  input()  

def menuPrincipal():
    borrarPantalla()
    print(  "\n\t\t\t..::: 👤 Sistema de gestión de agenda de contactos 👤 :::... " 
            "\n\t\t 1.- Agregar contacto 📝 " 
            "\n\t\t 2.- Mostrar todos los contactos 📂"
            "\n\t\t 3.- Buscar contacto por nombre 🔍" 
            "\n\t\t 4.- Borrar contacto"
            "\n\t\t 5.- Modificar contacto"
            "\n\t\t 6.- Salir")
    rsp=input("\t\t Elige una opción: ").upper().strip()
    return rsp

def agregarContacto(datos):
    borrarPantalla()
    print("\t\t..::Agregar Contacto::..")
    nombre=input("\t\tIngrese el nombre del contacto: ").upper().strip()
    if nombre in datos:
       print("\n\t\t El contacto ya existe...")
    else:
        telefono = input("\t\tTeléfono: ").upper().strip()
        correo = input("\t\tE-mail: ").upper().strip()
        datos[nombre] = [telefono, correo]
        print("\t\tLa operación se realizó con exito")
    esperarTecla()

def mostrarContacto(datos):
    borrarPantalla()
    print("\t\t..::Mostrar todos los contactos::..")
    if not datos:
       print("\t\tNo hay contactos... ")
    else:
       for nombre,data in datos.items():
          print(f"\t\tNombre: {nombre}\t\t\n Teléfono: {data[0]}\t\t\n E-mail: {data[1]}")

    esperarTecla()

def buscarContacto(datos):
    buscar=input("\t\tIngrese el nombre del contacto: ").upper().strip()
    encontrado = True
    num = 0
    for nombre,data in datos.items():
      if buscar == nombre:
        print(f"\t\tNombre: {nombre} \n\t\t Teléfono: {data[0]} \n\t\t E-mail: {data[1]}")
    if not encontrado:
       print("No se encontró ningun contacto")
    esperarTecla()

def borrarContacto(datos):
    buscar=input("\t\tIngrese el nombre del contacto: ").upper().strip()
    for nombre in datos.items():
      if buscar == nombre:
        datos.pop(buscar)
    esperarTecla()

def modificarContacto(datos):
    buscar=input("\t\tIngrese el nombre del contacto: ").upper().strip()
    for nombre in datos.items():
      if buscar == nombre:
        datos.pop(buscar)
    esperarTecla()