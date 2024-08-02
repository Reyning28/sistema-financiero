--CONSULTAS AVANZADAS
SELECT Clientes.Nombre, Clientes.Apellido, SUM(Transacciones.Monto) AS Total_Transacciones
FROM Clientes
JOIN Cuentas ON Clientes.ID_Cliente = Cuentas.ID_Cliente
JOIN Transacciones ON Cuentas.ID_Cuenta = Transacciones.ID_Cuenta_origen
GROUP BY Clientes.Nombre, Clientes.Apellido;
SELECT Tipo_de_cuenta, SUM(Saldo) AS Balance_Total
FROM Cuentas
GROUP BY Tipo_de_cuenta;
SELECT Clientes.Nombre, Clientes.Apellido, Transacciones.Fecha, Transacciones.Monto, Transacciones.Tipo_de_transacción
FROM Clientes
JOIN Cuentas ON Clientes.ID_Cliente = Cuentas.ID_Cliente
JOIN Transacciones ON Cuentas.ID_Cuenta = Transacciones.ID_Cuenta_origen
ORDER BY Transacciones.Fecha DESC;
