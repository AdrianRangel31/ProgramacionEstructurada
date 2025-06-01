import os
os.system("cls")
""" 
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros = [10, 29, 36, 41, 52]
print(numeros) 

#Ejemplo 2 Crear una lista de palabras y posteriormenet buscar la coincidencia de una palabra
palabras = ["Manzana", "Pera", "Sandia", "Melon"]
palabra_Buscar = input("Ingrese la palabra a buscar\n->")
#1era forma
print(f"Si existe\nEl numero de veces que se encontrol la palabra es {palabras.count(palabra_Buscar)}"
       if palabra_Buscar in palabras else "No existe")
#2da forma
found = False
for i in palabras:
    if i == palabra_Buscar:
        found = True
print("Si existe" if found else "No existe")
#3era forma
found = False
for i in range(0,len(palabras)):
    if palabras[i] == palabra_Buscar:
        found = True
print("Si existe" if found else "No existe")

"""

""" #Ejemplo 3 Añadir elementos a una lista
numeros = []
opc = True
while(opc):
    numeros.append(float(input("Ingrese el elemento para añadir a la lista\n->")))
    rsp = input("¿Desea añadir otro?\n->").lower()
    if rsp == "si":
        opc = True
    else:
        opc = False
print(numeros) """

#Crear una lista multidimensional que sea una agenda
agenda = [["Carlos","618789109"],
          ["Juan","61898765"],
          ["Pablo","61867548"]]

msj = ""
for i in range(0,3):
    for j in range(0,2):
        msj += agenda[i][j] + " "
    msj += "\n"
print(msj)
