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

CREATE TABLE `elidek`.`researcher` (
  `id` int(11) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `sex` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `name` varchar(45) NOT NULL DEFAULT 'fk from org',
  `works_since` date NOT NULL,
  PRIMARY KEY (`id`)
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `elidek`.`worksfor` (
  `title` VARCHAR(45) NOT NULL,
  `id` INT NULL,
  PRIMARY KEY (`title`));
  
  CREATE TABLE `elidek`.`manage` (
  `title` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`title`));

CREATE TABLE `elidek`.`deliverable` (
  `title` VARCHAR(45) NOT NULL,
  `summary` VARCHAR(45) NULL,
  `title` VARCHAR(45) NULL,
  `due_date` DATE NULL,
  PRIMARY KEY (`title`));

CREATE TABLE `elidek`.`fieldthatdescribes` (
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NULL,
  PRIMARY KEY (`name`));


