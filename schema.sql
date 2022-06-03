-- baseis.organization definition
CREATE SCHEMA `elide` ;

DROP TABLE IF EXISTS `elide`.`program`;

CREATE TABLE `elide`.`program` (
  `name` VARCHAR(45) NOT NULL,
  `address` VARCHAR(60) NULL,
  PRIMARY KEY (`name`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
DROP TABLE IF EXISTS `elide`.`organization`;

CREATE TABLE `elide`.`organization` (
  `name` varchar(45) NOT NULL,
  `initials` varchar(45) NOT NULL,
  `postal_code` int(11) NOT NULL,
  `street` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `elide`.`researcher`;

CREATE TABLE `elide`.`researcher` (
  `id` int(11) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `sex` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `name` varchar(45) NOT NULL,
  `works_since` date NOT NULL,
  `age` smallint as (TIMESTAMPDIFF(YEAR, birthdate, '2022-06-06')),
  PRIMARY KEY (`id`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `elide`.`project`;

CREATE TABLE `elide`.`project` (
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
  FOREIGN KEY(`name`) REFERENCES `program`(`name`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY(`from_org`) REFERENCES `organization`(`name`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY(`evaluated_from`) REFERENCES `researcher`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CHECK(duration>=1 AND duration<=4)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `elide`.`scientific_field`;

  CREATE TABLE `elide`.`scientific_field` (
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`name`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  DROP TABLE IF EXISTS `elide`.`worksfor`;
  
CREATE TABLE `elide`.`worksfor` (
  `title` VARCHAR(45) NOT NULL,
  `id` INT NULL,
  PRIMARY KEY (`title`),
  FOREIGN KEY (`title`) REFERENCES `project`(`title`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`id`) REFERENCES `researcher`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
 DROP TABLE IF EXISTS `elide`.`deliverable`;

CREATE TABLE `elide`.`deliverable` (
  `title` VARCHAR(45) NOT NULL,
  `summary` VARCHAR(45) NULL,
  `title_project` VARCHAR(45) NULL,
  `due_date` DATE NULL,
  FOREIGN KEY(`title_project`) REFERENCES `project`(`title`) ON DELETE RESTRICT ON UPDATE CASCADE,
  PRIMARY KEY (`title`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `elide`.`fieldthatdescribes`;

CREATE TABLE `elide`.`fieldthatdescribes` (
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NULL,
  FOREIGN KEY(`name`) REFERENCES `scientific_field`(`name`) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY(`title`) REFERENCES `project`(`title`) ON DELETE RESTRICT ON UPDATE CASCADE,
  PRIMARY KEY (`name`)
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
DROP TABLE IF EXISTS `elide`.`research_center`;

  CREATE TABLE `elide`.`research_center` (
  `name` varchar(45) NOT NULL,
  `budget_from_edu` int(11) NOT NULL,
  `budget_from_priv` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `elide`.`university`;

CREATE TABLE `elide`.`university` (
  `name` varchar(45) NOT NULL,
  `budget_from_edu` int(11) NOT NULL,
  PRIMARY KEY (`name`),  
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `elide`.`company`;

CREATE TABLE `elide`.`company` (
  `name` varchar(45) NOT NULL,
  `equity` int(11) NOT NULL,
  PRIMARY KEY (`name`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) ON DELETE RESTRICT ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `elide`.`phone`;

CREATE TABLE `elide`.`phone` (
  `name` VARCHAR(45) NOT NULL,
  `phone` INT NOT NULL,
  PRIMARY KEY (`name`, `phone`),
  FOREIGN KEY(`name`) REFERENCES `organization`(`name`) ON DELETE RESTRICT ON UPDATE CASCADE
  )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
