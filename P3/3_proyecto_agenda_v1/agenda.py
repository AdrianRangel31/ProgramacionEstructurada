import mysql.connector
from mysql.connector import Error 
from tabulate import tabulate

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user = "root",
            password = "",
            database = "bd_agenda"
        )
        cursor = conexion.cursor(buffered=True)
        return conexion, cursor
    except Error as e:
        print(f"En este momento no es posible comunicarse con el sistema, intentelo más tarde...{e}")


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\t\tOprima cualquier tecla para continuar ...")
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

def agregarContacto():
    borrarPantalla()
    print("\t\t..::Agregar Contacto::..")
    conexion,cursor = conectar()
    if conexion == None:
      return
    nombre=input("\t\tIngrese el nombre del contacto: ").upper().strip()

    telefono = input("\t\tTeléfono: ").upper().strip()
    correo = input("\t\tE-mail: ").upper().strip()

    cursor.execute(f"insert into contactos (nombre,telefono,correo) values('{nombre}','{telefono}','{correo}')")
    conexion.commit()
    print("\t\tLa operación se realizó con exito")
    esperarTecla()

def mostrarTodo():
    conexion, cursor = conectar()
    if conexion == None:
        return
    cursor.execute("select * from contactos")
    registros = cursor.fetchall()
    msj = [["ID","Nombre","Telefono","Correo"]]
    msj.extend(registros)
    print(f"{tabulate(msj, tablefmt="grid", colalign = ("center",) * 4)}\n")

def mostrarContacto():
    borrarPantalla()
    print("\t\t..::Mostrar todos los contactos::..")
    mostrarTodo()
    esperarTecla()

def buscarContacto():
    borrarPantalla()
    print("\t\t..::Buscar Contacto::..")

    buscar = input("Ingrese el contacto para buscar: \n").strip().upper()
    conexion,cursor = conectar()
    cursor.execute(f"select * from contactos where nombre = '{buscar}' ")
    busqueda = cursor.fetchall()
    if busqueda == []:
        print("No se encontró ningun contacto")
        return
    msj =  [["ID","Nombre","Telefono","Correo"]]
    msj.extend(busqueda)
    print(f"{tabulate(msj, tablefmt="grid", colalign = ("center",) * 4)}\n")
    print("\t\t..::Acción realizada con exito::..")
    esperarTecla()

def borrarContacto():
    borrarPantalla()
    print("\t\t..::Borrar Contacto::..")
    mostrarTodo()
    id = input("Ingrese el ID del contacto que desea borrar: ").upper().strip()
    conexion, cursor = conectar()
    cursor.execute(f"select * from contactos where id = '{id}'")
    contacto = cursor.fetchall()
    if contacto == []:
        print("No se encontró ningun contacto")
        return
    borrarPantalla()
    print("..::Borrar contacto::..")
    msj =  [["ID","Nombre","Telefono","Correo"]]
    msj.extend(contacto)
    print(f"{tabulate(msj, tablefmt="grid", colalign = ("center",) * 4)}\n")
    rsp = input("Seguro que desea eliminar a este contacto?(SI/NO): ").upper().strip()
    if rsp == "SI":
        cursor.execute(f"delete from contactos where id = {id}")
        conexion.commit()


        print("\t\t..::Acción realizada con exito::..")
    else:
        print("\t\t..::No se eliminó ningun registro::..")


def modificarContacto():
    borrarPantalla()
    print("\t\t..::Modificar Contacto::..")
    mostrarTodo()
    mod = input("Ingrese el ID del contacto que desea modificar: ").upper().strip()
    conexion, cursor = conectar()
    cursor.execute(f"select * from contactos where id = '{mod}'")
    contacto = cursor.fetchall()
    if contacto == []:
        print("No se encontró ningun contacto")
        return
    borrarPantalla()
    print("..::Modificar Contacto::..")
    msj = [["ID","Nombre","Telefono","Correo"]]
    msj.extend(contacto)
    print(f"{tabulate(msj, tablefmt="grid", colalign = ("center",) * 4)}\n")

    for i in range(1,4):
        rsp = input(f"Desea modificar el {msj[0][i]}?: ").upper().strip()
        if rsp == "SI":
            nuevo = input("Ingrese el nuevo valor: ")
            campo = ["nombre","telefono","correo"]
            cursor.execute(f"update contactos set {campo[i-1]} = '{nuevo}' where id = {mod}")
            conexion.commit()
           
    print("\t\t..::Acción realizada con exito::..")



    esperarTecla()