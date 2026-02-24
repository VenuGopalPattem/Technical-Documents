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