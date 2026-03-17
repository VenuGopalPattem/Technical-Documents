

# Throwing Errors in JavaScript

## Overview

Errors can be created and thrown manually using the `throw` statement. This is used to stop execution and signal that something went wrong.

---

## Basic Syntax

```javascript
throw expression;
```

---

## Throwing a Custom Error

```javascript
function checkAge(age) {
  if (age < 18) {
    throw new Error("Not allowed");
  }
}

checkAge(15); // throws error
```

---

## Using `try...catch`

```javascript
try {
  throw new Error("Something went wrong");
} catch (error) {
  console.log(error.message);
}
```

---

## Throwing Different Types

```javascript
throw "Error message";
throw 404;
throw true;
```

---

## Built-in Error Types

```javascript
throw new TypeError("Invalid type");
throw new ReferenceError("Variable not defined");
throw new RangeError("Out of range");
```

---

## Conditional Throw

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error("Division by zero");
  }
  return a / b;
}
```

---

## Custom Error Handling

```javascript
function process(data) {
  if (!data) {
    throw new Error("Invalid data");
  }
}
```

---
