def llenar(lista):
    if len(lista)==0:
        rsp = "SI"
        while rsp == "SI":
            lista.append(input("Ingrese una palabra: ").upper())
            rsp = input("Otra vez?: ").upper()
        print(lista)
    else:
        print("La lista tiene elementos")

lol = []
llenar(lol)