
# When to Use `forEach`, `map`, `filter`, `reduce` in JavaScript

## Overview

These methods are used to iterate and process arrays. Each has a specific purpose based on the required output.

---

## `forEach`

Use when performing an action for each element without returning a new array.

```javascript
const arr = [1, 2, 3];

arr.forEach(x => {
  console.log(x);
});
```

* Does not return a value
* Used for side effects (logging, updating external variables)

---

## `map`

Use when transforming each element and returning a new array.

```javascript
const arr = [1, 2, 3];

const result = arr.map(x => x * 2);

console.log(result); // [2, 4, 6]
```

* Returns new array
* Same length as input

---

## `filter`

Use when selecting elements based on a condition.

```javascript
const arr = [1, 2, 3];

const result = arr.filter(x => x > 1);

console.log(result); // [2, 3]
```

* Returns new array
* Can change length

---

## `reduce`

Use when reducing array to a single value.

```javascript
const arr = [1, 2, 3];

const sum = arr.reduce((acc, curr) => acc + curr, 0);

console.log(sum); // 6
```

* Returns single value
* Flexible for complex operations

---

## Comparison

| Method  | Purpose          | Returns      |
| ------- | ---------------- | ------------ |
| forEach | Side effects     | undefined    |
| map     | Transform data   | New array    |
| filter  | Select elements  | New array    |
| reduce  | Aggregate values | Single value |

---
