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
