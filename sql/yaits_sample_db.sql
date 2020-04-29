/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

SET FOREIGN_KEY_CHECKS=0;

# Dump of table projects
# ------------------------------------------------------------

DROP TABLE IF EXISTS `projects`;

CREATE TABLE `projects` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;

INSERT INTO `projects` (`id`, `name`, `description`, `last_updated`)
VALUES
	(1,'Backlogs','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.','2020-04-29 00:05:08'),
	(2,'Test Project 1','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.','2020-04-29 00:05:10'),
	(3,'Test Project 2','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.','2020-04-29 00:05:11'),
	(4,'Test Project 3','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.','2020-04-29 00:05:13'),
	(5,'Test Project 4','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.','2020-04-29 00:05:14'),
	(6,'Test Project 5','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.','2020-04-29 00:05:15');

/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table users
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(125) DEFAULT NULL,
  `first_name` varchar(125) DEFAULT NULL,
  `last_name` varchar(125) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;

INSERT INTO `users` (`id`, `username`, `first_name`, `last_name`, `email`, `last_updated`)
VALUES
	(1,'smartin','Steve','Martin','SteveMartin@some_email.com','2020-04-29 00:07:00'),
	(2,'cchase','Chevy','Chase','ChevyChase@some_email.com','2020-04-29 00:07:37'),
	(3,'mshort','Martin','Short','MartinShort@some_email.com','2020-04-29 00:08:09');

/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table issues
# ------------------------------------------------------------

DROP TABLE IF EXISTS `issues`;

CREATE TABLE `issues` (
                          `id` int unsigned NOT NULL AUTO_INCREMENT,
                          `project_id` int unsigned NOT NULL,
                          `name` varchar(255) DEFAULT NULL,
                          `description` varchar(500) DEFAULT NULL,
                          `priority_level` int unsigned NOT NULL DEFAULT '1',
                          `assigned_to_user_id` int unsigned NOT NULL DEFAULT '0',
                          `created_by_user_id` int unsigned NOT NULL,
                          `status` enum('OPEN','INPROGRESS','REOPENED','RESOLVED','CLOSED') NOT NULL,
                          `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                          PRIMARY KEY (`id`),
                          KEY `project_id` (`project_id`),
                          KEY `index_name` (`name`),
                          KEY `created_by_user_id_constraint_1` (`created_by_user_id`),
                          CONSTRAINT `created_by_user_id_constraint_1` FOREIGN KEY (`created_by_user_id`) REFERENCES `users` (`id`),
                          CONSTRAINT `project_id_constraint_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `issues` WRITE;
/*!40000 ALTER TABLE `issues` DISABLE KEYS */;

INSERT INTO `issues` (`id`, `project_id`, `name`, `description`, `priority_level`, `assigned_to_user_id`, `created_by_user_id`, `status`, `last_updated`)
VALUES
(3,2,'Lorem Ipsum Issue 1','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',1,2,1,'OPEN','2020-04-29 00:03:09'),
(6,2,'Lorem Ipsum Issue 2','At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. ',1,0,1,'OPEN','2020-04-29 00:03:41'),
(7,2,'Lorem Ipsum Issue 3','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',1,0,1,'OPEN','2020-04-29 00:03:15'),
(8,2,'Lorem Ipsum Issue 4','At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. ',1,0,1,'OPEN','2020-04-29 00:03:44'),
(10,1,'Lorem Ipsum Issue 5','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',2,1,1,'OPEN','2020-04-29 00:03:19'),
(12,1,'Lorem Ipsum Issue 6','At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. ',1,1,1,'OPEN','2020-04-29 00:03:47'),
(13,1,'Lorem Ipsum Issue 7','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',1,1,1,'OPEN','2020-04-29 00:03:22'),
(14,1,'Lorem Ipsum Issue 8','At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. ',1,1,1,'OPEN','2020-04-29 00:03:49'),
(15,1,'Lorem Ipsum Issue 9','Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',1,1,1,'OPEN','2020-04-29 00:03:24'),
(16,1,'Lorem Ipsum Issue 10','At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. ',1,1,1,'OPEN','2020-04-29 00:03:51');

/*!40000 ALTER TABLE `issues` ENABLE KEYS */;
UNLOCK TABLES;

SET FOREIGN_KEY_CHECKS=1;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
