-- baseis.organization definition
CREATE SCHEMA `elidek` ;

CREATE TABLE `elidek`.`executive` (
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`name`));
  CREATE TABLE `elidek`.`scientific field` (
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`name`));
  
CREATE TABLE `elidek`.`program` (
  `name` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(45) NULL,
  PRIMARY KEY (`name`));
  
CREATE TABLE `elidek`.`organization` (
  `name` varchar(45) NOT NULL,
  `initials` varchar(45) NOT NULL,
  `postal_code` int(11) NOT NULL,
  `street` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `phone` int(11) NOT NULL,
  `organizationcol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
