from agenda import *

opcion=True
agenda = {"RAUL":["618372832","CORREO@GMAIL.COM"],
          "JUAN":["618372832","CORREO@GMAIL.COM"],
          "LESLI":["618372832","CORREO@GMAIL.COM"]}
while opcion:
    rsp = menuPrincipal()
    match rsp:
        case "1":
            agregarContacto()
        case "2":
            mostrarContacto()
        case "3":
            buscarContacto()
        case "4":
            borrarContacto()
        case "5":
            modificarContacto()
        case "6":
            opcion=False
        case _:
            borrarPantalla() 
            input("\t\tOpción invalida vuelva a intentarlo ... por favor")
