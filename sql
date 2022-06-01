-- baseis.organization definition
CREATE SCHEMA `josephine` ;

DROP TABLE IF EXISTS `program`;

CREATE TABLE `josephine`.`program` (
  `name` VARCHAR(45) NOT NULL,
  `adress` VARCHAR(45) NULL,
  PRIMARY KEY (`name`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
DROP TABLE IF EXISTS `organization`;

CREATE TABLE `josephine`.`organization` (
  `name` varchar(45) NOT NULL,
  `initials` varchar(45) NOT NULL,
  `postal_code` int(11) NOT NULL,
  `street` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `researcher`;

CREATE TABLE `josephine`.`researcher` (
  `id` int(11) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `sex` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `name` varchar(45) NOT NULL,
  `works_since` date NOT NULL,
  `age` smallint as (TIMESTAMPDIFF(YEAR, birthdate, '2022-06-06')),
  PRIMARY KEY (`id`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `project`;

CREATE TABLE `josephine`.`project` (
  `title` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL,
  `summary` varchar(45) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `duration` smallint as (TIMESTAMPDIFF(YEAR, start_date, end_date)),
  `name` varchar(45) NOT NULL,
  `evaluated_from` int(11) NOT NULL ,
  `from_org` varchar(45) NOT NULL,
  `grade` int(11) NOT NULL,
  `date_of_eval` date NOT NULL,
  `exec` varchar(45) NOT NULL,
  PRIMARY KEY (`title`),
  FOREIGN KEY(`name`) REFERENCES `program`(`name`),
  FOREIGN KEY(`from_org`) REFERENCES `organization`(`name`),
  FOREIGN KEY(`evaluated_from`) REFERENCES `researcher`(`id`),
  CHECK(duration>=1 AND duration<=4)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `scientific_field`;

  CREATE TABLE `josephine`.`scientific_field` (
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`name`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  DROP TABLE IF EXISTS `worksfor`;
  
CREATE TABLE `josephine`.`worksfor` (
  `title` VARCHAR(45) NOT NULL,
  `id` INT NULL,
  PRIMARY KEY (`title`),
  FOREIGN KEY (`title`) REFERENCES `project`(`title`),
  FOREIGN KEY (`id`) REFERENCES `researcher`(`id`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
 DROP TABLE IF EXISTS `deliverable`;

CREATE TABLE `josephine`.`deliverable` (
  `title` VARCHAR(45) NOT NULL,
  `summary` VARCHAR(45) NULL,
  `title_project` VARCHAR(45) NULL,
  `due_date` DATE NULL,
  FOREIGN KEY(`title_project`) REFERENCES `project`(`title`),
  PRIMARY KEY (`title`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `fieldthatdescribes`;

CREATE TABLE `josephine`.`fieldthatdescribes` (
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NULL,
  FOREIGN KEY(`name`) REFERENCES `scientific field`(`name`),
  FOREIGN KEY(`title`) REFERENCES `project`(`title`),
  PRIMARY KEY (`name`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
DROP TABLE IF EXISTS `research_center`;

  CREATE TABLE `josephine`.`research_center` (
  `name` varchar(45) NOT NULL,
  `budget_from_edu` int(11) NOT NULL,
  `budget_from_priv` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `university`;

CREATE TABLE `josephine`.`university` (
  `name` varchar(45) NOT NULL,
  `budget_from_edu` int(11) NOT NULL,
  PRIMARY KEY (`name`),  
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `company`;

CREATE TABLE `josephine`.`company` (
  `name` varchar(45) NOT NULL,
  `equity` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) 
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `phone`;

CREATE TABLE `josephine`.`phone` (
  `name` VARCHAR(45) NOT NULL,
  `phone` INT NOT NULL,
  PRIMARY KEY (`name`, `phone`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
