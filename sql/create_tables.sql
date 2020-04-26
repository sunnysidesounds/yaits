CREATE TABLE IF NOT EXISTS projects (
    `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NULL,
    `description` varchar(500) NULL,
    `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS users (
     `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
     `username` varchar(125) NULL,
     `first_name` varchar(125) NULL,
     `last_name` varchar(125) NULL,
     `email` varchar(255) NULL,
     `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
     PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

CREATE TABLE IF NOT EXISTS issues (
   `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
   `project_id` int(10) UNSIGNED NOT NULL,
   `name` varchar(255) NULL,
   `description` varchar(500) NULL,
   `priority_level` int(10) UNSIGNED NOT NULL DEFAULT '1',
   `assigned_to_user_id` int(10) UNSIGNED NOT NULL DEFAULT 0,
   `created_by_user_id` int(10) UNSIGNED NOT NULL,
   `status` ENUM('OPEN', 'INPROGRESS', 'REOPENED', 'RESOLVED', 'CLOSED') NOT NULL,
   `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
   PRIMARY KEY (id),
   KEY `project_id` (`project_id`),
   KEY `index_name` (`name`(255)),
   CONSTRAINT `project_id_constraint_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`),
   CONSTRAINT `created_by_user_id_constraint_1` FOREIGN KEY (`created_by_user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;