

# Array Utility Methods Chaining in JavaScript

## Overview

Method chaining allows multiple array operations to be performed in a single sequence. It improves readability and avoids intermediate variables.

---

## Basic Example

```javascript id="m7q2zp"
const arr = [1, 2, 3, 4, 5];

const result = arr
  .filter(num => num > 2)
  .map(num => num * 2);

console.log(result); // [6, 8, 10]
```

---

## With `reduce`

```javascript id="x4b9ks"
const arr = [1, 2, 3, 4];

const result = arr
  .filter(num => num % 2 === 0)
  .map(num => num * 2)
  .reduce((acc, val) => acc + val, 0);

console.log(result); // 12
```

---

## Real-world Style Example

```javascript id="d8t1vy"
const users = [
  { name: "A", age: 20 },
  { name: "B", age: 30 },
  { name: "C", age: 25 }
];

const result = users
  .filter(user => user.age > 21)
  .map(user => user.name);

console.log(result); // ["B", "C"]
```

---

## Important Points

* Works best with **immutable methods** (`map`, `filter`, `reduce`)
* Avoid chaining with mutating methods (`splice`, `sort`)
* Improves readability when used properly

---
