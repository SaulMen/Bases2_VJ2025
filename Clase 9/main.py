import csv
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["graduaciones"]
coleccion = db["egresados"]

coleccion.delete_many({})

def convertir_entero(valor):
    try:
        return int(valor)
    except ValueError:
        return None
 
with open("graduaciones_2010.csv", newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        
        fila["anio_examen_publico"] = convertir_entero(fila["anio_examen_publico"])
        fila["mes_examen_publico"] = convertir_entero(fila["mes_examen_publico"])
        fila["anio_nacimiento"] = convertir_entero(fila["anio_nacimiento"])
        fila["anio_ingreso_carrera"] = convertir_entero(fila["anio_ingreso_carrera"])
        fila["promedio_al_graduarse"] = convertir_entero(fila["promedio_al_graduarse"])
        
        coleccion.insert_one(fila)