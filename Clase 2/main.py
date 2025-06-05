from datetime import datetime, timedelta
from faker import Faker
import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '$2a0U0l0',
    'database': 'ejemplo2'
}

NUM_USERS = 45000

fake = Faker('es_ES')

def connect():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        print("Generando usuarios...")
        clientes_ids = []

        for i in range(NUM_USERS):
            nombre = fake.name()
            correo = fake.email()
            telefono = fake.phone_number()[:12]
            simbolo = telefono.replace("+", "")
            espacio = simbolo.replace(" ", "")
            cursor.execute("INSERT INTO USUARIO (nombre, correo, telefono) VALUES (%s, %s, %s)",
                           (nombre, correo, espacio[:8]))
            clientes_ids.append(cursor.lastrowid)
        conn.commit()

        print("\nDatos generados y cargados exitosamente!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexión a la base de datos cerrada.")



if __name__=="__main__":
    connect()

## mysqldump -u root -p ejemplo2 > clase2_full