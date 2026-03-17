

# Functions Without a Return Statement in JavaScript

## Overview

In JavaScript, if a function does not explicitly return a value, it automatically returns `undefined`.

---

## Default Return Value

```javascript
function test() {
  let x = 10;
}

let result = test();

console.log(result); // undefined
```

---

## Explicit vs Implicit Return

### Without Return

```javascript
function add(a, b) {
  a + b;
}

console.log(add(2, 3)); // undefined
```

### With Return

```javascript
function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // 5
```

---

## Early Exit Without Return Value

```javascript
function check(value) {
  if (!value) {
    return;
  }
  return value;
}

console.log(check(0)); // undefined
```

---

## Arrow Functions

### Without Return

```javascript
const test = () => {
  10 + 20;
};

console.log(test()); // undefined
```

### With Implicit Return

```javascript
const test = () => 10 + 20;

console.log(test()); // 30
```

---

## Common Issues

### Missing Return

```javascript
function multiply(a, b) {
  let result = a * b;
}

let output = multiply(2, 3);

console.log(output); // undefined
```

---
