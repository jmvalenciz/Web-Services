create table if not exists origen(
       id int primary key,
       dato varchar(20)
);

create table if not exists sensores(
       id int auto_increment primary key,
       nombre varchar(45) not null,
       variable varchar(20) not null,
       unidades varchar(20) not null,
);

create table if not exists tipo_sensores(
       id int primary key,
       fecha date not null,
       origen varchar(200) not null,
       valor float not null,
       codigoSensor int not null,
       observacion varchar(45),
       foreign key(codigoSensor) REFERENCES sensores(id),
       foreign key(origen) REFERENCES origen(id)
);
