
"""
Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener 
como las listas indices numericos tiene alfanumericos.
Es decir algo parecido comoo los objetos.
También se conoce como un arrerglo asosiativo u Objeto JSON
El diccionario es una colección ordenada y modificable.
No hay miembros duplicados
"""

import os
os.system("cls")

#paises = ["Mexico","Brasil","Canada","España"]
pais_mx = {"nombre":"México",
        "capital":"CDMX",
        "poblacion":1200000,
        "idioma":"español"}
pais_bs = {"nombre":"Brasil",
        "capital":"Brasilia",
        "poblacion":1400000,
        "idioma":"Portugues"}
pais_can= {"nombre":"Canada",
        "capital":"Ottawa",
        "poblacion":1500000,
        "idioma":["Ingles","Frances"]
        }
alumno1 = {"nombre":"Daniel",
           "apellido_paterno":"Flores",
           "apellido_materno":"Gomez",
           "carrera":"DN",
           "area":"mercadotecnia",
           "Matricula":"3141012543",
           "semestre":"2"}

for i in alumno1:
    print(f"{i} = {alumno1[i]}")

alumno1["telefono"] = "6183456789"

for i in alumno1:
    print(f"{i} = {alumno1[i]}")

