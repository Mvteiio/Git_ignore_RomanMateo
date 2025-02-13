import json

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

def crearUsuario ():
    nombreUsuario = input("Ingresa el nombre completo del usuario: ")
    direccionUsuario = input("Ingresa la direccion del usuario: ")
    infoContacto = input("Escribe el numero de contacto del usuario: ")
    print("\nLista de servicios")
    print("1. Fibra optica. ")
    print("2. Plan Pospago. ")
    print("3. Prepago. ")
    serviciosUsuario = (input("\nQué servicio va a adquirir el usuario (escribe el servicio como se muestra): "))
    
    nuevoUsuario = {
        "nombre": nombreUsuario,
        "direccion": direccionUsuario,
        "infoContacto": infoContacto,
        "tipoCliente": "Nuevo Cliente",
        "servicios": serviciosUsuario,
        "yearInicio": 2025
    }

    dicUsuarios['usuarios'].append(nuevoUsuario)
    print("Usuario agregado con exito :). ")
    guardarUsuariosJSON(dicUsuarios)

def verUsuarios ():
    for usuario in dicUsuarios['usuarios']:
        print (f"Nombre: {usuario['nombre']} / Direccion: {usuario['direccion']} / Contacto: {usuario['infoContacto']} / Serivicio: {usuario['servicios']}") 

def modificarUsuario():
    booleanito = True
    while booleanito == True:
        idUsuario = int(input("\nIngresa el ID del usuario que deseas modificar: "))
        for usuario in dicUsuarios['usuarios']:
            if usuario['identificador']==idUsuario:
                eleccionModificar = input(f"\nVas a modificar a: {usuario['nombre']}?(S/N): ")
                match eleccionModificar:
                    case "S":
                        nombreModificar = input("Escribe el nuevo nombre del usuario: ")
                        direccionModificar = input("Escribe la nueva direccion del usuario: ")
                        contactoModificar = input("Escribe el nuevo contacto del usuario: ")
                        print("\nLista de servicios")
                        print("1. Fibra optica. ")
                        print("2. Plan Pospago. ")
                        print("3. Prepago. ")
                        serviciosModificar = (input("\nQué servicio va a adquirir el usuario (escribe el servicio como se muestra): "))

                        nuevoUsuario = {
                            "identificador": idUsuario,
                            "nombre": nombreModificar,
                            "direccion": direccionModificar,
                            "infoContacto": contactoModificar,
                            "tipoCliente": "Nuevo Cliente",
                            "servicios": serviciosModificar,
                            "yearInicio": 2025
                        }   

                        dicUsuarios['usuarios'][idUsuario-1]=(nuevoUsuario)
                        print("Usuario modificado con exito. ")
                        guardarUsuariosJSON(dicUsuarios)
                        booleanito = False
                        break
                    case "N":
                        booleanito = True

def eliminarUsuario():
    booleanito = True
    while booleanito == True:
        idUsuario = int(input("\nIngresa el ID del usuario que deseas eliminar: "))
        for usuario in dicUsuarios['usuarios']:
            if usuario['identificador']==idUsuario:
                eleccionModificar = input(f"\nEstas seguro de eliminar a: {usuario['nombre']}?(S/N): ")
                match eleccionModificar:
                    case "S":
                        dicUsuarios['usuarios'].pop(idUsuario-1)
                        print("Usuario eliminado con exito. ")
                        guardarUsuariosJSON(dicUsuarios)
                        booleanito = False
                        break
                    case "N":
                        booleanito = True

def asignarCategoria ():
    idUsuario = int(input("\nIngresa el ID del usuario al que deseas asignar una categoria: "))
    for usuario in dicUsuarios['usuarios']:
        if usuario['identificador']==idUsuario:
            
            if (2025-usuario['yearInicio']) > 10:
                usuario['tipoCliente']="Cliente Leal"
                print(f"{usuario['nombre']}, lleva mas de 10 años con la compañia, es un cliente leal.")
                print("Tipo de cliente guardado con exito")
                guardarUsuariosJSON(dicUsuarios)

            elif (2025-usuario['yearInicio']) < 5:
                usuario['tipoCliente']="Cliente Nuevo"
                print(f"{usuario['nombre']}, lleva menos de 5 años con la compañia, es un cliente nuevo.")
                print("Tipo de cliente guardado con exito")
                guardarUsuariosJSON(dicUsuarios)

            elif (2025-usuario['yearInicio']) > 5 and (2025-usuario['yearInicio']) < 10:
                usuario['tipoCliente']="Cliente Regular"
                print(f"{usuario['nombre']}, lleva mas de 5 años con la compañia, pero no mas de 10, es un cliente regular.")
                print("Tipo de cliente guardado con exito")
                guardarUsuariosJSON(dicUsuarios)
                

               
               
               
        








   
   
   
   
   
    