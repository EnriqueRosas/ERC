DELIMITER //

CREATE TRIGGER BeforeInsertReserva
BEFORE INSERT ON rentaautos.reservas
FOR EACH ROW
BEGIN
    DECLARE total_reservas INT;

    -- Verificar el número de reservas existentes para el cliente
    SELECT COUNT(*)
    INTO total_reservas
    FROM rentaautos.reservas
    WHERE id_cliente = NEW.id_cliente;

    -- Si el cliente ya tiene una reserva, devolver un error
    IF total_reservas >= 1 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'El cliente ya tiene una reserva activa y no puede realizar otra.';
    END IF;
END //

DELIMITER ;


INSERT INTO rentaautos.reservas(id_cliente, id_auto, fechaInicio, fechaFin, fechaDevolucion, anticipo, total)
VALUES (1, 2, '2023-01-10', '2023-01-20', '2023-01-21', 100.0, 0.0);



select * 
from reservas;
