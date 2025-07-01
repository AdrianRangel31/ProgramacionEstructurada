from agenda import *

opcion=True
agenda = {}
while opcion:
    rsp = menuPrincipal()
    match rsp:
        case "1":
            agregarContacto(agenda)
        case "2":
            mostrarContacto(agenda)
        case "3":
            buscarContacto(agenda)
        case "4":
            borrarContacto(agenda)
        case "5":
            modificarContacto(agenda)
        case "6":
            opcion=False
        case _:
            borrarPantalla() 
            input("\t\tOpción invalida vuelva a intentarlo ... por favor")
