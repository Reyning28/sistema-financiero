import pyodbc
import pymongo
from decimal import Decimal

# Conexión a SQL Server
sql_conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-6O57TFH\SQLEXPRESS;DATABASE=SistemaFinanciero;Trusted_Connection=yes')
sql_cursor = sql_conn.cursor()

# Conexión a MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client.SistemaFinanciero
transacciones_collection = mongo_db.transacciones

# Extraer datos de Transacciones de SQL Server
sql_cursor.execute("SELECT * FROM Transacciones")
rows = sql_cursor.fetchall()

# Transformar y cargar datos en MongoDB
for row in rows:
    transaccion = {
        "transaccionId": row.ID_Transacción,
        "fecha": row.Fecha,
        "monto": float(row.Monto) if isinstance(row.Monto, Decimal) else row.Monto,
        "tipoDetransaccion": row.Tipo_de_transacción,
        "cuentaId": row.ID_Cuenta_origen,
        "destinoId": row.ID_Cuenta_destino
    }
    transacciones_collection.update_one({"transaccionId": transaccion["transaccionId"]}, {"$set": transaccion}, upsert=True)

# Cerrar conexiones
sql_conn.close()
mongo_client.close()
