# Transaction in SQL

A **transaction** is a group of SQL statements that run as one unit.

- Either **all statements succeed**
- Or **all are cancelled**

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
