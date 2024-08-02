--vistas
--procedimientos almacenados
--triggers
--funciones
go
use SistemaFinanciero

CREATE VIEW DetallesClientesCuentas AS
SELECT 
    c.ID_Cliente,
    c.Nombre,
    c.Apellido,
    ct.N�mero_de_cuenta,
    ct.Tipo_de_cuenta,
    ct.Saldo
FROM 
    Clientes c
JOIN 
    Cuentas ct ON c.ID_Cliente = ct.ID_Cliente;
	go



	CREATE VIEW DetallesClientesCuentasTarjetas AS
SELECT 
    c.ID_Cliente,
    c.Nombre,
    c.Apellido,
    cu.N�mero_de_cuenta,
    cu.Tipo_de_cuenta,
    cu.Saldo,
    t.N�mero_de_tarjeta,
    t.Tipo_de_tarjeta,
    t.Fecha_de_expiraci�n,
    t.L�mite_de_cr�dito
FROM 
    Clientes c
LEFT JOIN 
    Cuentas cu ON c.ID_Cliente = cu.ID_Cliente
LEFT JOIN 
    Tarjetas t ON c.ID_Cliente = t.ID_Cliente;



	CREATE VIEW DetallesClientesConPrestamos AS
SELECT 
    c.ID_Cliente,
    c.Nombre AS NombreCliente,
    c.Apellido AS ApellidoCliente,
    cu.N�mero_de_cuenta,
    cu.Tipo_de_cuenta,
    cu.Saldo,
    p.ID_Pr�stamo,
    p.Monto AS MontoPrestamo,
    p.Tasa_de_inter�s,
    p.Plazo,
    p.Fecha_de_inicio
FROM 
    Clientes c
LEFT JOIN 
    Cuentas cu ON c.ID_Cliente = cu.ID_Cliente
LEFT JOIN 
    Pr�stamos p ON c.ID_Cliente = p.ID_Cliente




	select * from DetallesClientesConPrestamos
	SELECT * FROM DetallesClientesCuentasTarjetas
	select * from DetallesClientesCuentas



--Procedimiento1
CREATE PROCEDURE ObtenerClientesPorTipo
    @Tipo_de_Cliente NVARCHAR(20)
AS
BEGIN
    SELECT 
        ID_Cliente,
        Nombre,
        Apellido,
        Direccion,
        Telefono,
        Email,
        Fecha_de_Nacimiento
    FROM 
        Clientes
    WHERE 
        Tipo_de_Cliente = @Tipo_de_Cliente;
END;
EXEC [dbo].[ObtenerClientesPorTipo]
   @Tipo_de_Cliente = 'corporativo';


--Procedimientos2
   CREATE PROCEDURE ObtenerSaldoTotalCliente
    @ID_Cliente INT
AS
BEGIN
    -- Seleccionar el saldo total de todas las cuentas del cliente
    SELECT 
        c.ID_Cliente,
        c.Nombre,
        c.Apellido,
        SUM(cu.Saldo) AS Saldo_Total
    FROM 
        Clientes c
    INNER JOIN 
        Cuentas cu ON c.ID_Cliente = cu.ID_Cliente
    WHERE 
        c.ID_Cliente = @ID_Cliente
    GROUP BY 
        c.ID_Cliente, c.Nombre, c.Apellido;
END;
EXEC [dbo].[ObtenerSaldoTotalCliente]
    @ID_Cliente = 20; 




--funcion

CREATE FUNCTION ObtenerNumeroTransacciones (@ID_Cuenta INT)
RETURNS INT
AS
BEGIN
    DECLARE @NumeroTransacciones INT;
    
    SELECT @NumeroTransacciones = COUNT(*)
    FROM Transacciones
    WHERE ID_Cuenta_origen = @ID_Cuenta
       OR ID_Cuenta_destino = @ID_Cuenta;
    
    RETURN @NumeroTransacciones;
END;
SELECT 
    N�mero_de_cuenta,
    dbo.ObtenerNumeroTransacciones(ID_Cuenta) AS NumeroTransacciones
FROM 
    Cuentas
WHERE 
    ID_Cuenta = 20;  --cambia_id_bro


	CREATE FUNCTION ObtenerMontoTotalPrestamos (@ID_Cliente INT)
RETURNS DECIMAL(18, 2)
AS
BEGIN
    DECLARE @MontoTotal DECIMAL(18, 2);
    
    SELECT @MontoTotal = ISNULL(SUM(Monto), 0)
    FROM Pr�stamos
    WHERE ID_Cliente = @ID_Cliente;
    
    RETURN @MontoTotal;
END;
SELECT 
    Nombre,
    Apellido,
    dbo.ObtenerMontoTotalPrestamos(ID_Cliente) AS MontoTotalPrestamos
FROM 
    Clientes
WHERE 
    ID_Cliente = 10;  --idcambiar


	--triggers




	-- Crear trigger despu�s de una inserci�n en la tabla Transacciones
CREATE TRIGGER trg_AfterInsertTransacciones
ON Transacciones
AFTER INSERT
AS
BEGIN
    DECLARE @ID_Cuenta_origen INT;
    DECLARE @ID_Cuenta_destino INT;
    DECLARE @Monto DECIMAL(18, 2);
    DECLARE @Tipo_de_transacci�n NVARCHAR(20);
    
    -- Obtener los valores insertados
    SELECT 
        @ID_Cuenta_origen = inserted.ID_Cuenta_origen,
        @ID_Cuenta_destino = inserted.ID_Cuenta_destino,
        @Monto = inserted.Monto,
        @Tipo_de_transacci�n = inserted.Tipo_de_transacci�n
    FROM inserted;
    
    -- Verificar si la transacci�n es una transferencia
    IF @Tipo_de_transacci�n = 'transferencia'
    BEGIN
        -- Actualizar el saldo de la cuenta origen
        UPDATE Cuentas
        SET Saldo = Saldo - @Monto
        WHERE ID_Cuenta = @ID_Cuenta_origen;
        
        -- Actualizar el saldo de la cuenta destino
        UPDATE Cuentas
        SET Saldo = Saldo + @Monto
        WHERE ID_Cuenta = @ID_Cuenta_destino;
    END
END;
SELECT 
    name AS TriggerName,
    object_name(parent_id) AS TableName,
    type_desc AS TriggerType
FROM 
    sys.triggers;


