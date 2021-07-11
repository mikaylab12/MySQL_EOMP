-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: Lifechoices_Online
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Admin`
--

DROP TABLE IF EXISTS `Admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Admin` (
  `admin_id` varchar(13) NOT NULL,
  `admin_name` varchar(20) NOT NULL,
  `admin_surname` varchar(20) NOT NULL,
  `admin_contact` varchar(10) NOT NULL,
  `admin_sign_in_date` date NOT NULL,
  `admin_sign_in_time` time NOT NULL,
  `admin_password` varchar(20) NOT NULL,
  `admin_sign_out_date` date DEFAULT NULL,
  `admin_sign_out_time` time DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
INSERT INTO `Admin` VALUES ('0011120149080','Mikayla','Beelders','0826889551','2021-07-11','11:36:18','12345',NULL,NULL),('0912295368084','Zavier','Dorland','0213654789','2021-07-09','14:39:12','100',NULL,NULL),('7706230091089','Liesl','Beelders','0829906427','2021-07-11','11:40:20','777','2021-07-11','11:41:05');
/*!40000 ALTER TABLE `Admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Next_Of_Kin`
--

DROP TABLE IF EXISTS `Next_Of_Kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Next_Of_Kin` (
  `admin_id` varchar(13) DEFAULT NULL,
  `stud_id` varchar(13) DEFAULT NULL,
  `visitor_id` varchar(13) DEFAULT NULL,
  `next_of_kin_name` varchar(20) NOT NULL,
  `next_of_kin_surname` varchar(20) NOT NULL,
  `next_of_kin_contact` varchar(10) NOT NULL,
  KEY `admin_id` (`admin_id`),
  KEY `stud_id` (`stud_id`),
  KEY `visitor_id` (`visitor_id`),
  CONSTRAINT `Next_Of_Kin_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `Admin` (`admin_id`),
  CONSTRAINT `Next_Of_Kin_ibfk_2` FOREIGN KEY (`stud_id`) REFERENCES `Students` (`stud_id`),
  CONSTRAINT `Next_Of_Kin_ibfk_3` FOREIGN KEY (`visitor_id`) REFERENCES `Visitors` (`visitor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Next_Of_Kin`
--

LOCK TABLES `Next_Of_Kin` WRITE;
/*!40000 ALTER TABLE `Next_Of_Kin` DISABLE KEYS */;
INSERT INTO `Next_Of_Kin` VALUES (NULL,'9903105047084',NULL,'Denise','Andries','0842369557'),(NULL,'9610055082082',NULL,'Jason','Calvert','0670202665'),('0912295368084',NULL,NULL,'Tania','Gavrilov','0835585725'),(NULL,NULL,'4410150121082','Liesl','Beelders','0829906427'),('7706230091089',NULL,NULL,'Mikayla ','Beelders','0826889551'),('0011120149080',NULL,NULL,'Ashley','Beelders','0829908173');
/*!40000 ALTER TABLE `Next_Of_Kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Students` (
  `stud_id` varchar(13) NOT NULL,
  `stud_name` varchar(20) NOT NULL,
  `stud_surname` varchar(20) NOT NULL,
  `stud_contact` varchar(10) NOT NULL,
  `stud_sign_in_date` date NOT NULL,
  `stud_sign_in_time` time NOT NULL,
  `stud_password` varchar(20) NOT NULL,
  `stud_sign_out_date` date DEFAULT NULL,
  `stud_sign_out_time` time DEFAULT NULL,
  PRIMARY KEY (`stud_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES ('9610055082082','Justin','Calvert','0679150663','2021-07-11','11:43:05','two','2021-07-11','11:44:02'),('9903105047084','Tashwill','Andries','0721918667','2021-07-11','10:37:53','54321','2021-07-11','10:40:45');
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Visitors`
--

DROP TABLE IF EXISTS `Visitors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Visitors` (
  `visitor_id` varchar(13) NOT NULL,
  `visitor_name` varchar(20) NOT NULL,
  `visitor_surname` varchar(20) NOT NULL,
  `visitor_contact` varchar(10) NOT NULL,
  `visitor_sign_in_date` date NOT NULL,
  `visitor_sign_in_time` time NOT NULL,
  `visitor_password` varchar(20) NOT NULL,
  `visitor_sign_out_date` date DEFAULT NULL,
  `visitor_sign_out_time` time DEFAULT NULL,
  PRIMARY KEY (`visitor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Visitors`
--

LOCK TABLES `Visitors` WRITE;
/*!40000 ALTER TABLE `Visitors` DISABLE KEYS */;
INSERT INTO `Visitors` VALUES ('0011120149080','Mikayla','Beelders','0826889551','2021-07-11','03:56:26','12345',NULL,NULL),('4410150121082','Maria','Johan','0217156873','2021-07-11','03:53:35','maria','2021-07-11','03:54:46');
/*!40000 ALTER TABLE `Visitors` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 11:47:35
