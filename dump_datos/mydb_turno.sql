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
-- Table structure for table `turno`
--

DROP TABLE IF EXISTS `turno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turno` (
  `idTurno` int NOT NULL AUTO_INCREMENT,
  `estado` enum('pendiente','aceptado','cancelado') NOT NULL,
  `fecha` date DEFAULT NULL,
  `f_hora` datetime NOT NULL,
  `Profesionales_idProfesionales` int NOT NULL,
  `Pacientes_dni` int NOT NULL,
  `Especialidad_idEspecialidad` int NOT NULL,
  PRIMARY KEY (`idTurno`,`Profesionales_idProfesionales`,`Pacientes_dni`,`Especialidad_idEspecialidad`),
  KEY `fk_Turno_Profesionales1_idx` (`Profesionales_idProfesionales`),
  KEY `fk_Turno_Pacientes1_idx` (`Pacientes_dni`),
  KEY `fk_Turno_Especialidad1_idx` (`Especialidad_idEspecialidad`),
  CONSTRAINT `fk_Turno_Especialidad1` FOREIGN KEY (`Especialidad_idEspecialidad`) REFERENCES `especialidad` (`idEspecialidad`),
  CONSTRAINT `fk_Turno_Pacientes1` FOREIGN KEY (`Pacientes_dni`) REFERENCES `pacientes` (`dni`),
  CONSTRAINT `fk_Turno_Profesionales1` FOREIGN KEY (`Profesionales_idProfesionales`) REFERENCES `profesionales` (`idProfesionales`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turno`
--

LOCK TABLES `turno` WRITE;
/*!40000 ALTER TABLE `turno` DISABLE KEYS */;
INSERT INTO `turno` VALUES (2,'pendiente',NULL,'2024-06-14 10:00:00',1,40598321,4),(3,'pendiente',NULL,'2024-06-14 12:00:00',1,42518752,4),(4,'pendiente',NULL,'2024-06-18 06:30:00',1,36547982,3),(5,'pendiente',NULL,'2024-06-17 08:30:00',4,46507945,3);
/*!40000 ALTER TABLE `turno` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-13 20:46:09
