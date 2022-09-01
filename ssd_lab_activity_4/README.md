# LAB ACTIVITY 4: STORED PROCEDURE and CURSOR
## Software Systems Development

### Question 1
Created a stored procedure called spAddtwo where I have declared two IN parameters for the two input numbers and one out parameter for the result. In order to call the function, use the following syntax:

call spAddTwo(5,8,@s); 
select @s; //answer will come as 13

### Solution 2
Created a stored procedure called spFindCity which takes city name as a parameter and runs the required where clause. In order to call the function, use the following syntax:

call spFindCity('Bangalore');

### Solution 3
Created a stored procedure called spGreaterAmount runs the required where condition and returns a table with the mentioned rows. In order to call the function, use the following syntax:
call spGreaterAmount;


### Solution 4
Created a stored procedure called spAgentCode. Declared the four mentioned variables and made a cursor which points to the result set of the select query based on the given conditions. Then I loop through the result set till eof and store the values of the resultset pointed by the cursor into the variables created earlier and select them. In order to call the function, use the following syntax:

call spAgentCode;
