

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

- Index improves **SELECT** speed
- Index makes **INSERT, UPDATE, DELETE** slightly slower
- Primary key automatically has index
- Use index on columns used in:

* WHERE
* JOIN
* ORDER BY

---

> An index is a fast lookup system that helps SQL find data quickly without scanning the entire table.

---
