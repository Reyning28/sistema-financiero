import pyodbc
import pymongo
from decimal import Decimal

# Conexión a SQL Server
sql_conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-6O57TFH\SQLEXPRESS;DATABASE=SistemaFinanciero;Trusted_Connection=yes')
sql_cursor = sql_conn.cursor()

# Conexión a MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client.SistemaFinanciero
Cuentas_collection = mongo_db.cuentas

# Extraer datos de Empleados de SQL Server
sql_cursor.execute("SELECT * FROM Cuentas")
rows = sql_cursor.fetchall()

# Transformar y cargar datos en MongoDB
for row in rows:
    cuenta = {
        "cuentaid": row.ID_Cuenta,
        "numeroDecuenta": row.Número_de_cuenta,
        "tipoDecuenta": row.Tipo_de_cuenta,
        "saldo": float(row.Saldo) if isinstance(row.Saldo, Decimal) else row.Saldo,
        "fechaDeapertura": row.Fecha_de_apertura,
        "clienteid": row.ID_Cliente
        
    }
    Cuentas_collection.update_one({"cuentaid": cuenta["cuentaid"]}, {"$set": cuenta}, upsert=True)

# Cerrar conexiones
sql_conn.close()
mongo_client.close()
