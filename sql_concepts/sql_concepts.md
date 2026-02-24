# SQL Concepts 


# ACID in SQL (Database Transactions)

## What is ACID?

ACID is a set of 4 rules that make sure database transactions are safe and reliable.

ACID stands for:

* **A** → Atomicity
* **C** → Consistency
* **I** → Isolation
* **D** → Durability

These rules are mainly used in relational databases like:

* PostgreSQL
* MySQL
* Oracle Database
* Microsoft SQL Server

---

# What is a Transaction?

A **transaction** is a group of SQL operations that work together.

Example:

* Deduct money from Account A
* Add money to Account B

Both steps together form **one transaction**.

We use:

```sql
BEGIN;
-- SQL queries
COMMIT;
```

If something goes wrong:

```sql
ROLLBACK;
```

---

# 1) Atomicity (All or Nothing)

Atomicity means:

> Either everything happens or nothing happens.

There is no middle state.

### Example – Bank Transfer

If ₹1000 is deducted from A, but not added to B,
that is wrong.

So database ensures:

* Both happen ✔
* Or none happen ❌

### Why it matters?

Without atomicity:

* Money can disappear.
* Data can become incomplete.

---

# 2) Consistency (Always Valid Data)

Consistency means:

> After transaction, database must follow all rules.

Rules include:

* Primary key
* Foreign key
* NOT NULL
* CHECK constraints

### Example

If balance cannot be negative:

```sql
CHECK (balance >= 0)
```

If transaction makes balance -500 → database stops it.

### Why it matters?

It prevents:

* Invalid data
* Broken relationships
* Duplicate primary keys

---

#  3) Isolation (Transactions Don’t Disturb Each Other)

Isolation means:

> Multiple users can work at the same time without breaking data.

Example:
Two people try to withdraw money from same account.

Database ensures:

* They don’t see half-completed work.
* They don’t use wrong data.

### Isolation Levels

* Read Uncommitted
* Read Committed
* Repeatable Read
* Serializable (Strongest)

Higher isolation → more safety → slightly slower performance.

---

# 4) Durability (Data Stays Safe After Commit)

Durability means:

> Once COMMIT is done, data will not disappear.

Even if:

* Power goes off
* System crashes
* Server restarts

Database saves data in disk and logs.

---

# Real Life Example

Imagine ATM transaction:

1. You withdraw ₹5000
2. ATM gives cash
3. Bank balance reduces

ACID ensures:

| Property    | What It Protects                     |
| ----------- | ------------------------------------ |
| Atomicity   | Money is both given AND deducted     |
| Consistency | Balance never goes invalid           |
| Isolation   | Two ATM users don’t mix data         |
| Durability  | After success, money record is saved |

---

# Why ACID is Important?

Without ACID:

* Data corruption happens
* Bank systems break
* E-commerce fails
* Orders get duplicated
* Money gets lost

ACID makes database trustworthy.


---

# CAP Theorem (Very Simple Version)

CAP says:

> In a distributed system, you can only guarantee **2 out of 3** things when a network problem happens.

C → Consistency
A → Availability
P → Partition Tolerance

---

## What Each Means 

* **Consistency** → Everyone sees the same latest data.
* **Availability** → System always gives a response.
* **Partition Tolerance** → System keeps working even if servers cannot talk to each other.

---

## The Important Part

When a network fails,
you must choose:

* **Consistency OR Availability**
  (because Partition tolerance is required in distributed systems)

---

## Example (Very Easy)

If servers disconnect:

* Stop system to keep data correct → **CP**
* Keep system running but data may delay → **AP**



---

# What is a JOIN?

A **JOIN** is used to combine rows from two or more tables based on a related column (usually a primary key and foreign key).

It helps you get data that is stored in different tables.

---

# Types of JOINs 

## 1) INNER JOIN

Returns only the rows that match in both tables.
Unmatched rows are removed.

---

## 2) LEFT JOIN (or LEFT OUTER JOIN)

Returns all rows from the left table and matching rows from the right table.
If no match, NULL is returned for the right side.

---

## 3) RIGHT JOIN (or RIGHT OUTER JOIN)

Returns all rows from the right table and matching rows from the left table.
If no match, NULL is returned for the left side.

---

## 4) FULL JOIN (or FULL OUTER JOIN)

Returns all rows from both tables.
If there is no match, NULL appears where data is missing.

---

Good 👍 now we’ll slow down and do it properly.

I will take **two small tables (6 rows each)** and show you **exactly how INNER JOIN works step-by-step**.

No theory overload. Just clarity.

---

# Step 1: Two Tables

### 🔵 Table 1: students

| id | name  |
| -- | ----- |
| 1  | Venu  |
| 2  | Ravi  |
| 3  | Anu   |
| 4  | Kiran |
| 5  | Meena |
| 6  | Arjun |

---

### 🟢 Table 2: marks

| student_id | marks |
| ---------- | ----- |
| 1          | 90    |
| 2          | 85    |
| 4          | 70    |
| 6          | 88    |
| 7          | 95    |
| 8          | 60    |

Notice carefully:

* student 3 → no marks
* student 5 → no marks
* marks 7 and 8 → no student

This is important.

---

# Step 2: The INNER JOIN Query

```sql
SELECT s.id, s.name, m.marks
FROM students s
INNER JOIN marks m
ON s.id = m.student_id;
```

---

# Step 3: How INNER JOIN Actually Works (Mentally)

Think like this 👇

Database checks **each row from students**
and tries to find a matching row in marks
where:

```
s.id = m.student_id
```

Let’s simulate manually.

---

## Row 1 → id = 1 (Venu)

Does marks table have student_id = 1?
Yes → 90

So result row:

| 1 | Venu | 90 |

---

## Row 2 → id = 2 (Ravi)

Match found → 85

| 2 | Ravi | 85 |

---

## Row 3 → id = 3 (Anu)

Is there student_id = 3 in marks?

❌ No

So this row is ignored.

---

## Row 4 → id = 4 (Kiran)

Match found → 70

| 4 | Kiran | 70 |

---

## Row 5 → id = 5 (Meena)

No match → ignored.

---

## Row 6 → id = 6 (Arjun)

Match found → 88

| 6 | Arjun | 88 |

---

# Step 4: Final Result After INNER JOIN

| id | name  | marks |
| -- | ----- | ----- |
| 1  | Venu  | 90    |
| 2  | Ravi  | 85    |
| 4  | Kiran | 70    |
| 6  | Arjun | 88    |

---

# Very Important Observation

Students removed:

* 3 (no marks)
* 5 (no marks)

Marks removed:

* 7
* 8

INNER JOIN only keeps matching pairs.

---

# How It Is Happening Internally 

Conceptually, database does this:

1. Take one row from students
2. Compare with ALL rows in marks
3. If condition matches → create result row
4. If no match → skip
5. Repeat for next student





# LEFT JOIN

```sql
SELECT s.id, s.name, m.marks
FROM students s
LEFT JOIN marks m
ON s.id = m.student_id;
```

### Result Table

| id | name  | marks |
| -- | ----- | ----- |
| 1  | Venu  | 90    |
| 2  | Ravi  | 85    |
| 3  | Anu   | NULL  |
| 4  | Kiran | 70    |
| 5  | Meena | NULL  |
| 6  | Arjun | 88    |

---

# Brief Explanation

LEFT JOIN keeps **all rows from the left table (students)**.

If a student has matching marks → marks appear.
If a student has no marks → NULL appears.

Rows from the marks table that don’t match students (7 and 8) are ignored.

---


LEFT JOIN = "Keep left table safe."



---

# RIGHT JOIN Query

```sql
SELECT s.id, s.name, m.marks
FROM students s
RIGHT JOIN marks m
ON s.id = m.student_id;
```

---

# RIGHT JOIN Result

| id   | name  | marks |
| ---- | ----- | ----- |
| 1    | Venu  | 90    |
| 2    | Ravi  | 85    |
| 4    | Kiran | 70    |
| 6    | Arjun | 88    |
| NULL | NULL  | 95    |
| NULL | NULL  | 60    |

---

# Brief Explanation

RIGHT JOIN keeps **all rows from the right table (marks)**.

If marks have a matching student → student details appear.
If marks do NOT have a matching student (7 and 8) → student columns become NULL.

Students without marks (3 and 5) are removed.

---

RIGHT JOIN = "Keep right table safe."


---

# FULL JOIN Query

```sql id="8mcrls"
SELECT s.id, s.name, m.marks
FROM students s
FULL JOIN marks m
ON s.id = m.student_id;
```

---

# FULL JOIN Result

| id   | name  | marks |
| ---- | ----- | ----- |
| 1    | Venu  | 90    |
| 2    | Ravi  | 85    |
| 3    | Anu   | NULL  |
| 4    | Kiran | 70    |
| 5    | Meena | NULL  |
| 6    | Arjun | 88    |
| NULL | NULL  | 95    |
| NULL | NULL  | 60    |

---

# Brief Explanation

FULL JOIN keeps **all rows from both tables**.

* If match exists → combined row.
* If no match on left → right side shows NULL.
* If no match on right → left side shows NULL.

Nothing is removed.

---

FULL JOIN = “Keep both tables safe.”

---

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

# Important Aggregate Functions (Reference Table)

| Function | What It Does   | Example Use Case    |
| -------- | -------------- | ------------------- |
| COUNT()  | Counts rows    | Number of employees |
| SUM()    | Adds values    | Total salary        |
| AVG()    | Average value  | Average marks       |
| MIN()    | Smallest value | Lowest salary       |
| MAX()    | Largest value  | Highest marks       |

👉 These 5 are the most important and used in interviews.

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

# What is Normalization in SQL?

**Normalization** is the process of organizing data in tables to:

* Reduce duplicate data
* Avoid data inconsistency
* Improve data integrity

> Normalization means breaking big tables into smaller related tables to avoid repetition.

---

# Why Do We Need Normalization?

Without normalization:

* Same data gets repeated many times
* Updating data becomes difficult
* Deleting data may cause problems
* Data can become inconsistent

---

# Simple Example (Without Normalization)

| student_id | student_name | course | course_teacher |
| ---------- | ------------ | ------ | -------------- |
| 1          | Venu         | DBMS   | Ravi Sir       |
| 1          | Venu         | OS     | Kiran Sir      |

Here:

* Student name is repeated.
* If we update the name, we must update in multiple rows.

---

# After Normalization

### Students table

| student_id | student_name |
| ---------- | ------------ |

### Courses table

| course_id | course_name | teacher |
| ---------- | ------------ |------------ |

### Enrollment table

| student_id | course_id |
| ---------- | ------------ |

Now:

* No unnecessary repetition
* Data is clean and structured

---

> Normalization is the process of organizing database tables to remove redundancy and maintain data consistency.

---

# Types of Normalization

---

#  1NF (First Normal Form)

## Rule:

- One value per cell (no multiple values in one column)

---

###  Not 1NF

| student_id | name | subjects |
| ---------- | ---- | -------- |
| 1          | Venu | DBMS, OS |

Problem:

* "subjects" has multiple values in one cell

---

###  After 1NF

| student_id | name | subject |
| ---------- | ---- | ------- |
| 1          | Venu | DBMS    |
| 1          | Venu | OS      |

 Each cell has only one value.

---

#  2NF (Second Normal Form)

## Rule:

- Must be in 1NF
- No partial dependency

---

### Example Table

| student_id | course_id | student_name | course_name |
| ---------- | --------- | ------------ | ----------- |

Primary Key = (student_id, course_id)

Problem:

* student_name depends only on student_id
* course_name depends only on course_id
* Not on full key

That is partial dependency 

---

### After 2NF

#### Students Table

| student_id | student_name |

#### Courses Table

| course_id | course_name |

#### Enrollment Table

| student_id | course_id |

Now everything depends on full key 

---

#  3NF (Third Normal Form)

## Rule:

- Must be in 2NF
- No transitive dependency

---

###  Not 3NF

| student_id | name | dept_id | dept_name |

Problem:

* dept_name depends on dept_id
* dept_id depends on student_id
* So dept_name indirectly depends on student_id

That is transitive dependency 

---

### After 3NF

#### Students Table

| student_id | name | dept_id |

#### Departments Table

| dept_id | dept_name |

Now:
Each column depends only on primary key 

---

1NF → No multiple values in one column
2NF → No partial dependency
3NF → No indirect dependency

---

# What is an INDEX in SQL?

An **index** is a special structure that makes searching data faster.

It works like:

>  Book index → helps you find topics quickly
>  SQL index → helps database find rows quickly

Without index → database checks rows one by one.
With index → database jumps directly to needed data.

---

#  Example Query

```sql
CREATE INDEX idx_name
ON employees(name);
```

### What this means:

* `CREATE INDEX` → Create a fast lookup structure
* `idx_name` → Name of the index
* `ON employees(name)` → Create it on the `name` column

So now when you run:

```sql
SELECT * FROM employees WHERE name = 'Ravi';
```

Database finds "Ravi" faster.

---

#  Important Points

✔ Index improves **SELECT** speed
❌ Index makes **INSERT, UPDATE, DELETE** slightly slower
✔ Primary key automatically has index
✔ Use index on columns used in:

* WHERE
* JOIN
* ORDER BY

---

> An index is a fast lookup system that helps SQL find data quickly without scanning the entire table.

---

# Transaction in SQL

A **transaction** is a group of SQL statements that run as one unit.

👉 Either **all statements succeed**
👉 Or **all are cancelled**

No partial changes.

---

#  Why we need it?

To keep data safe and correct.

Example:
Money transfer must fully complete or not happen at all.

---

#  Basic Syntax

```sql
START TRANSACTION;

-- SQL statements
UPDATE table_name SET column = value WHERE condition;

COMMIT;
```

If something goes wrong:

```sql
ROLLBACK;
```

---

# Important Commands

* `START TRANSACTION` → Begin
* `COMMIT` → Save changes
* `ROLLBACK` → Cancel changes

---

> A transaction is a set of SQL operations executed completely or not at all.



---

#  What is Locking in SQL?

**Locking** is a way for the database to control access to data when multiple users are working at the same time.

- It prevents data conflicts
- It keeps data safe and correct

---

#  Why Locking is Needed?

Imagine:

* User 1 updates a row
* User 2 tries to update the same row at the same time

Without locking, data may become wrong.

So database **locks** the data until first operation is finished.

---

# Types of Locks

### Shared Lock (Read Lock)

* Used when reading data
* Other users can read
* But cannot update

---

### Exclusive Lock (Write Lock)

* Used when updating or deleting
* No one else can read or write that row until done

---

#  Example

```sql
START TRANSACTION;

UPDATE employees
SET salary = 60000
WHERE id = 1;

COMMIT;
```

While this runs:
That row is locked.

Other users must wait until COMMIT or ROLLBACK.

---

> Locking is a mechanism that controls access to data to prevent conflicts during transactions.

---

# Database Isolation Levels

## What is Isolation Level?

Isolation level defines **how one transaction sees changes made by other transactions**.

It controls:

* Data visibility
* Data consistency
* Concurrency behavior

---

## Why It Matters

When multiple transactions run at the same time:

* One may read data
* Another may update data

Isolation level decides:

> Should the reader see the updated value or not?


| Isolation Level  | What It Allows                              | Problems Possible    | Safety Level |
| ---------------- | ------------------------------------------- | -------------------- | ------------ |
| READ UNCOMMITTED | Can read uncommitted data                   | Dirty Reads          | Very Low     |
| READ COMMITTED   | Can read only committed data                | Non-repeatable Reads | Medium       |
| REPEATABLE READ  | Same data if read again in same transaction | Phantom Reads        | High         |
| SERIALIZABLE     | Transactions run one by one                 | No common issues     | Very High    |



---

# What is a Trigger?

A **trigger** is a stored SQL block that runs **automatically** when an `INSERT`, `UPDATE`, or `DELETE` happens on a table.

You don’t execute it manually.
The database executes it.

---

# Definition

> A trigger is an automatic action performed by the database when a specified event occurs on a table.

---

# Simple Example

### Table: employees

| id | name | salary |
| -- | ---- | ------ |
| 1  | Ravi | 50000  |

---

### Requirement

If someone inserts a negative salary, make it `0`.

---

## Trigger Query

```sql
CREATE TRIGGER check_salary
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
   IF NEW.salary < 0 THEN
      SET NEW.salary = 0;
   END IF;
END;
```

---

# What This Query Does

* `BEFORE INSERT` → Runs before inserting
* `FOR EACH ROW` → Runs for every new row
* `NEW.salary` → Refers to the incoming value
* If salary is negative → change it to 0

---

# What Happens Now?

If someone runs:

```sql
INSERT INTO employees VALUES (2, 'Anu', -2000);
```

Instead of -2000, salary becomes:

`0`

Because trigger corrected it automatically.

---

