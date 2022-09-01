DELIMITER //
create procedure `spAgentCode`()
BEGIN
	DECLARE name varchar(20);
	DECLARE city varchar(20);
	DECLARE country varchar(20);
	DECLARE grade int;
	DECLARE vend int default 0;
	DECLARE c cursor for select CUST_NAME,CUST_CITY,CUST_COUNTRY,GRADE from customer where AGENT_CODE LIKE 'A00%';
	DECLARE continue handler for not found set vend=1;
	open c;
	get_cust:loop
	fetch c into name,city,country,grade;
	select name,city,country,grade;
	if vend=1 then
	leave get_cust;
	end if;
	end loop get_cust;
END//
DELIMITER ;


