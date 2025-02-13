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

def informeServicios ():
    for servicios in dicServicios['servicios']:
        print(f"Servicio: {servicios['nombreServicio']} / Precio: ${servicios['precioServicio']} / Caracteristicas: {servicios['caracteristica']} ")
    print (f"\nLa compañia ofrece un total de {servicios['numeroServicio']} servicios. ")
