

# Default Parameters in JavaScript

## Overview

Default parameters allow function parameters to have predefined values when no argument or `undefined` is passed.

---

## Basic Syntax

```javascript id="f0g3m2"
function greet(name = "Guest") {
  return `Hello, ${name}`;
}

console.log(greet());        // Hello, Guest
console.log(greet("Venu"));  // Hello, Venu
```

---

## When `undefined` is Passed

```javascript id="v5k9dp"
function test(value = 10) {
  return value;
}

console.log(test(undefined)); // 10
```

---

## When `null` is Passed

```javascript id="m2q8zc"
function test(value = 10) {
  return value;
}

console.log(test(null)); // null
```

---

## Multiple Default Parameters

```javascript id="j3r1bx"
function add(a = 0, b = 0) {
  return a + b;
}

console.log(add());      // 0
console.log(add(5, 3));  // 8
```

---

## Using Expressions

```javascript id="s9x4lw"
function calculate(a, b = a * 2) {
  return b;
}

console.log(calculate(5)); // 10
```

---
