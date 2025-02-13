import json
from menu import *
from moduloUsuarios import *

def abrirUsuariosJSON():
    dicFinal={}
    with open("./usuarios.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarUsuariosJSON(dic):
    with open("./usuarios.json",'w') as outFile:
        json.dump(dic,outFile)

dicUsuarios = {}
dicUsuarios = abrirUsuariosJSON()

menuPrincipal()
eleccionAdministrador = int(input("Que deseas hacer?: "))
match eleccionAdministrador:
    case 1:
            crudAdministrador()
            eleccionCRUD = int(input("\nQue deseas hacer?: "))
            match eleccionCRUD:
                    case 1:
                        crearUsuario()
                    case 2:
                        verUsuarios()
                    case 3:
                      modificarUsuario()
                    case 4:
                      eliminarUsuario()
    case 2:
        asignarCategoria()


                        
                      
