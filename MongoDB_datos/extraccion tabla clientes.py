import pyodbc
import pymongo

# Conexión a SQL Server
sql_conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=DESKTOP-6O57TFH\SQLEXPRESS;DATABASE=SistemaFinanciero;Trusted_Connection=yes')
sql_cursor = sql_conn.cursor()

# Conexión a MongoDB
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client.SistemaFinanciero
clientes_collection = mongo_db.clientes

# Extraer datos de Clientes de SQL Server
sql_cursor.execute("SELECT * FROM Clientes")
rows = sql_cursor.fetchall()

# Transformar y cargar datos en MongoDB
for row in rows:
    cliente = {
        "clienteId": row.ID_Cliente,
        "nombre": row.Nombre,
        "apellido": row.Apellido,
        "direccion": row.Direccion,
        "telefono": row.Telefono,
        "email": row.Email,
        "fechaDeNacimiento": row.Fecha_de_Nacimiento,
        "tipoDeCliente": row.Tipo_de_Cliente
    }
    clientes_collection.update_one({"clienteId": cliente["clienteId"]}, {"$set": cliente}, upsert=True)

# Cerrar conexiones
sql_conn.close()
mongo_client.close()
