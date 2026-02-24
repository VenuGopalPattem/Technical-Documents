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
