def borrarPantalla():
    import os  
    os.system("cls")

def esperarTecla():
    input("\t\t 🕓Ingrese enter para continuar🕓")

def agregar_Calificaciones(lista):
    borrarPantalla()
    print("\t\t..::📝 Agregar Calificaciones 📝::..")
    nombre = input("\t👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
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
    
    lista.append([nombre]+calificaciones)
    print("\tAcción realizada con exito")
def mostrar_Calificaciones(lista):
    borrarPantalla()
    print("\t   ..::🔍 Mostrar Calificaciones 🔍::..")
    print(f"\t{'-'*40}")
    if len(lista)>0:
        print(f"\t{'Nombre':<15} {'Calf. 1'} {'Calf. 2'} {'Calf. 3'}")
        msj = ""
        for fila in lista:
            for i in range(0,len(fila)):
                msj += f"\t{fila[i]:<15} " if i == 0 else f"{fila[i]:<10}"
            msj += "\n"
        print(msj)
        print(f"\t{'-'*40}")
        num = len(lista)
        print(f"\tSon {num} alumnos")
    else:
        print("⚠️ No hay calificaciones en el sistema⚠️")

def calcular_Promedios(lista):
    borrarPantalla()
    print("\t   ..::Calcular promedios::..")
    if len(lista)>0:
        print(f"\t{'Alumno':<15}{'Promedio':<10}")
        print(f"\t{'-'*30}")
        promediogrup = 0
        for fila in lista:
            nombre = fila[0]
            i=1
            suma = 0
            promedio = 0
            while i<=3:
                suma += fila[i]
                i+=1
            promedio = suma/3
            print(f"\t{nombre:<15} {promedio:2f}")
            print(f"\t{'-'*30}")
            promediogrup += promedio

        promediogrup = promediogrup/len(lista)
        print(f"\t 🎓El promedio grupal es: {round(promediogrup,2)}")
    else:
        print("\t\t ⚠️ No hay calificaciones registradas en el sistema⚠️")

def calcular_Promedios2(lista):
    print("..::Calcular promedios::..")
    if len(lista)>0:
        print(f"\t{'Alumno':<15}{'Promedio':<10}")
        print(f"\t{'-'*30}")
        promediogrup = 0
        for fila in lista:
            nombre = fila[0]
            promedio = round(sum(fila[1:])/3,2)
            print(f"\t{nombre:<15} {promedio:2f}")
            print(f"\t{'-'*30}")
            promediogrup += promedio

        promediogrup = round(promediogrup/len(lista),2)
        print(f"👨🏻‍🎓El promedio grupal es: {round(promediogrup,2)}")
    else:
        print("⚠️ No hay calificaciones registradas en el sistema⚠️")


"""     for i in range(0,len(lista)):
        prom = round(((lista[i][1]+lista[i][2]+lista[i][3])/3),2)
        lista[i].append(prom)
    print("Promedios calculados") """


def menu_Principal():
    borrarPantalla()
    print("\n\t     ..::: 📑🦬 Calificaciones UTD 🦬 📑 :::... " 
            "\n\t..::: Sistema de Gestión de Calificaciones :::..." 
            "\n\t 1️⃣.- Agregar" 
            "\n\t 2️⃣.- Mostrar"
            "\n\t 3️⃣.- Calcular promedios " 
            "\n\t 4️⃣.- Buscar alumnos "
            "\n\t 5.- Salir ")
    rsp=input("\t\t 👉Elige una opción: ").upper()
    return rsp

def buscarAlumno(lista):
    borrarPantalla()
    print("..::Buscar Alumno::..")
    buscar = input("Ingrese el alumno para buscar: \n").strip().upper()
    num = 0
    if len(lista)>0:
        for fila in lista:
            if buscar in fila:
                num += 1
                print(f"\t{'-'*40}") 
                print(f"\t{'Nombre':<15} {'Calf. 1'} {'Calf. 2'} {'Calf. 3'}")
                msj = ""
                for i in range(0,len(fila)):
                    msj += f"\t{fila[i]:<15} " if i == 0 else f"{fila[i]:<10}"
                msj += "\n"
                print(msj)
                print(f"\t{'-'*40}") 
                
        if num == 0: 
            print("No se encontraron coincidencias un alumno")
        else:
            print(f"Se encontraron {num} alumnos")
    else:
        print("No hay alumnos")


    esperarTecla()