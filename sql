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
-- baseis.researcher definition

CREATE TABLE `researcher` (
  `id` int(11) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `sex` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `name` varchar(45) NOT NULL DEFAULT 'fk from org',
  `works_since` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
