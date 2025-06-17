import csv
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["estudiantes"]
coleccion = db["aspirantes"]

coleccion.delete_many({})

def convertir_entero(valor):
    try:
        return int(valor)
    except ValueError:
        # Si no se puede convertir a entero (SIN REGISTRO) se retorna None/null
        return None

# retornar valores booleanos
def convertir_booleano(valor):
    if isinstance(valor, str):
        valor = valor.strip().lower()
        if valor in ['true', '1', 'si', 'aprobado']: # cualquiera de estos devuleve true
            return True
        elif valor in ['false', '0', 'no', 'reprobado']: # cualquiera de estos devuleve true
            return False
    return None

with open("pruebas_especificas_2023.csv", newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        
        documento_mongo = {
            "fecha_asignacion": fila["fecha_asignacion"],
            "sexo": fila["sexo"],
            "materia": fila["materia"],
            "carrera_objetivo": fila["carrera_objetivo"],
            "departamento_institucion_educativa": fila["departamento_institucion_ed"],
            "municipio_institucion_educativa": fila["municipio_institucion_"],
            "tipo_institucion_educativa": fila["tipo_institucion_educativa"],
            "correlativo_aspirante": fila["correlativo_aspirante"]
        }

        anio_nacimiento = convertir_entero(fila["anio_nacimiento"])
        if anio_nacimiento is not None:
            documento_mongo["anio_nacimiento"] = anio_nacimiento
        else:
            pass

        numero_evaluacion = convertir_entero(fila["numero_de_fecha_de_evaluaci"])
        if numero_evaluacion is not None:
            documento_mongo["numero_de_fecha_de_evaluacion"] = numero_evaluacion
        else:
            pass

        anio_ingreso = convertir_entero(fila["anio_de_ingreso"])
        if anio_ingreso is not None:
            documento_mongo["anio_de_ingreso"] = anio_ingreso
        else:
            pass

        aprobacion = convertir_booleano(fila["aprobacion"])
        if aprobacion is not None:
            documento_mongo["aprobacion"] = aprobacion
        else:
            pass

        coleccion.insert_one(documento_mongo)

print("Los datos fueron cargados exitosamente")