import mysql.connector
from mysql.connector import Error 
from tabulate import tabulate

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user = "root",
            password = "",
            database = "bd_calificaciones"
        )
        cursor = conexion.cursor(buffered=True)
        return conexion, cursor
    except Error as e:
        print(f"En este momento no es posible comunicarse con el sistema, intentelo más tarde...{e}")

def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input("\t\t 🕓Ingrese enter para continuar🕓")

def agregar_Calificaciones():
    borrarPantalla()
    print("\t\t..::📝 Agregar Calificaciones 📝::..")
    conexion, cursor = conectar()
    if conexion == None:
        return
    nombre = input("\t👤 Nombre del alumno: ").upper().strip()
    calificaciones = [nombre]
    for i in range(1,4):
        continua = True
        while continua:
            try:
                cal = float(input(f"\t✏️ Ingrese la calificación {i}: "))
                if cal >=0 and cal <11:
                    calificaciones.append(cal)
                    continua = False
                else: 
                    print("\t ⚠️Ingrese un numero valido⚠️")
            except ValueError:
                print("\t ⚠️Ingrese un valor numerico⚠️")
    
    cursor.execute(f"insert into alumnos (nombre,cal1,cal2,cal3) values ('{calificaciones[0]}',{calificaciones[1]},{calificaciones[2]},{calificaciones[3]})")
    cursor.execute(f"insert into promedios (nombre) values ('{nombre}')")
    conexion.commit()
    print("\tAcción realizada con exito")


def mostrar_Calificaciones():
    borrarPantalla()
    print("\t   ..::🔍 Mostrar Calificaciones 🔍::..")
    todoCalificaciones()
    print("\t\t..::Acción realizada con exito::..")

def todoCalificaciones():
    conexion, cursor = conectar()
    if conexion == None:
        return
    cursor.execute("select id,nombre,cal1,cal2,cal3 from alumnos")
    registros = cursor.fetchall()
    msj = [["ID","Nombre","Calificación 1","Calificación 2","Calificación 3"]]
    msj.extend(registros)
    print(f"{tabulate(msj, tablefmt="grid", colalign = ("center",) * 5)}\n")


def calcular_Promedios():
    borrarPantalla()
    print("\t   ..::Calcular promedios::..")
    conexion, cursor = conectar()
    if conexion == None:
        return
    cursor.execute("select cal1,cal2,cal3 from alumnos")
    promedios = []
    registros = cursor.fetchall()
    for fila in registros:
        promedios.append(round((fila[0]+fila[1]+fila[2])/3,2))
    cursor.execute("select id from alumnos ORDER BY id ASC")
    registros = cursor.fetchall()
    for i in range(0,len(registros)):
        cursor.execute(f"update promedios set promedio = {promedios[i]} where id = {registros[i][0]}")
        conexion.commit()
    
    cursor.execute("select * from promedios")
    promedios = cursor.fetchall()
    msj = [["ID","NOMBRE","PROMEDIO"]]
    msj.extend(promedios)
    print(f"\n{tabulate(msj, tablefmt="grid", colalign = ("center",) * 3)}\n")
    print("\t\t..::Acción realizada con exito::..")

    




def menu_Principal():
    borrarPantalla()
    print("\n\t     ..::: 📑🦬 Calificaciones UTD 🦬 📑 :::... " 
            "\n\t..::: Sistema de Gestión de Calificaciones :::..." 
            "\n\t 1.- Agregar" 
            "\n\t 2.- Mostrar"
            "\n\t 3.- Calcular promedios " 
            "\n\t 4.- Buscar alumnos "
            "\n\t 5.- Modificar alumnos "
            "\n\t 6.- Dar de baja alumnos "
            "\n\t 7.- Salir ")
    rsp=input("\t\t 👉Elige una opción: ").upper()
    return rsp

def buscarAlumno():
    borrarPantalla()
    print("..::Buscar Alumno::..")
    buscar = input("Ingrese el alumno para buscar: \n").strip().upper()
    conexion,cursor = conectar()
    cursor.execute(f"select * from alumnos where nombre = '{buscar}' ")
    busqueda = cursor.fetchall()

    if busqueda == []:
        print("No se encontró ningun alumno")
        return
    cursor.execute(f"select promedio from promedios where nombre = '{buscar}'")
    promedios = cursor.fetchall()


    msj = [["ID","Nombre","Calificación 1","Calificación 2","Calificación 3","Promedio"]]
    for i in range(0,len(promedios)):
        busqueda[i] = list(busqueda[i])
        busqueda[i].extend(promedios[i])
    msj.extend(busqueda)
    print(f"{tabulate(msj, tablefmt="grid", colalign = ("center",) * 5)}\n")
    print("\t\t..::Acción realizada con exito::..")

def modificarAlumno():
    borrarPantalla()
    print("..::Modificar Calificaciones::..")
    todoCalificaciones()
    mod = input("Ingrese el ID del alumno que desea modificar: ").upper().strip()
    conexion, cursor = conectar()
    cursor.execute(f"select * from alumnos where id = '{mod}'")
    alumno = cursor.fetchall()
    if alumno == []:
        print("No se encontró ningun alumno")
        return
    borrarPantalla()
    print("..::Modificar Calificaciones::..")
    msj = [["ID","Nombre","Calificación 1","Calificación 2","Calificación 3"]]
    msj.extend(alumno)
    print(f"{tabulate(msj, tablefmt="grid", colalign = ("center",) * 5)}\n")

    for i in range(2,5):
        rsp = input(f"Desea modificar {msj[0][i]}?: ").upper().strip()
        if rsp == "SI":
            nuevo = input("Ingrese el nuevo valor: ")
            cal = ["cal1","cal2","cal3"]
            cursor.execute(f"update alumnos set {cal[i-2]} = {nuevo} where id = {mod}")
            conexion.commit()
           
    print("\t\t..::Acción realizada con exito::..")



def borrarAlumno():
    borrarPantalla()
    print("..::Dar de baja del sistema::..")
    todoCalificaciones()
    id = input("Ingrese el ID del alumno que desea dar de baja: ").upper().strip()
    conexion, cursor = conectar()
    cursor.execute(f"select * from alumnos where id = '{id}'")
    alumno = cursor.fetchall()
    if alumno == []:
        print("No se encontró ningun alumno")
        return
    borrarPantalla()
    print("..::Dar de baja del sistema::..")
    msj = [["ID","Nombre","Calificación 1","Calificación 2","Calificación 3"]]
    msj.extend(alumno)
    print(f"{tabulate(msj, tablefmt="grid", colalign = ("center",) * 5)}\n")

    rsp = input("Seguro que desea dar de baja a este alumno?(SI/NO): ").upper().strip()
    if rsp == "SI":
        cursor.execute(f"delete from promedios where id = {id}")
        cursor.execute(f"delete from alumnos where id = {id}")
        conexion.commit()


        print("\t\t..::Acción realizada con exito::..")
    else:
        print("\t\t..::No se eliminó ningun registro::..")
