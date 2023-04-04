-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: iHelper_dev_db
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

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
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES ('421a55f1-7d82-45d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Adama'),('421a55f1-7d82-45d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','bahirdar'),('421a55f1-7d82-45d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','mekelle'),('421a55f1-7d82-45d9-b54c-a76916479548','2017-03-25 19:42:40','2017-03-25 19:42:40','hawassa'),('ea059e6d-2284-432e-9dcd-7dda0fc7c230','2023-03-18 02:19:08','2023-03-18 02:19:08','Addis Ababa');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `request_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `request_id` (`request_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`request_id`) REFERENCES `requests` (`id`),
  CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `place`
--

DROP TABLE IF EXISTS `place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `place` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  `city_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `city_id` (`city_id`),
  CONSTRAINT `place_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `place`
--

LOCK TABLES `place` WRITE;
/*!40000 ALTER TABLE `place` DISABLE KEYS */;
INSERT INTO `place` VALUES ('25a9add2-dd7f-412c-a90f-af0871de07cb','2023-03-18 15:31:14','2023-03-18 15:31:14','total','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('284934d2-dd7f-412c-a30f-a318796e0033','2023-03-23 10:00:00','2023-03-23 11:30:00','gulele','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('284934d2-dd7f-612c-a30f-a318796e0033','2023-03-23 10:00:00','2023-03-23 11:30:00','yeka','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('284934d2-dd7f-612c-a30f-a318796e0933','2023-03-23 10:00:00','2023-03-23 11:30:00','kirkos','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('28493dd2-dd7f-412c-a30f-a318796e0033','2023-03-23 10:00:00','2023-03-23 11:30:00','arada','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('28a93dd2-dd7f-412c-a30f-a318796e0033','2023-03-23 10:00:00','2023-03-23 11:30:00','lemi kura','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('28a9add2-dd7f-412c-a30f-a308796e0033','2023-03-23 10:00:00','2023-03-23 11:30:00','bole','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('28a9add2-dd7f-412c-a30f-a308796e0333','2023-03-23 10:00:00','2023-03-23 11:30:00','lideta','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('28a9add2-dd7f-412c-a30f-a318796e0033','2023-03-23 10:00:00','2023-03-23 11:30:00','nifassilk lafto','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('28a9add2-dd7f-412c-a90f-a308796e0333','2023-03-23 10:00:00','2023-03-23 11:30:00','akaki kaliti','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('28a9add2-dd7f-412c-a90f-a308798e0333','2023-03-23 10:00:00','2023-03-23 11:30:00','kolfe keraniyo','ea059e6d-2284-432e-9dcd-7dda0fc7c230'),('421a55f1-7d82-4599-b54c-a6651942547','2017-03-25 19:42:40','2017-03-25 19:42:40','bahirdar merkato','421a55f1-7d82-45d9-b54c-a76916479546'),('421a55f1-7d82-4599-b54c-a66519439547','2017-03-25 19:42:40','2017-03-25 19:42:40','bahirdar apiyasa','421a55f1-7d82-45d9-b54c-a76916479546'),('421a55f1-7d82-45d9-b54c-a66516439547','2017-03-25 19:42:40','2017-03-25 19:42:40','haik','421a55f1-7d82-45d9-b54c-a76916479548'),('421a55f1-7d82-45d9-b54c-a66516479547','2017-03-25 19:42:40','2017-03-25 19:42:40','postabet','421a55f1-7d82-45d9-b54c-a76916479545'),('421a55f1-7d82-45d9-b54c-a66519439547','2017-03-25 19:42:40','2017-03-25 19:42:40','hawasapiyasa','421a55f1-7d82-45d9-b54c-a76916479548'),('421a55f1-7d82-45d9-b54c-a66916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','franco','421a55f1-7d82-45d9-b54c-a76916479545');
/*!40000 ALTER TABLE `place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `Request_status` varchar(20) NOT NULL,
  `service_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  KEY `service_id` (`service_id`),
  CONSTRAINT `requests_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `requests_ibfk_3` FOREIGN KEY (`service_id`) REFERENCES `service` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `service_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `text` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `service_id` (`service_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`service_id`) REFERENCES `service` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES ('7c1023ec-3d95-49d2-a534-6647e7097e23','2023-03-18 17:22:32','2023-03-18 17:22:32','46f20573-016f-4506-b220-c540ddb0e254','4f5ee2bd-f243-4a11-9afb-d58fb792cca3','goodsrevice'),('fbdd540a-8555-438d-b676-307bc044a893','2023-03-18 17:22:35','2023-03-18 17:22:35','46f20573-016f-4506-b220-c540ddb0e254','4f5ee2bd-f243-4a11-9afb-d58fb792cca3','goodsrevice');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `describtion` varchar(128) NOT NULL,
  `place_id` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `fk_place` (`place_id`),
  CONSTRAINT `fk_place` FOREIGN KEY (`place_id`) REFERENCES `place` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service`
--

LOCK TABLES `service` WRITE;
/*!40000 ALTER TABLE `service` DISABLE KEYS */;
INSERT INTO `service` VALUES ('25a9add2-dd7f-412c-a90f-a308798e0333','2023-03-23 10:00:00','2023-03-23 11:30:00','cleaning',75.00,'Deep cleaning the living room,kitchen and bathrooms','25a9add2-dd7f-412c-a90f-af0871de07cb'),('25a9add2-dd7f-412c-a90f-af0871de0333','2023-03-23 10:00:00','2023-03-23 11:30:00','gardening',75.00,'mowing lawn and trimming hedges','421a55f1-7d82-4599-b54c-a6651942547'),('25a9add2-dd7f-412c-a90f-af0871de0733','2023-03-23 10:00:00','2023-03-23 10:00:00','electrician',350.00,'electrical wiring','25a9add2-dd7f-412c-a90f-af0871de07cb'),('25a9add2-dd7f-412c-a90f-af08798e0333','2023-03-23 10:00:00','2023-03-23 11:30:00','babysitting/maid',75.00,'prepare meal and taking care of the kids','25a9add2-dd7f-412c-a90f-af0871de07cb'),('25a9add2-dd7f-412c-a90f-af0879de0333','2023-03-23 10:00:00','2023-03-23 11:30:00','security',75.00,'24/7 surveillance monitoring and security service for home and events','421a55f1-7d82-45d9-b54c-a66516479547'),('46f20573-016f-4506-b220-c540ddb0e254','2023-03-18 16:47:38','2023-03-18 16:47:38','plumbing',277.00,'water pipe mentenance','25a9add2-dd7f-412c-a90f-af0871de07cb');
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `phone_number` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('4f5ee2bd-f243-4a11-9afb-d58fb792cca3','2023-03-18 09:47:06','2023-03-18 09:47:06','tomasmandefro@gmail.com','1234','tomsa','mandefro','+251922477450'),('9e4cb400-7e35-4831-88ae-fdd05b8028e7','2023-03-18 09:45:31','2023-03-18 09:45:31','tomasmandefro@gmail.com','1234','tomsa','mandefro','+251922477450'),('c13f06a6-f614-4866-a1e9-b5bfbeab5cba','2023-03-18 12:16:17','2023-03-18 12:16:17','tomasmandefro@gmail.com','1234','tomsa','mandefro','+251922477450');
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

-- Dump completed on 2023-04-04  1:13:39
