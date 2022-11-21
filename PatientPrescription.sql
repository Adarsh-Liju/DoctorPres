-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 20, 2022 at 06:40 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `DoctorPres`
--

-- --------------------------------------------------------

--
-- Table structure for table `PatientPres`
--

CREATE TABLE `PatientPres` (
  `Pat_ID` int(11) NOT NULL,
  `Pat_Name` text DEFAULT NULL,
  `Pat_Age` int(11) DEFAULT NULL,
  `Adult` int(11) NOT NULL,
  `Symptoms` text DEFAULT NULL,
  `Medicines` text DEFAULT NULL,
  `Prescription` text DEFAULT NULL,
  `Date_Joined` date NOT NULL,
  `Timestamp` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `PatientPres`
--

INSERT INTO `PatientPres` (`Pat_ID`, `Pat_Name`, `Pat_Age`, `Adult`, `Symptoms`, `Medicines`, `Prescription`, `Date_Joined`, `Timestamp`) VALUES
(1166, 'oafnoadufn', 12, 0, 'iubiubuibui', 'Augmentin, Augmentin, Augmentin', NULL, '2022-11-18', '2022-11-20'),
(1209, 'oafnoadufn', 12, 0, 'iubiubuibui', 'Augmentin ,Augmentin , Augmentin', NULL, '2022-11-18', '2022-11-20'),
(2580, 'Shenoy', 20, 1, '', 'Dolo ,Cremaffin, Aciloc', NULL, '2022-11-09', '2022-11-20'),
(3238, 'Navin Shrinivas', 120, 1, '', 'Dolo ,Avil ,Emty', NULL, '2022-11-17', '2022-11-20'),
(4160, 'adarsh Liju abraham', 19, 1, '', 'Augmentin ,Augmentin, Augmentin', NULL, '2022-10-26', '2022-11-20'),
(5623, 'yggk', 134, 1, '', 'Augmentin ,Augmentin ,Augmentin', NULL, '2022-11-09', '2022-11-20'),
(7014, 'adarsh', 190, 1, '', 'Augmentin , Augmentin ,Augmentin', NULL, '2022-10-26', '2022-11-20'),
(9182, 'adarsh Liju abraham', 19, 1, '', 'Augmentin , Augmentin , Augmentin ', NULL, '2022-10-26', '2022-11-20'),
(9425, 'adarsh Liju abraham', 19, 1, '', 'Augmentin, Augmentin ,Augmentin', NULL, '2022-10-26', '2022-11-20');

--
-- Triggers `PatientPres`
--
DELIMITER $$
CREATE TRIGGER `age_verify` BEFORE INSERT ON `PatientPres` FOR EACH ROW IF new.`Pat_Age` < 18 then set new.`Adult` = 'C';
ELSEIF new.`Pat_Age` > 18 then set new.`Adult` = 'A';
END IF
$$
DELIMITER ;


