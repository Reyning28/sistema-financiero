import pyodbc
import pymongo
from decimal import Decimal

# Conexión a SQL Server
sql_conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-6O57TFH\SQLEXPRESS;DATABASE=SistemaFinanciero;Trusted_Connection=yes')
sql_cursor = sql_conn.cursor()

# Conexión a MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client.SistemaFinanciero
Empleados_collection = mongo_db.empleados

# Extraer datos de Empleados de SQL Server
sql_cursor.execute("SELECT * FROM Empleados")
rows = sql_cursor.fetchall()

# Transformar y cargar datos en MongoDB
for row in rows:
    empleado = {
        "empleadoId": row.ID_Empleado,
        "nombre": row.Nombre,
        "apellido": row.Apellido,
        "salario": float(row.Salario) if isinstance(row.Salario, Decimal) else row.Salario,
        "fechaDeContratacion": row.Fecha_de_contratacion,
        "puesto": row.Cargo,
        "sucursal": row.ID_Sucursal
    }
    Empleados_collection.update_one({"empleadoId": empleado["empleadoId"]}, {"$set": empleado}, upsert=True)

# Cerrar conexiones
sql_conn.close()
mongo_client.close()
