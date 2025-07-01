"""
List (Array)
Son colecciones o conjunto de datos/valores 
bajo un mismo nombre, para acceder a los valores.
Se hace con un indice numerico.
Nota: Sus valores si son modificables
La lista es una colección ordenada y modificable. Permite
miembros modificables
"""

import os
os.system("cls")
paises = ["México", "Brasil","España","Canada"]
numeros = [23,12,100,34,12]

#Ordenar ascendentemente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

#Añadir o ingresar elementos a una lista
#1er forma

paises.append("Honduras")
print(paises) 

#2da forma
paises.insert(1,"Honduras")
print(paises)


#Eliminar o borrar elementos de una lista
#1er forma
paises.pop(1)
print(paises)
#2da forma
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
print("Brasil" in paises)
print("Si encontre el pais" if "Brasil" in paises else "No encontre")

pais_buscar = input("Dame el pais\n->")
encontrado = False
for i in range(0,len(paises)):
    if paises[i]==pais_buscar:
        encontrado = True
print("Si encontre" if encontrado else "No encontre")


#Contar el numero de veces que aparece un valor
print(f"El numero 12 aparece: {numeros.count(12)} veces")
numeros.append(12)
print(f"El numero 12 aparece: {numeros.count(12)} veces")


#Identificar o conocer el indice de un valor
indice = paises.index("España")
print(indice)
paises.pop(indice)
print(paises)


#Recorrer los valores de la lista
for i in paises:
    print(i)
    
for i in range(0,len(paises)):
    print(f"El valor {i} es: {paises[i]}")  

     
#Unir contenido de listas
print(paises)
print(numeros)
paises.extend(numeros)
print(paises)