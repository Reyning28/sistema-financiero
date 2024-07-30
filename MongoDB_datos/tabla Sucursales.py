import pyodbc
import pymongo

def extract_and_load_sucursales():
    # Conexión a SQL Server
    sql_conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-6O57TFH\SQLEXPRESS;DATABASE=SistemaFinanciero;Trusted_Connection=yes')
    sql_cursor = sql_conn.cursor()

    # Conexión a MongoDB
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
    mongo_db = mongo_client.SistemaFinanciero
    sucursales_collection = mongo_db.sucursales

    # Extraer datos de Sucursales de SQL Server
    sql_cursor.execute("SELECT * FROM Sucursales")
    rows = sql_cursor.fetchall()

    # Transformar y cargar datos en MongoDB
    for row in rows:
        sucursal = {
            "sucursalId": row.ID_Sucursal,
            "nombre": row.Nombre,
            "direccion": row.Direccion,
            "telefono": row.Telefono
        }
        sucursales_collection.update_one({"sucursalId": sucursal["sucursalId"]}, {"$set": sucursal}, upsert=True)

    # Cerrar conexiones
    sql_conn.close()
    mongo_client.close()

extract_and_load_sucursales()
