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
