DELIMITER //
CREATE PROCEDURE `spFindCity`(
	IN City_name varchar(20)
)
BEGIN
	select CUST_NAME from customer where WORKING_AREA = City_name;
END//
DELIMITER ;


