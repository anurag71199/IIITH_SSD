DELIMITER //
create procedure `spAddTwo`(
	IN `first_num` int,
	IN `second_num` int,
	OUT `res` int
)
BEGIN
	Set res = first_num + second_num;
END//
DELIMITER ;



