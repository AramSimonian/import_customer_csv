USE `ezyvet`;
DROP procedure IF EXISTS `usp_add_contact`;

DELIMITER $$
USE `ezyvet`$$
CREATE PROCEDURE `usp_add_contact` (
	IN title VARCHAR(4),
    IN first_name VARCHAR(64),
    IN last_name VARCHAR(64),
    IN company_name VARCHAR(64),
    IN date_of_birth DATETIME,
    IN notes VARCHAR(255),
	OUT contact_id INT
)
BEGIN
	INSERT INTO contact (
		title,
        first_name,
        last_name,
        company_name,
        date_of_birth,
        notes
	)
	VALUES (
		title,
        first_name,
        last_name,
        company_name,
        date_of_birth,
        notes		
    );
    
    SELECT LAST_INSERT_ID();
END$$

DELIMITER ;

