# What is Aggregation?

**Aggregation** means:

> Performing a calculation on multiple rows and returning a single summarized value.

It reduces many rows into fewer results .

Example:

* Total salary of all employees
* Average marks of students
* Maximum price of products

---

# Types of Aggregations 

There are mainly 4 types of aggregations:

### 1) Counting

* How many rows?
* Function: `COUNT()`

---

### 2) Summation

* Adding numeric values
* Function: `SUM()`

---

### 3) Average

* Finding mean value
* Function: `AVG()`

---

### 4) Extreme Values

* Smallest value → `MIN()`
* Largest value → `MAX()`

---

# Important Aggregate Functions 

| Function | What It Does   | Example Use Case    |
| -------- | -------------- | ------------------- |
| COUNT()  | Counts rows    | Number of employees |
| SUM()    | Adds values    | Total salary        |
| AVG()    | Average value  | Average marks       |
| MIN()    | Smallest value | Lowest salary       |
| MAX()    | Largest value  | Highest marks       |


---

# Demonstration Table


## employees

| id | name  | dept | salary |
| -- | ----- | ---- | ------ |
| 1  | Venu  | IT   | 50000  |
| 2  | Ravi  | HR   | 60000  |
| 3  | Anu   | IT   | 55000  |
| 4  | Kiran | HR   | 45000  |
| 5  | Meena | IT   | 70000  |

---

# Examples Using This Table

---

## COUNT()

How many employees?

```sql
SELECT COUNT(*) FROM employees; # Result 5 
```

---

## SUM()

Total salary of all employees:

```sql
SELECT SUM(salary) FROM employees; # Result 280000
```

---

##  AVG()

Average salary:

```sql
SELECT AVG(salary) FROM employees; # Result 56000
```

---

##  MIN()

Lowest salary:

```sql
SELECT MIN(salary) FROM employees; #  Result 45000
```


---

##  MAX()

Highest salary:

```sql
SELECT MAX(salary) FROM employees; # Result 70000
```

---

# Using GROUP BY 

Now suppose we want total salary per department.

```sql
SELECT dept, SUM(salary)
FROM employees
GROUP BY dept;
```

### Result:

| dept | sum    |
| ---- | ------ |
| IT   | 175000 |
| HR   | 105000 |

 GROUP BY divides the table into groups and then aggregation runs on each group.

---

#  Final Simple Summary

Aggregation = summarizing data.

Main functions:

* COUNT()
* SUM()
* AVG()
* MIN()
* MAX()

GROUP BY is used when you want aggregation per category.

---
