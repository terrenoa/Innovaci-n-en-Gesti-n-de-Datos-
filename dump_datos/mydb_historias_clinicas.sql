-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `historias_clinicas`
--

DROP TABLE IF EXISTS `historias_clinicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historias_clinicas` (
  `idhistorias_clinicas` int NOT NULL,
  `Pacientes_dni` int NOT NULL,
  `Pacientes_ObraS_idObraS` int NOT NULL,
  `fecha_primera_atencion` date DEFAULT NULL,
  `altura` float DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `alergias` tinyint(1) NOT NULL,
  `medicacion_diaria` tinyint(1) NOT NULL,
  `hipertenso` tinyint(1) DEFAULT NULL,
  `fue_operado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idhistorias_clinicas`,`Pacientes_dni`,`Pacientes_ObraS_idObraS`),
  KEY `fk_historias_clinicas_Pacientes1_idx` (`Pacientes_dni`,`Pacientes_ObraS_idObraS`),
  CONSTRAINT `fk_historias_clinicas_Pacientes1` FOREIGN KEY (`Pacientes_dni`, `Pacientes_ObraS_idObraS`) REFERENCES `pacientes` (`dni`, `ObraS_idObraS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historias_clinicas`
--

LOCK TABLES `historias_clinicas` WRITE;
/*!40000 ALTER TABLE `historias_clinicas` DISABLE KEYS */;
/*!40000 ALTER TABLE `historias_clinicas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-13 20:46:08
