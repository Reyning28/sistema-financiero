
--DATOS
INSERT INTO Sucursales (Nombre,Direccion, Telefono) VALUES 
('Sucursal Central', 'Av. Principal 123', '123-456-7890');

INSERT INTO Clientes (Nombre, Apellido, Direccion, Telefono, Email, Fecha_de_nacimiento, Tipo_de_cliente) VALUES 
('Juan', 'P�rez', 'Calle Falsa 123', '111-222-3333', 'juan.perez@example.com', '1980-01-01', 'Personal');

INSERT INTO Empleados (Nombre, Apellido, Cargo, Salario, Fecha_de_contratacion, ID_Sucursal) VALUES 
('Ana', 'G�mez', 'Gerente', 50000, '2020-01-01', 1);

INSERT INTO Cuentas (N�mero_de_cuenta, Tipo_de_cuenta, Saldo, Fecha_de_apertura, ID_Cliente) VALUES 
('1234567890', 'Ahorros', 1000.00, '2021-01-01', 1);

INSERT INTO Pr�stamos (Monto, Tasa_de_inter�s, Plazo, Fecha_de_inicio, ID_Cliente, ID_Empleado) VALUES 
(5000.00, 5.5, 24, '2022-01-01', 1, 1);

INSERT INTO Tarjetas (N�mero_de_tarjeta, Tipo_de_tarjeta, Fecha_de_expiraci�n, L�mite_de_cr�dito, ID_Cuenta, ID_Cliente) VALUES 
('9876543210', 'Cr�dito', '2025-01-01', 2000.00, 1, 1);

INSERT INTO Transacciones (Fecha, Monto, Tipo_de_transacci�n, ID_Cuenta_origen, ID_Cuenta_destino) VALUES 
('2023-01-01 10:00:00', 100.00, 'Dep�sito', 1, NULL);
