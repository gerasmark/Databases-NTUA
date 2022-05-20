-- baseis.organization definition
CREATE SCHEMA `elidek` ;

CREATE TABLE `elidek`.`project` (
  `title` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL,
  `summary` varchar(45) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `duration` year(4) NOT NULL,
  `name` varchar(45) NOT NULL ,
  `evaluated_from` int(11) NOT NULL ,
  `grade` int(11) NOT NULL,
  `date_of_eval` date NOT NULL,
  PRIMARY KEY (`title`),
  FOREIGN KEY(`name`) REFERENCES `program`(`name`),
  FOREIGN KEY(`evaluated_from`) REFERENCES `researcher`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- baseis.researcher definition

CREATE TABLE `elidek`.`researcher` (
  `id` int(11) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `sex` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `name` varchar(45) NOT NULL,
  `works_since` date NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `elidek`.`worksfor` (
  `title` VARCHAR(45) NOT NULL,
  `id` INT NULL,
  PRIMARY KEY (`title`),
  FOREIGN KEY (`title`) REFERENCES `project`(`title`),
  FOREIGN KEY (`id`) REFERENCES `researcher`(`id`)
  );
  
  CREATE TABLE `elidek`.`manage` (
  `title` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`title`),
  FOREIGN KEY(`name`) REFERENCES `executive`(`name`),
  FOREIGN KEY(`title`) REFERENCES `project`(`title`)
  );

CREATE TABLE `elidek`.`deliverable` (
  `title` VARCHAR(45) NOT NULL,
  `summary` VARCHAR(45) NULL,
  `title` VARCHAR(45) NULL,
  `due_date` DATE NULL,
  PRIMARY KEY (`title`));

CREATE TABLE `elidek`.`fieldthatdescribes` (
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NULL,
  FOREIGN KEY(`name`) REFERENCES `scientific field`(`name`),
  FOREIGN KEY(`title`) REFERENCES `project`(`title`),
  PRIMARY KEY (`name`));
  
  CREATE TABLE `elidek`.`research_center` (
  `name` varchar(45) NOT NULL,
  `budget_from_edu` int(11) NOT NULL,
  `budget_from_priv` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `elidek`.`university` (
  `name` varchar(45) NOT NULL,
  `budget_from_edu` int(11) NOT NULL,
  PRIMARY KEY (`name`),  
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `elidek`.`company` (
  `name` varchar(45) NOT NULL,
  `equity` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
) ;
ody