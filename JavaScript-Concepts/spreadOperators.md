
# Spread Operator in JavaScript (`...`)

## Overview

The spread operator (`...`) is used to expand elements of arrays, objects, or iterables. It is commonly used for copying, merging, and passing values.

---

## Array Usage

### Copy Array — immutable

```javascript
const arr = [1, 2, 3];

const copy = [...arr];

console.log(copy); // [1, 2, 3]
```

---

### Merge Arrays — immutable

```javascript
const a = [1, 2];
const b = [3, 4];

const result = [...a, ...b];

console.log(result); // [1, 2, 3, 4]
```

---

### Add Elements

```javascript
const arr = [2, 3];

const result = [1, ...arr, 4];

console.log(result); // [1, 2, 3, 4]
```

---

## Object Usage

### Copy Object — immutable

```javascript
const obj = { a: 1, b: 2 };

const copy = { ...obj };

console.log(copy); // { a: 1, b: 2 }
```

---

### Merge Objects — immutable

```javascript
const obj1 = { a: 1 };
const obj2 = { b: 2 };

const result = { ...obj1, ...obj2 };

console.log(result); // { a: 1, b: 2 }
```

---

### Override Properties

```javascript
const obj = { a: 1, b: 2 };

const updated = { ...obj, b: 10 };

console.log(updated); // { a: 1, b: 10 }
```

---

## Function Arguments

### Spread Arguments

```javascript
function add(a, b, c) {
  return a + b + c;
}

const nums = [1, 2, 3];

console.log(add(...nums)); // 6
```

---

## String Usage

```javascript
const str = "abc";

const arr = [...str];

console.log(arr); // ["a", "b", "c"]
```

---
