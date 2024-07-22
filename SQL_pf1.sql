--TABLAS


CREATE TABLE Clientes(
ID_Cliente INT PRIMARY KEY IDENTITY(1,1),
Nombre NVARCHAR(50),
Apellido NVARCHAR(50),
Direccion NVARCHAR(100),
Telefono NVARCHAR(20),
Email NVARCHAR(50),
Fecha_de_Nacimiento DATE,
Tipo_de_Cliente NVARCHAR(20)

);

CREATE TABLE Sucursales(
ID_Sucursal INT PRIMARY KEY IDENTITY(1,1),
Nombre NVARCHAR(50),
Direccion NVARCHAR(100),
Telefono NVARCHAR(20)

);


CREATE TABLE Empleados(
ID_Empleado INT PRIMARY KEY IDENTITY(1,1),
Nombre NVARCHAR(50),
Apellido NVARCHAR(50),
Cargo NVARCHAR(50),
Salario DECIMAL(10,2),
Fecha_de_contratacion DATE,
ID_Sucursal INT,
FOREIGN KEY (ID_Sucursal) REFERENCES Sucursales(ID_Sucursal)

);

CREATE TABLE Cuentas (
    ID_Cuenta INT PRIMARY KEY IDENTITY(1,1),
    N�mero_de_cuenta NVARCHAR(20),
    Tipo_de_cuenta NVARCHAR(20),
    Saldo DECIMAL(18, 2),
    Fecha_de_apertura DATE,
    ID_Cliente INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
);

CREATE TABLE Transacciones (
    ID_Transacci�n INT PRIMARY KEY IDENTITY(1,1),
    Fecha DATETIME,
    Monto DECIMAL(18, 2),
    Tipo_de_transacci�n NVARCHAR(20),
    ID_Cuenta_origen INT,
    ID_Cuenta_destino INT,
    FOREIGN KEY (ID_Cuenta_origen) REFERENCES Cuentas(ID_Cuenta),
    FOREIGN KEY (ID_Cuenta_destino) REFERENCES Cuentas(ID_Cuenta)
);

CREATE TABLE Pr�stamos (
    ID_Pr�stamo INT PRIMARY KEY IDENTITY(1,1),
    Monto DECIMAL(18, 2),
    Tasa_de_inter�s DECIMAL(5, 2),
    Plazo INT,
    Fecha_de_inicio DATE,
    ID_Cliente INT,
    ID_Empleado INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
    FOREIGN KEY (ID_Empleado) REFERENCES Empleados(ID_Empleado)
);

CREATE TABLE Tarjetas (
    ID_Tarjeta INT PRIMARY KEY IDENTITY(1,1),
    N�mero_de_tarjeta NVARCHAR(20),
    Tipo_de_tarjeta NVARCHAR(20),
    Fecha_de_expiraci�n DATE,
    L�mite_de_cr�dito DECIMAL(18, 2),
    ID_Cuenta INT,
    ID_Cliente INT,
    FOREIGN KEY (ID_Cuenta) REFERENCES Cuentas(ID_Cuenta),
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
);
