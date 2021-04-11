-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: bot_info
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

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
-- Table structure for table `bot_metadata`
--

DROP TABLE IF EXISTS `bot_metadata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_metadata` (
  `bot_id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `owner_id` int NOT NULL COMMENT 'Owner of this bot',
  `bot_name` varchar(255) NOT NULL COMMENT 'name of the bot',
  `created_date` datetime NOT NULL COMMENT 'date of creation',
  `last_modified_date` datetime NOT NULL COMMENT 'latest date bot configuration changed',
  PRIMARY KEY (`bot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_metadata`
--

LOCK TABLES `bot_metadata` WRITE;
/*!40000 ALTER TABLE `bot_metadata` DISABLE KEYS */;
INSERT INTO `bot_metadata` VALUES (1,154,'upeld','1988-11-02 11:55:09','2011-04-20 23:49:48'),(2,291,'rfvfk','2020-03-16 14:40:09','1993-04-05 17:12:24'),(3,157,'snocj','1987-02-10 10:10:47','1987-10-31 15:19:49'),(4,651,'bhpud','1999-01-13 03:11:33','2003-07-06 22:10:15'),(5,863,'nsirx','2012-04-01 16:36:39','2015-01-03 02:36:54'),(6,584,'htgoj','1997-07-15 15:29:27','2016-10-26 10:35:31'),(7,255,'xixbm','1999-02-03 00:17:51','1975-09-15 19:55:38'),(8,820,'salrs','2013-05-17 22:02:01','2002-05-27 12:35:27'),(9,53,'qkdjm','1974-11-21 01:44:38','1995-09-06 04:53:24'),(10,820,'agovd','1982-06-22 20:57:56','1981-12-12 17:35:48'),(101,969,'knfyr','1990-01-30 01:49:45','2003-05-13 22:41:21'),(102,587,'xthrs','1985-05-25 09:58:42','1970-07-31 17:38:22'),(103,977,'lubeq','1974-11-09 08:17:52','1982-02-23 20:31:04'),(104,398,'borfp','1972-05-19 11:38:11','2002-04-17 17:20:41'),(105,1017,'eaulo','1985-07-22 09:03:00','2016-07-31 12:21:52'),(106,460,'xmpio','1990-11-11 18:56:50','2001-02-25 23:30:06'),(107,65,'nodbh','1988-10-01 19:48:02','2011-08-23 16:01:52'),(108,950,'tnuoo','2011-04-20 14:31:58','1973-06-13 13:15:34'),(109,324,'ddoxx','2020-02-13 19:53:04','1980-03-01 09:18:36'),(110,89,'xpkuo','1994-07-10 09:37:01','2012-06-28 03:53:57');
/*!40000 ALTER TABLE `bot_metadata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `ix_users_id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-05  0:08:08
