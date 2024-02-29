-- Create the database
CREATE DATABASE mine;

-- Use the database
USE mine;

CREATE TABLE `measurement_detail` (
  `name_sensor` varchar(20) NOT NULL,
  `value` decimal(10,0) NOT NULL,
  `unit` varchar(20) NOT NULL,
  `timestamp` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `summary` (
  `average` decimal(10,0) NOT NULL,
  `name_sensor` varchar(20) NOT NULL,
  `timestamp` date NOT NULL,
  `unit` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
