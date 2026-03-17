
# Importance of `catch` Block in JavaScript

## Overview

The `catch` block is used to handle errors that occur inside a `try` block. It prevents program crashes and allows controlled error handling.

---

## Basic Usage

```javascript
try {
  let data = JSON.parse("invalid json");
} catch (error) {
  console.log("Error handled");
}
```

---

## Prevents Program Crash

Without `catch`, errors stop execution.

```javascript
JSON.parse("invalid json"); // program stops
```

With `catch`:

```javascript
try {
  JSON.parse("invalid json");
} catch (error) {
  console.log("Execution continues");
}
```

---

## Access Error Information

```javascript
try {
  undefinedFunction();
} catch (error) {
  console.log(error.name);
  console.log(error.message);
}
```

---

## Custom Error Handling

```javascript
function check(value) {
  if (!value) {
    throw new Error("Invalid value");
  }
}

try {
  check(null);
} catch (error) {
  console.log(error.message);
}
```

---

## Control Application Flow

```javascript
try {
  let result = riskyOperation();
} catch (error) {
  result = null;
}
```

---

## Conditional Handling

```javascript
try {
  someFunction();
} catch (error) {
  if (error instanceof TypeError) {
    console.log("Type issue");
  }
}
```

---
