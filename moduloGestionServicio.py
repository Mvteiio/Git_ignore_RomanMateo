import json

def abrirServiciosJSON():
    dicFinal={}
    with open("./servicios.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarServiciosJSON(dic):
    with open("./servicios.json",'w') as outFile:
        json.dump(dic,outFile)

dicServicios = {}
dicServicios = abrirServiciosJSON()

def agregarServicio ():
    servicioNuevo = input("Escribe el nombre del nuevo servicio: ")
    precioNuevo = int(input("Ingresa el precio del nuevo servicio: "))
    caracteristicaNuevo = input ("Ingresa la caracteristica del servicio: ")

    nuevoServicio = {
        "nombreServicio": servicioNuevo,
        "precioServicio": precioNuevo,
        "caracteristica": caracteristicaNuevo
    }

    dicServicios['servicios'].append(nuevoServicio)
    print("Servicio agregado con exito. ")
    guardarServiciosJSON(dicServicios)

def verServiciosActivos():
    for servicios in dicServicios['servicios']:
        print(f"Servicio: {servicios['nombreServicio']} / Precio: ${servicios['precioServicio']} / Caracteristicas: {servicios['caracteristica']} ")

def modificarServicio ():
    for servicios in dicServicios['servicios']:
        print (f"{servicios['numeroServicio']}. Servicio:  {servicios['nombreServicio']}")
    eleccionModificar = int(input("Cual servicio deseas modificar?: "))
    for servicios in dicServicios['servicios']:
        if servicios['numeroServicio'] == eleccionModificar:
            servicioNombreMod = input("Cual sera el nuevo nombre del servicio: ")
            servicioPrecioMod = int(input("Cual es el nuevo precio del servicio: "))
            servicioCaracMod = input("Escribe las nuevas caracteristicas del servicio: ")

            servicioMod = {
                "numeroServicio": eleccionModificar,
                "nombreServicio": servicioNombreMod,
                "precioServicio": servicioPrecioMod,
                "caracteristica": servicioCaracMod  
            }

            dicServicios['servicios'][eleccionModificar-1]=(servicioMod)
            print ("Servicio modificado con exito.")
            guardarServiciosJSON(dicServicios)
        
def eliminarServicio ():
    for servicios in dicServicios['servicios']:
        print (f"{servicios['numeroServicio']}. Servicio:  {servicios['nombreServicio']}")
    eleccionEliminar = int(input("Cual servicio deseas eliminar?: "))
    for servicios in dicServicios['servicios']:
        if servicios['numeroServicio'] == eleccionEliminar:
            dicServicios['servicios'].pop(eleccionEliminar-1)
            print ("Servicio Eliminado con exito. ")
            guardarServiciosJSON(dicServicios)



