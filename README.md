![Στιγμιότυπο οθόνης (837)](https://user-images.githubusercontent.com/57221590/153102241-db516325-e9d9-4169-bff5-609306fad307.png)


# SAMSUNG INNOVATION CAMPUS - UPSKILLING DIGITALLY

# 1) Python:
# Questions about the description of the dataset
1. Read data.csv
2. Print the last 5 dataframe records
3. How many (number) and which (names) columns has the dataset you uploaded?
4. As what type of data, does the pandas library recognize the columns of the dataset?
5. Are ther missing value columns? And if so, which ones?
6. What is the total number of registrations?

# Instructions for cleaning the dataset
1. Remove from the dataset all rows that have NaN (missing values) in the 'Description' and / or 'CustomerID' columns. Tip: see the method [dropna] 
2. Delete all lines where the 'Description' column is: "AMAZON FEE", "Manual", "SAMPLES", "POSTAGE" or "PACKING CHARGE". (You can delete any way you want, with one or more lines of code, the goal is to keep the correct entries)
3. Remove from the dataset all records that have a negative value in the 'Quantity' column
4. Create a column called ItemTotal that contains the result of the Quantity * UnitPrice operation per line to calculate the total cost per product category

# Questions for understanding the dataset
1. What is the number of unique / different customers (do not take into account all the registrations that have a ΝΑΝ instead of a price in the field of CustomerID)?
2. Which countries does the company still trade with? 
3. How long does the data we have available relate to? (Tip finding the maximum and minimum value of the InvoiceDate column)
4. Which product / s can a customer buy who wants to spend 100-150 euros?
5. If we search the products (in the descriptions) with the term "HANDBAG" what results will we get?

# 2) SQL:
# Instructions
1. Import the database backup BackupFull.sql
2. Write queries in order to answer tasks 1-10

# Tasks
1. Write a query to get all employee details from the employee table order by first salary, descending
2. Write a query to get the first 2 characters of first name from employees table
3. Write a query to display the last name of all employees who have both "b" and "c" in their first name
4. Write a query to get the highest, lowest, sum, and average salary of all employees that work in the IT dept
5. Write a query to find the name first_name, last_name, and salary of the employees whose salary is less than the average salary
6. Write a query to fetch odd numbered records from employees table
7. Write a query to select last 20 records from a table
8. Write a query to find the name first_name, last_name and hire date of the employees hired before 'Jones'
9. Write a query to extract the month from the hire date of the employees
10. Write a query to get the details of the employees where the length of their first name is greater than or equal to 5
