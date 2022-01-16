/*  
	TEAM 3
	TEAM MEMBERS:
	IOANNA - MARIA PAPIDAKI
	VASILIKI PSOROGIANNI
	IOANNA DEDELOUDI  
*/


/* 1st question */
SELECT *
  FROM [hr].[dbo].[employees]
  ORDER BY SALARY DESC

/* 2nd question */
SELECT SUBSTRING (FIRST_NAME,1,2) 
  FROM [hr].[dbo].[employees]

/* 3rd question */
SELECT LAST_NAME
  FROM [hr].[dbo].[employees]
  WHERE (FIRST_NAME like '%b%'  AND FIRST_NAME like '%c%')

/* 4th question */
SELECT MAX (SALARY), MIN (SALARY), SUM (SALARY), AVG (SALARY)
  FROM [hr].[dbo].[employees]
  WHERE JOB_ID='IT_PROG'

/* 5th question */
SELECT [FIRST_NAME],[LAST_NAME],[SALARY]
  FROM [hr].[dbo].[employees]
  WHERE SALARY < (SELECT AVG (SALARY) FROM [hr].[dbo].[employees])

/* 6th question */

/* Για εμφάνιση περιττών record id */
ALTER TABLE [hr].[dbo].[employees]
ADD Record_id int identity(1,1);

SELECT *
  FROM [hr].[dbo].[employees]
  WHERE Record_id IN(SELECT Record_id FROM [hr].[dbo].[employees] WHERE Record_id % 2 <> 0);

/*
ALTER TABLE [hr].[dbo].[employees]
DROP COLUMN Record_id;  
*/

/* Για εμφάνιση περιττών employee id */
SELECT *
  FROM [hr].[dbo].[employees]
  WHERE EMPLOYEE_ID IN(SELECT EMPLOYEE_ID FROM [hr].[dbo].[employees] WHERE EMPLOYEE_ID % 2 <> 0);

 /* 7th question */

 /* Αν επιλέξουμε τον πίνακα employees */
SELECT * 
  FROM [hr].[dbo].[employees] 
  WHERE EMPLOYEE_ID NOT IN (SELECT TOP((SELECT COUNT(*) FROM [hr].[dbo].[employees] ) -20 )EMPLOYEE_ID FROM [hr].[dbo].[employees])

/* Αντίστοιχες εντολές και για τους υπόλοιπους πίνακες */

 /* 8th question */
SELECT [FIRST_NAME], [LAST_NAME], [HIRE_DATE]
  FROM [hr].[dbo].[employees]
  WHERE HIRE_DATE < (SELECT HIRE_DATE FROM [hr].[dbo].[employees] WHERE LAST_NAME = 'Jones')

/* 9th question */
SELECT MONTH (HIRE_DATE) 
  FROM [hr].[dbo].[employees]

/* 10th question */
SELECT * 
  FROM [hr].[dbo].[employees]
  WHERE LEN(FIRST_NAME)>=5


