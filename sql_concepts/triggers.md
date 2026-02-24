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
