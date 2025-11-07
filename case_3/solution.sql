-- SQL-скрипт для создания схемы и таблиц для БД (Туризм). Используется PostgreSQL.

-- Создаём схему (БД для туризма)
CREATE SCHEMA IF NOT EXISTS tourism;
SET search_path TO tourism;

-- СПРАВОЧНИКИ (4 таблицы) 

-- 1) Направления (страна/город)
CREATE TABLE destinations (
    destination_id BIGSERIAL PRIMARY KEY,
    country        VARCHAR(100) NOT NULL,
    city           VARCHAR(100) NOT NULL,
    description    TEXT,
    CONSTRAINT uq_destinations_country_city UNIQUE (country, city)
);

-- 2) Типы туров (перечень услуг)
CREATE TABLE tourtypes (
    tourtype_id   BIGSERIAL PRIMARY KEY,
    typename      VARCHAR(100) NOT NULL UNIQUE,
    description   TEXT,
    duration_days INTEGER,
    base_price    NUMERIC(12,2) NOT NULL
);

-- 3) Отели
CREATE TABLE hotels (
    hotel_id        BIGSERIAL PRIMARY KEY,
    destination_id  BIGINT NOT NULL,
    hotel_name      VARCHAR(200) NOT NULL,
    star_rating     SMALLINT NOT NULL,    -- допустимые значения: 1..5
    address         VARCHAR(300),
    phone           VARCHAR(30),
    email           VARCHAR(100),
    price_per_night NUMERIC(12,2) NOT NULL,
    CONSTRAINT fk_hotels_destination
        FOREIGN KEY (destination_id) REFERENCES destinations(destination_id),
    CONSTRAINT uq_hotels_name_per_destination
        UNIQUE (destination_id, hotel_name)
);

-- 4) Клиенты
CREATE TABLE clients (
    client_id         BIGSERIAL PRIMARY KEY,
    first_name        VARCHAR(100) NOT NULL,
    last_name         VARCHAR(100) NOT NULL,
    passport_number   VARCHAR(20)  NOT NULL UNIQUE,
    birth_date        DATE,
    phone             VARCHAR(30)  NOT NULL,
    email             VARCHAR(100),
    address           TEXT,
    registration_date TIMESTAMP NOT NULL DEFAULT now()
);

-- ТАБЛИЦА ФАКТОВ, содержащая внешние ключи на справочники (1 таблица).
-- Таблица предназначена для объединения с таблицами-справочниками по внешним ключам 
-- с целью добавления аналитических разрезов (измерений).

-- Бронирования/заказы туров
CREATE TABLE tourbookings (
    booking_id        BIGSERIAL PRIMARY KEY,
    client_id         BIGINT NOT NULL,
    tourtype_id       BIGINT NOT NULL,
    destination_id    BIGINT NOT NULL,
    hotel_id          BIGINT NOT NULL,
    booking_date      TIMESTAMP NOT NULL DEFAULT now(),
    departure_date    DATE NOT NULL,
    return_date       DATE NOT NULL,
    number_of_persons SMALLINT NOT NULL DEFAULT 1,
    total_price       NUMERIC(14,2) NOT NULL,
    payment_status    VARCHAR(20) NOT NULL,   -- например: 'pending' | 'paid' | 'cancelled'
    booking_status    VARCHAR(20) NOT NULL,   -- например: 'pending' | 'confirmed' | 'cancelled'
    special_requests  TEXT,

    CONSTRAINT fk_tb_client
        FOREIGN KEY (client_id)      REFERENCES clients(client_id),
    CONSTRAINT fk_tb_tourtype
        FOREIGN KEY (tourtype_id)    REFERENCES tourtypes(tourtype_id),
    CONSTRAINT fk_tb_destination
        FOREIGN KEY (destination_id) REFERENCES destinations(destination_id),
    CONSTRAINT fk_tb_hotel
        FOREIGN KEY (hotel_id)       REFERENCES hotels(hotel_id)
);

-- Индексы по полям, наиболее часто используемым в соединениях (JOIN) и фильтрации по секции WHERE.
CREATE INDEX ix_tb_dates    ON tourbookings (departure_date, return_date);
CREATE INDEX ix_tb_client   ON tourbookings (client_id);
CREATE INDEX ix_tb_statuses ON tourbookings (booking_status, payment_status);
