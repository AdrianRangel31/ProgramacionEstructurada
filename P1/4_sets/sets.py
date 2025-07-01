"""
Set es una colección desordenada, inmutable y no indexada.
No hay miembros duplicados
"""
"""
personas = {"Ramiro","Choche","Lupe"}
print(personas)
personas.add("El peje")
print(personas)
personas.pop()
print(personas)
personas.clear()
print(personas)

varios = {3.12,2,True,"Hoal"}
"""
#Crear un programa que solicite los email de los alumnos de la utd, almacenar en una lista y posteriormente mostrar
#en pantalla los email sin duplicados
rsp = "si"
email_Set = []
while(rsp=="si"):
    email_Set.append(input("Ingrese el correo\n->"))
    rsp = input("Deseas ingresar otro?\n->").lower()
    
print(email_Set)
set1 = set(email_Set)
print(set1)
email_Set = list(set1)
print(email_Set)
