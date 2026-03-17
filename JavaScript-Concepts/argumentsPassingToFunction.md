

# Variable Number of Arguments in JavaScript Functions

## Overview

JavaScript functions can accept a variable number of arguments using the `arguments` object or rest parameters (`...`).

---

## Using `arguments` Object

Available inside regular functions.

```javascript id="k9p2dx"
function sum() {
  let total = 0;

  for (let i = 0; i < arguments.length; i++) {
    total += arguments[i];
  }

  return total;
}

console.log(sum(1, 2, 3)); // 6
```

### Characteristics

* Array-like object
* Available only in regular functions
* Does not work in arrow functions

---

## Using Rest Parameters (`...`)

Modern and preferred approach.

```javascript id="m4q7zs"
function sum(...nums) {
  return nums.reduce((acc, val) => acc + val, 0);
}

console.log(sum(1, 2, 3, 4)); // 10
```

### Characteristics

* Collects arguments into an array
* Works with arrow functions
* Cleaner and more readable

---

## Combining with Other Parameters

```javascript id="t8x3vn"
function log(first, ...rest) {
  console.log(first);
  console.log(rest);
}

log(1, 2, 3, 4);
```

---
