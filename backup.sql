-- MySQL dump 10.13  Distrib 9.0.1, for Win64 (x86_64)
--
-- Host: localhost    Database: thuvien
-- ------------------------------------------------------
-- Server version	9.0.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'hien');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add manager',7,'add_manager'),(26,'Can change manager',7,'change_manager'),(27,'Can delete manager',7,'delete_manager'),(28,'Can view manager',7,'view_manager'),(29,'Can add library log',8,'add_librarylog'),(30,'Can change library log',8,'change_librarylog'),(31,'Can delete library log',8,'delete_librarylog'),(32,'Can view library log',8,'view_librarylog'),(33,'Can add book',9,'add_book'),(34,'Can change book',9,'change_book'),(35,'Can delete book',9,'delete_book'),(36,'Can view book',9,'view_book'),(37,'Can add book transaction',10,'add_booktransaction'),(38,'Can change book transaction',10,'change_booktransaction'),(39,'Can delete book transaction',10,'delete_booktransaction'),(40,'Can view book transaction',10,'view_booktransaction'),(41,'Can add student',11,'add_student'),(42,'Can change student',11,'change_student'),(43,'Can delete student',11,'delete_student'),(44,'Can view student',11,'view_student'),(45,'Can add application',12,'add_application'),(46,'Can change application',12,'change_application'),(47,'Can delete application',12,'delete_application'),(48,'Can view application',12,'view_application'),(49,'Can add access token',13,'add_accesstoken'),(50,'Can change access token',13,'change_accesstoken'),(51,'Can delete access token',13,'delete_accesstoken'),(52,'Can view access token',13,'view_accesstoken'),(53,'Can add grant',14,'add_grant'),(54,'Can change grant',14,'change_grant'),(55,'Can delete grant',14,'delete_grant'),(56,'Can view grant',14,'view_grant'),(57,'Can add refresh token',15,'add_refreshtoken'),(58,'Can change refresh token',15,'change_refreshtoken'),(59,'Can delete refresh token',15,'delete_refreshtoken'),(60,'Can view refresh token',15,'view_refreshtoken'),(61,'Can add id token',16,'add_idtoken'),(62,'Can change id token',16,'change_idtoken'),(63,'Can delete id token',16,'delete_idtoken'),(64,'Can view id token',16,'view_idtoken'),(65,'Can add token',17,'add_token'),(66,'Can change token',17,'change_token'),(67,'Can delete token',17,'delete_token'),(68,'Can view token',17,'view_token'),(69,'Can add category',18,'add_category'),(70,'Can change category',18,'change_category'),(71,'Can delete category',18,'delete_category'),(72,'Can view category',18,'view_category');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_home_manager_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_home_manager_id` FOREIGN KEY (`user_id`) REFERENCES `home_manager` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'home','book'),(10,'home','booktransaction'),(18,'home','category'),(8,'home','librarylog'),(7,'home','manager'),(11,'home','student'),(17,'home','token'),(13,'oauth2_provider','accesstoken'),(12,'oauth2_provider','application'),(14,'oauth2_provider','grant'),(16,'oauth2_provider','idtoken'),(15,'oauth2_provider','refreshtoken'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'home','0001_initial','2024-11-10 17:43:42.327763'),(2,'contenttypes','0001_initial','2024-11-10 17:43:42.335676'),(3,'contenttypes','0002_remove_content_type_name','2024-11-10 17:43:42.339651'),(4,'auth','0001_initial','2024-11-10 17:43:42.341651'),(5,'auth','0002_alter_permission_name_max_length','2024-11-10 17:43:42.343650'),(6,'auth','0003_alter_user_email_max_length','2024-11-10 17:43:42.345755'),(7,'auth','0004_alter_user_username_opts','2024-11-10 17:43:42.348751'),(8,'auth','0005_alter_user_last_login_null','2024-11-10 17:43:42.351759'),(9,'auth','0006_require_contenttypes_0002','2024-11-10 17:43:42.355298'),(10,'auth','0007_alter_validators_add_error_messages','2024-11-10 17:43:42.360759'),(11,'auth','0008_alter_user_username_max_length','2024-11-10 17:43:42.366347'),(12,'auth','0009_alter_user_last_name_max_length','2024-11-10 17:43:42.370053'),(13,'auth','0010_alter_group_name_max_length','2024-11-10 17:43:42.372130'),(14,'auth','0011_update_proxy_permissions','2024-11-10 17:43:42.373802'),(15,'auth','0012_alter_user_first_name_max_length','2024-11-10 17:43:42.376829'),(16,'home','0002_rename_book_id_booktransaction_book_and_more','2024-11-10 17:43:42.378285'),(17,'home','0003_alter_manager_options_alter_manager_managers_and_more','2024-11-10 17:43:42.380654'),(18,'home','0004_rename_book_booktransaction_book_and_more','2024-11-10 17:43:42.383716'),(19,'home','0005_token_alter_booktransaction_borrow_date_and_more','2024-11-10 17:43:42.385891'),(20,'home','0006_alter_booktransaction_borrow_date_and_more','2024-11-10 17:43:42.387890'),(21,'home','0007_alter_book_id','2024-11-10 17:43:42.389044'),(22,'home','0008_alter_token_token','2024-11-10 17:43:42.391101'),(23,'home','0009_alter_book_id_alter_student_id','2024-11-10 17:43:42.393122'),(24,'home','0010_alter_token_token','2024-11-10 17:43:42.394633'),(25,'home','0011_alter_book_quantity','2024-11-10 17:43:42.397646'),(26,'home','0012_alter_student_id','2024-11-10 17:43:42.400652'),(27,'home','0013_alter_booktransaction_student','2024-11-10 17:43:42.401980'),(28,'home','0014_alter_librarylog_student','2024-11-10 17:43:42.403987'),(29,'home','0015_rename_student_librarylog_student_id','2024-11-10 17:43:42.405009'),(30,'home','0016_rename_student_id_librarylog_student','2024-11-10 17:43:42.407268'),(31,'home','0017_book_cover_image','2024-11-10 17:43:42.408267'),(32,'admin','0001_initial','2024-11-10 17:44:32.708606'),(33,'admin','0002_logentry_remove_auto_add','2024-11-10 17:44:32.714583'),(34,'admin','0003_logentry_add_action_flag_choices','2024-11-10 17:44:32.719418'),(35,'oauth2_provider','0001_initial','2024-11-10 17:44:33.282081'),(36,'oauth2_provider','0002_auto_20190406_1805','2024-11-10 17:44:33.323342'),(37,'oauth2_provider','0003_auto_20201211_1314','2024-11-10 17:44:33.372910'),(38,'oauth2_provider','0004_auto_20200902_2022','2024-11-10 17:44:33.586711'),(39,'oauth2_provider','0005_auto_20211222_2352','2024-11-10 17:44:33.618988'),(40,'oauth2_provider','0006_alter_application_client_secret','2024-11-10 17:44:33.635932'),(41,'oauth2_provider','0007_application_post_logout_redirect_uris','2024-11-10 17:44:33.658964'),(42,'oauth2_provider','0008_alter_accesstoken_token','2024-11-10 17:44:33.668472'),(43,'oauth2_provider','0009_add_hash_client_secret','2024-11-10 17:44:33.701762'),(44,'oauth2_provider','0010_application_allowed_origins','2024-11-10 17:44:33.726965'),(45,'oauth2_provider','0011_refreshtoken_token_family','2024-11-10 17:44:33.747625'),(46,'oauth2_provider','0012_add_token_checksum','2024-11-10 17:44:33.888096'),(47,'sessions','0001_initial','2024-11-10 17:44:33.909054'),(48,'home','0018_alter_book_title','2024-11-17 16:55:30.613109'),(49,'home','0019_book_created_at_book_updated_at_and_more','2024-11-17 16:55:30.876377'),(50,'home','0020_category','2024-11-18 13:32:50.590238'),(51,'home','0021_category_created_at_category_updated_at','2024-11-18 13:37:09.249607'),(52,'home','0022_alter_category_created_at_alter_category_updated_at','2024-11-18 16:27:55.577617'),(53,'home','0023_alter_category_created_at_alter_category_updated_at','2024-11-18 16:41:56.698221'),(54,'home','0024_alter_book_created_at_alter_book_updated_at_and_more','2024-11-18 16:45:46.923162'),(55,'home','0025_remove_token_created_date','2024-11-18 16:47:06.321223'),(56,'home','0026_delete_token_alter_book_publish_date_and_more','2024-11-19 18:44:31.743030'),(57,'home','0027_alter_librarylog_checked_in','2024-11-19 18:52:58.558134'),(58,'home','0028_alter_librarylog_checked_in','2024-11-20 18:20:35.801608'),(59,'home','0029_alter_librarylog_checked_in','2024-11-20 18:21:53.749486'),(60,'home','0030_alter_booktransaction_id_alter_category_id_and_more','2024-11-20 18:29:51.558753'),(61,'home','0031_alter_librarylog_checked_in_alter_student_birthday','2024-11-20 18:33:07.720851'),(62,'home','0032_alter_librarylog_checked_in_alter_student_birthday_and_more','2024-11-21 13:27:22.262186'),(63,'home','0033_alter_librarylog_checked_in_alter_student_birthday','2024-11-21 16:13:47.344530'),(64,'home','0034_alter_student_birthday','2024-11-21 16:17:25.666728'),(65,'home','0035_alter_student_birthday','2024-11-21 16:20:13.103717');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8361fo9l0wwfdtrc55wsjlwjq0mbv4mz','.eJxVjMEOwiAQRP-FsyELLsF69O43EHZZpGpoUtpT479Lkx70MsnMm5lNhbguJaxN5jAmdVWoTr8ZRX5J3UF6xvqYNE91mUfSe0UftOn7lOR9O7p_ByW20tcejGVjDPmuCc-QPVhvc46XPHTjGQgdOjFAJN6ZzAwiA4pjRCvq8wXKmze7:1tCfsA:0tPTpWNlIPjw3uui_DQOsvAZmS8ftmjJdERxCz3VqHw','2024-12-01 14:03:30.343843');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_book`
--

DROP TABLE IF EXISTS `home_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_book` (
  `id` varchar(9) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `publish_date` bigint NOT NULL,
  `quantity` int NOT NULL,
  `cover_image` varchar(255) NOT NULL,
  `created_at` bigint NOT NULL,
  `updated_at` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_book_title_dd774e74_uniq` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_book`
--

LOCK TABLES `home_book` WRITE;
/*!40000 ALTER TABLE `home_book` DISABLE KEYS */;
INSERT INTO `home_book` VALUES ('book_123a','anh yêu em','tuấn','toán',1732045488,1,'1',20241118162944,1732217257),('book_3OZ1','hoa máu','hiến','ngôn tình',20031211,10,'2',20241117165952,20241117170431),('book_LVPY','hoa cỏ may','hiến','ngôn tình',1732043988,10,'3',20241118162944,1732043988),('book_TOND','Nihonggo','Hiến','TIeng Anh',1732134446,3,'',1732134446,1732134446),('book_XOEZ','tiếng anh','Hiến','TIeng Anh',1732134514,3,'',1732134514,1732134514),('book_YQX5','hoa cai','F. Scott Fitzgerald','Classic Literature',1732045488,9,'http://example.com/covers/great_gatsby.jpg',1732042410,1732045488);
/*!40000 ALTER TABLE `home_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_booktransaction`
--

DROP TABLE IF EXISTS `home_booktransaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_booktransaction` (
  `id` varchar(10) NOT NULL,
  `borrow_date` bigint NOT NULL,
  `days_registered` int unsigned NOT NULL,
  `return_date` bigint DEFAULT NULL,
  `book_id` varchar(9) NOT NULL,
  `student_id` varchar(128) NOT NULL,
  `created_at` bigint NOT NULL,
  `updated_at` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_booktransaction_book_id_0cd3eb21_fk` (`book_id`),
  KEY `home_booktransaction_student_id_dc94b5bb_fk` (`student_id`),
  CONSTRAINT `home_booktransaction_book_id_0cd3eb21_fk` FOREIGN KEY (`book_id`) REFERENCES `home_book` (`id`),
  CONSTRAINT `home_booktransaction_chk_1` CHECK ((`days_registered` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_booktransaction`
--

LOCK TABLES `home_booktransaction` WRITE;
/*!40000 ALTER TABLE `home_booktransaction` DISABLE KEYS */;
INSERT INTO `home_booktransaction` VALUES ('1',20241104,3,20241108,'5','1',20241117165531,20241117165531),('10',1732043975,4,NULL,'book_YQX5','B22DCCN112',1732043975,1732043975),('11',1732043988,10,NULL,'book_LVPY','B22DCCN112',1732043988,1732043988),('12',1732045488,5,1732217257,'book_123a','B22DCCN293',1732045488,1732217257),('4',20241108,1,20241108,'5','B22DCCN293',20241117165531,20241117165531),('7',1732043343,5,1732043538,'book_123a','B22DCCN293',1732043343,1732043538),('8',1732043765,8,1732043778,'book_YQX5','B22DCCN293',1732043765,1732043778),('9',1732043946,8,1732045488,'book_YQX5','B22DCCN293',1732043946,1732045488);
/*!40000 ALTER TABLE `home_booktransaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_category`
--

DROP TABLE IF EXISTS `home_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_category` (
  `id` varchar(13) NOT NULL,
  `label` varchar(255) NOT NULL,
  `created_at` bigint NOT NULL,
  `updated_at` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `label` (`label`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_category`
--

LOCK TABLES `home_category` WRITE;
/*!40000 ALTER TABLE `home_category` DISABLE KEYS */;
INSERT INTO `home_category` VALUES ('1','Van hoc',20241118135724,20241118140802),('3','Toan',20241118163110,20241118163110),('4','Toan23',1731922941,1731923005),('5','Khoa hoc',1732089708,1732089708),('6','a',1732089843,1732090713),('7','TIeng Anh',1732089910,1732090227);
/*!40000 ALTER TABLE `home_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_librarylog`
--

DROP TABLE IF EXISTS `home_librarylog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_librarylog` (
  `id` varchar(8) NOT NULL,
  `checked_in` bigint NOT NULL,
  `checked_out` bigint DEFAULT NULL,
  `student_id` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_librarylog_student_id_d3391bc0_fk_home_student_student_id` (`student_id`),
  CONSTRAINT `home_librarylog_student_id_d3391bc0_fk_home_student_student_id` FOREIGN KEY (`student_id`) REFERENCES `home_student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_librarylog`
--

LOCK TABLES `home_librarylog` WRITE;
/*!40000 ALTER TABLE `home_librarylog` DISABLE KEYS */;
INSERT INTO `home_librarylog` VALUES ('4',20241108145241,20241108145444,'B22DCCN293'),('5',20241108145452,20241108145457,'B22DCCN293'),('6',1732042406,1732043137,'B22DCCN293'),('7',1732045193,1732128144,'B22DCCN293'),('lib_0HA6',1732217650,NULL,'B22DCCN293'),('lib_2MI1',1732204028,1732204990,'B22DCCN293'),('lib_4SYI',1732204028,1732205014,'B22DCCN112'),('lib_8PSZ',1732204028,1732205670,'B22DCCN293'),('lib_FMJU',1732131212,1732134691,'B22DCCN293'),('lib_GKB2',1732216257,1732216286,'B22DCCN293'),('lib_JPLB',1732205698,1732210245,'B22DCCN293'),('lib_TG30',1732131212,1732204854,'B22DCCN112'),('lib_VDEL',1732205689,1732210252,'B22DCCN112'),('lib_W3OD',1732210280,NULL,'B22DCCN112'),('lib_Z7S4',1732204028,1732205680,'B22DCCN112');
/*!40000 ALTER TABLE `home_librarylog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_manager`
--

DROP TABLE IF EXISTS `home_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_manager` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `last_name` varchar(150) NOT NULL,
  `created_at` bigint NOT NULL,
  `updated_at` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_manager`
--

LOCK TABLES `home_manager` WRITE;
/*!40000 ALTER TABLE `home_manager` DISABLE KEYS */;
INSERT INTO `home_manager` VALUES (3,'tuan','pbkdf2_sha256$870000$1sCu1xCiGYQ04Ac2x23OXe$txUnZbnS/RXdIb8w0UYImsEoJHjyfG7BtUmCVsnaUz8=','2024-11-04 03:35:30.314071','','',1,1,1,'2024-11-04 03:35:55.122919','',20241117165531,20241117165531),(4,'hien1172004','pbkdf2_sha256$870000$IUcNpY0MCX8cCAxE3rhrBn$iZC+lmlIFq6oiHLpjymZMu7cSzhkCmqzlR/hYvkY5kI=','2024-11-04 03:39:17.405370','','',1,1,1,'2024-11-17 14:03:30.336305','',20241117165531,20241117165531);
/*!40000 ALTER TABLE `home_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_manager_groups`
--

DROP TABLE IF EXISTS `home_manager_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_manager_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `manager_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_manager_groups_manager_id_group_id_0a28dc22_uniq` (`manager_id`,`group_id`),
  KEY `home_manager_groups_group_id_761040c6_fk_auth_group_id` (`group_id`),
  CONSTRAINT `home_manager_groups_group_id_761040c6_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `home_manager_groups_manager_id_aca16231_fk` FOREIGN KEY (`manager_id`) REFERENCES `home_manager` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_manager_groups`
--

LOCK TABLES `home_manager_groups` WRITE;
/*!40000 ALTER TABLE `home_manager_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_manager_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_manager_user_permissions`
--

DROP TABLE IF EXISTS `home_manager_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_manager_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `manager_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `home_manager_user_permis_manager_id_permission_id_fa605aba_uniq` (`manager_id`,`permission_id`),
  KEY `home_manager_user_pe_permission_id_222ab99d_fk_auth_perm` (`permission_id`),
  CONSTRAINT `home_manager_user_pe_permission_id_222ab99d_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `home_manager_user_permissions_manager_id_ad782d65_fk` FOREIGN KEY (`manager_id`) REFERENCES `home_manager` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_manager_user_permissions`
--

LOCK TABLES `home_manager_user_permissions` WRITE;
/*!40000 ALTER TABLE `home_manager_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_manager_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_student`
--

DROP TABLE IF EXISTS `home_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_student` (
  `id` varchar(12) NOT NULL,
  `name` varchar(255) NOT NULL,
  `student_class` varchar(50) NOT NULL,
  `birthday` bigint NOT NULL,
  `student_id` varchar(128) NOT NULL,
  `created_at` bigint NOT NULL,
  `updated_at` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Student_id` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_student`
--

LOCK TABLES `home_student` WRITE;
/*!40000 ALTER TABLE `home_student` DISABLE KEYS */;
INSERT INTO `home_student` VALUES ('3','Hoang','12a',20111111,'B22DCCN112',20241117165531,20241117165531),('4','Hien','12b',20011111,'B22DCCN293',20241117165531,20241117165531);
/*!40000 ALTER TABLE `home_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_accesstoken`
--

DROP TABLE IF EXISTS `oauth2_provider_accesstoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_accesstoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `source_refresh_token_id` bigint DEFAULT NULL,
  `id_token_id` bigint DEFAULT NULL,
  `token_checksum` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oauth2_provider_accesstoken_token_checksum_85319a26_uniq` (`token_checksum`),
  UNIQUE KEY `source_refresh_token_id` (`source_refresh_token_id`),
  UNIQUE KEY `id_token_id` (`id_token_id`),
  KEY `oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_home_manager_id` (`user_id`),
  CONSTRAINT `oauth2_provider_acce_application_id_b22886e1_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_acce_id_token_id_85db651b_fk_oauth2_pr` FOREIGN KEY (`id_token_id`) REFERENCES `oauth2_provider_idtoken` (`id`),
  CONSTRAINT `oauth2_provider_acce_source_refresh_token_e66fbc72_fk_oauth2_pr` FOREIGN KEY (`source_refresh_token_id`) REFERENCES `oauth2_provider_refreshtoken` (`id`),
  CONSTRAINT `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_home_manager_id` FOREIGN KEY (`user_id`) REFERENCES `home_manager` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_accesstoken`
--

LOCK TABLES `oauth2_provider_accesstoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_application`
--

DROP TABLE IF EXISTS `oauth2_provider_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_application` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `client_id` varchar(100) NOT NULL,
  `redirect_uris` longtext NOT NULL,
  `client_type` varchar(32) NOT NULL,
  `authorization_grant_type` varchar(32) NOT NULL,
  `client_secret` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `user_id` int DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `algorithm` varchar(5) NOT NULL,
  `post_logout_redirect_uris` longtext NOT NULL,
  `hash_client_secret` tinyint(1) NOT NULL,
  `allowed_origins` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `oauth2_provider_application_user_id_79829054_fk_home_manager_id` (`user_id`),
  KEY `oauth2_provider_application_client_secret_53133678` (`client_secret`),
  CONSTRAINT `oauth2_provider_application_user_id_79829054_fk_home_manager_id` FOREIGN KEY (`user_id`) REFERENCES `home_manager` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_application`
--

LOCK TABLES `oauth2_provider_application` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_application` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_grant`
--

DROP TABLE IF EXISTS `oauth2_provider_grant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_grant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `redirect_uri` longtext NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `code_challenge` varchar(128) NOT NULL,
  `code_challenge_method` varchar(10) NOT NULL,
  `nonce` varchar(255) NOT NULL,
  `claims` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `oauth2_provider_gran_application_id_81923564_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_grant_user_id_e8f62af8_fk_home_manager_id` (`user_id`),
  CONSTRAINT `oauth2_provider_gran_application_id_81923564_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_grant_user_id_e8f62af8_fk_home_manager_id` FOREIGN KEY (`user_id`) REFERENCES `home_manager` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_grant`
--

LOCK TABLES `oauth2_provider_grant` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_grant` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_grant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_idtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_idtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_idtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `jti` char(32) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `application_id` bigint DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `jti` (`jti`),
  KEY `oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_idtoken_user_id_dd512b59_fk_home_manager_id` (`user_id`),
  CONSTRAINT `oauth2_provider_idto_application_id_08c5ff4f_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_idtoken_user_id_dd512b59_fk_home_manager_id` FOREIGN KEY (`user_id`) REFERENCES `home_manager` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_idtoken`
--

LOCK TABLES `oauth2_provider_idtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_idtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_idtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_refreshtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `access_token_id` bigint DEFAULT NULL,
  `application_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `revoked` datetime(6) DEFAULT NULL,
  `token_family` char(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `access_token_id` (`access_token_id`),
  UNIQUE KEY `oauth2_provider_refreshtoken_token_revoked_af8a5134_uniq` (`token`,`revoked`),
  KEY `oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr` (`application_id`),
  KEY `oauth2_provider_refreshtoken_user_id_da837fce_fk_home_manager_id` (`user_id`),
  CONSTRAINT `oauth2_provider_refr_access_token_id_775e84e8_fk_oauth2_pr` FOREIGN KEY (`access_token_id`) REFERENCES `oauth2_provider_accesstoken` (`id`),
  CONSTRAINT `oauth2_provider_refr_application_id_2d1c311b_fk_oauth2_pr` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_refreshtoken_user_id_da837fce_fk_home_manager_id` FOREIGN KEY (`user_id`) REFERENCES `home_manager` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_refreshtoken`
--

LOCK TABLES `oauth2_provider_refreshtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-22 10:17:26
