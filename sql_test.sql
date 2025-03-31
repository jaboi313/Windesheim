CREATE DATABASE bestelinterface;

USE bestelinterface;

CREATE TABLE categorie (
    id INTEGER(10) PRIMARY KEY AUTO_INCREMENT,
    naam VARCHAR(255) NOT NULL
);

CREATE TABLE menu (
    id INTEGER(10) PRIMARY KEY AUTO_INCREMENT,
    naam VARCHAR(255) NOT NULL
);

CREATE TABLE product (
    id INTEGER(10) PRIMARY KEY AUTO_INCREMENT,D:\Computer\Progameren\VScode\Windesheim\Oefeningen\Windesheim\sql_test.sql
    categorie_id INTEGER(10),
    naam VARCHAR(255) NOT NULL,
    prijs DECIMAL(6,2) NOT NULL,
    kcal INTEGER(10),
    FOREIGN KEY (categorie_id) REFERENCES categorie(id) ON DELETE SET NULL
);

CREATE TABLE menu_producten (
    menu_id INTEGER(10),
    product_id INTEGER(10),
    aantal INTEGER(10) NOT NULL,
    PRIMARY KEY (menu_id, product_id),
    FOREIGN KEY (menu_id) REFERENCES menu(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
);

CREATE TABLE bestelling (
    id INTEGER(10) PRIMARY KEY AUTO_INCREMENT,
    datum_tijd DATETIME NOT NULL,
    tafelnummer INTEGER(10) NOT NULL
);

CREATE TABLE bestelling_items (
    bestelling_id INTEGER(10),
    product_id INTEGER(10),
    aantal INTEGER(10) NOT NULL,
    opmerking VARCHAR(255),
    PRIMARY KEY (bestelling_id, product_id),
    FOREIGN KEY (bestelling_id) REFERENCES bestelling(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE
);
