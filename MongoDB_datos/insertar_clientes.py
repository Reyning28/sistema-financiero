from pymongo import MongoClient

# Datos de ejemplo
clientes = [
    {"clienteId": 1, "nombre": "Juan Pérez", "email": "juan@example.com"},
    {"clienteId": 2, "nombre": "Ana García", "email": "ana@example.com"},
    {"clienteId": 3, "nombre": "Carlos Martínez", "direccion": "Calle Luna 789", "telefono": "111-222-3335", "email": "carlos.martinez@example.com", "fechaNacimiento": "1979-03-20", "tipoCliente": "Corporativo"},
    {"clienteId": 4, "nombre": "María López", "direccion": "Av. Sol 101", "telefono": "111-222-3336", "email": "maria.lopez@example.com", "fechaNacimiento": "1990-04-25", "tipoCliente": "Personal"},
    {"clienteId": 5, "nombre": "Luis Hernández", "direccion": "Calle Estrella 202", "telefono": "111-222-3337", "email": "luis.hernandez@example.com", "fechaNacimiento": "1982-05-30", "tipoCliente": "Corporativo"},
    {"clienteId": 6, "nombre": "Sofía González", "direccion": "Av. Mar 303", "telefono": "111-222-3338", "email": "sofia.gonzalez@example.com", "fechaNacimiento": "1988-06-15", "tipoCliente": "Personal"},
    {"clienteId": 7, "nombre": "Miguel Rodríguez", "direccion": "Calle Río 404", "telefono": "111-222-3339", "email": "miguel.rodriguez@example.com", "fechaNacimiento": "1975-07-18", "tipoCliente": "Corporativo"},
    {"clienteId": 8, "nombre": "Laura Fernández", "direccion": "Av. Campo 505", "telefono": "111-222-3340", "email": "laura.fernandez@example.com", "fechaNacimiento": "1992-08-23", "tipoCliente": "Personal"},
    {"clienteId": 9, "nombre": "Jorge Sánchez", "direccion": "Calle Bosque 606", "telefono": "111-222-3341", "email": "jorge.sanchez@example.com", "fechaNacimiento": "1981-09-27", "tipoCliente": "Corporativo"},
    {"clienteId": 10, "nombre": "Elena Ramírez", "direccion": "Av. Lago 707", "telefono": "111-222-3342", "email": "elena.ramirez@example.com", "fechaNacimiento": "1987-10-30", "tipoCliente": "Personal"},
    {"clienteId": 11, "nombre": "David Torres", "direccion": "Calle Colina 808", "telefono": "111-222-3343", "email": "david.torres@example.com", "fechaNacimiento": "1973-11-12", "tipoCliente": "Corporativo"},
    {"clienteId": 12, "nombre": "Patricia Flores", "direccion": "Av. Jardín 909", "telefono": "111-222-3344", "email": "patricia.flores@example.com", "fechaNacimiento": "1993-12-05", "tipoCliente": "Personal"},
    {"clienteId": 13, "nombre": "Francisco Rivera", "direccion": "Calle Parque 1010", "telefono": "111-222-3345", "email": "francisco.rivera@example.com", "fechaNacimiento": "1984-01-16", "tipoCliente": "Corporativo"},
    {"clienteId": 14, "nombre": "Lucía Díaz", "direccion": "Av. Montaña 1111", "telefono": "111-222-3346", "email": "lucia.diaz@example.com", "fechaNacimiento": "1991-02-24", "tipoCliente": "Personal"},
    {"clienteId": 15, "nombre": "Alberto Cruz", "direccion": "Calle Valle 1212", "telefono": "111-222-3347", "email": "alberto.cruz@example.com", "fechaNacimiento": "1986-03-12", "tipoCliente": "Corporativo"},
    {"clienteId": 16, "nombre": "Raquel Moreno", "direccion": "Av. Sol 1313", "telefono": "111-222-3348", "email": "raquel.moreno@example.com", "fechaNacimiento": "1994-04-14", "tipoCliente": "Personal"},
    {"clienteId": 17, "nombre": "Ricardo Ortiz", "direccion": "Calle Nube 1414", "telefono": "111-222-3349", "email": "ricardo.ortiz@example.com", "fechaNacimiento": "1983-05-19", "tipoCliente": "Corporativo"},
    {"clienteId": 18, "nombre": "Gabriela Méndez", "direccion": "Av. Playa 1515", "telefono": "111-222-3350", "email": "gabriela.mendez@example.com", "fechaNacimiento": "1995-06-22", "tipoCliente": "Personal"},
    {"clienteId": 19, "nombre": "Manuel Chávez", "direccion": "Calle Brisa 1616", "telefono": "111-222-3351", "email": "manuel.chavez@example.com", "fechaNacimiento": "1980-07-10", "tipoCliente": "Corporativo"},
    {"clienteId": 20, "nombre": "Adriana Ramos", "direccion": "Av. Árbol 1717", "telefono": "111-222-3352", "email": "adriana.ramos@example.com", "fechaNacimiento": "1990-08-28", "tipoCliente": "Personal"},
    {"clienteId": 21, "nombre": "Fernando Guzmán", "direccion": "Calle Roca 1818", "telefono": "111-222-3353", "email": "fernando.guzman@example.com", "fechaNacimiento": "1985-09-07", "tipoCliente": "Corporativo"},
    {"clienteId": 22, "nombre": "Isabel Soto", "direccion": "Av. Campo 1919", "telefono": "111-222-3354", "email": "isabel.soto@example.com", "fechaNacimiento": "1989-10-11", "tipoCliente": "Personal"},
    {"clienteId": 23, "nombre": "Santiago Vargas", "direccion": "Calle Mar 2020", "telefono": "111-222-3355", "email": "santiago.vargas@example.com", "fechaNacimiento": "1978-11-22", "tipoCliente": "Corporativo"},
    {"clienteId": 24, "nombre": "Teresa Castillo", "direccion": "Av. Río 2121", "telefono": "111-222-3356", "email": "teresa.castillo@example.com", "fechaNacimiento": "1996-12-19", "tipoCliente": "Personal"},
    {"clienteId": 25, "nombre": "Roberto Peña", "direccion": "Calle Sol 2222", "telefono": "111-222-3357", "email": "roberto.pena@example.com", "fechaNacimiento": "1981-01-23", "tipoCliente": "Corporativo"},
    {"clienteId": 26, "nombre": "Andrea Silva", "direccion": "Av. Viento 2323", "telefono": "111-222-3358", "email": "andrea.silva@example.com", "fechaNacimiento": "1993-02-27", "tipoCliente": "Personal"},
    {"clienteId": 27, "nombre": "Pablo Molina", "direccion": "Calle Luna 2424", "telefono": "111-222-3359", "email": "pablo.molina@example.com", "fechaNacimiento": "1984-03-08", "tipoCliente": "Corporativo"},
    {"clienteId": 28, "nombre": "Julia Herrera", "direccion": "Av. Mar 2525", "telefono": "111-222-3360", "email": "julia.herrera@example.com", "fechaNacimiento": "1991-04-05", "tipoCliente": "Personal"},
    {"clienteId": 29, "nombre": "Raúl Romero", "direccion": "Calle Tierra 2626", "telefono": "111-222-3361", "email": "raul.romero@example.com", "fechaNacimiento": "1977-05-15", "tipoCliente": "Corporativo"},
    {"clienteId": 30, "nombre": "Marta Aguilar", "direccion": "Av. Sol 2727", "telefono": "111-222-3362", "email": "marta.aguilar@example.com", "fechaNacimiento": "1986-06-24", "tipoCliente": "Personal"},
    {"clienteId": 31, "nombre": "Guillermo Núñez", "direccion": "Calle Estrella 2828", "telefono": "111-222-3363", "email": "guillermo.nunez@example.com", "fechaNacimiento": "1989-07-30", "tipoCliente": "Corporativo"}
    # Agrega más clientes según sea necesario
]

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.SistemaFinanciero
clientes_collection = db.clientes

# Insertar o actualizar documentos en MongoDB
for cliente in clientes:
    clientes_collection.update_one({"clienteId": cliente["clienteId"]}, {"$set": cliente}, upsert=True)

client.close()
