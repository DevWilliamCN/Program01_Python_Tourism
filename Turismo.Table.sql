CREATE DATABASE turismo;
USE turismo;
CREATE TABLE Turistas(
numeroTurista int primary key not null, 
nombreTurista  varchar(20),
paisTurista varchar(15)
);

CREATE TABLE destinos(
numeroDestino int primary key not null, 
nombreSitio	varchar(20),
tipoDestino	varchar(20),
continente varchar(20)
);

CREATE TABLE viajes (
    numeroViaje VARCHAR(10) PRIMARY KEY NOT NULL,
    numeroTurista INT,
    numeroDestino INT,
    fechaSalida DATE,
    fechaLlegada DATE,
    ciudadSalida VARCHAR(25),
    FOREIGN KEY (numeroTurista)
        REFERENCES Turistas (numeroTurista),
    FOREIGN KEY (numeroDestino)
        REFERENCES destinos (numeroDestino)
);