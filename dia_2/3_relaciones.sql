-- Seguiremos utilizando la bd de finanzas

-- Crear una tabla cuentas 
-- NOTA: NO CREAR LA TABLA

-- id autoincrementable primary key
-- numero_cuenta text not null unico,
-- tipo_moneda SOLES | DOLARES | EUROS no nulo
-- fecha_creacion timestamp valor actual del servidor no nulo
-- mantenimiento float puede ser nulo

CREATE TYPE tipo_moneda_enum AS ENUM ('SOLES', 'DOLARES', 'EUROS');

CREATE TABLE cuentas (
    id SERIAL NOT NULL PRIMARY KEY,
    numero_cuenta TEXT UNIQUE NOT NULL,
    tipo_moneda tipo_moneda_enum NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT NOW() NOT NULL,
    mantenimiento FLOAT,
    cliente_id INT NOT NULL,
    CONSTRAINT fk_clientes FOREIGN KEY(cliente_id) REFERENCES clientes(id)
);