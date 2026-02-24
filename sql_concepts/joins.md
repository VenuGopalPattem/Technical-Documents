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

Think like this , 

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
