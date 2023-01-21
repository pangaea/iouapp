--- Create Database ---
CREATE DATABASE IF NOT EXISTS IouApp;

--- Create Tables ---
CREATE TABLE IF NOT EXISTS `IouApp`.`users` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(64) NULL,
  `display_name` VARCHAR(64) NULL,
  `email` VARCHAR(128) NULL,
  `password_hash` VARCHAR(128) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE IF NOT EXISTS `IouApp`.`iou` (
    `id` BIGINT NOT NULL AUTO_INCREMENT,
    `owed` DECIMAL(10,2),
    `notes` VARCHAR(128) NULL,
    `from_user_id` BIGINT,
    INDEX `from_user_id` (from_user_id),
    FOREIGN KEY (from_user_id) REFERENCES users(id),
    `to_user_id` BIGINT,
    INDEX `to_user_id` (to_user_id),
    FOREIGN KEY (to_user_id) REFERENCES users(id),
    PRIMARY KEY (`id`));

-- Stored Procedures ---
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_username VARCHAR(64),
    IN p_display_name VARCHAR(64),
    IN p_email VARCHAR(128),
    IN p_password_hash VARCHAR(128)
)
BEGIN
    if ( select exists (select 1 from users where username = p_username) ) THEN
      
        select 'Username Exists !!';
      
    ELSE
      
        insert into users
        (
            username,
            display_name,
            email,
            password_hash
        )
        values
        (
            p_username,
            p_display_name,
            p_email,
            p_password_hash
        );
      
    END IF;
END$$
DELIMITER ;