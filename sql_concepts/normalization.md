

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
