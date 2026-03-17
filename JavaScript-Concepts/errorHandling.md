

# Error Handling in JavaScript (try...catch)

## Overview

`try...catch` is used to handle runtime errors and prevent program crashes.

---

## Basic Syntax

```javascript
try {
  // code that may throw error
} catch (error) {
  // handle error
}
```

---

## Example

```javascript
try {
  let data = JSON.parse("invalid json");
} catch (error) {
  console.log("Error occurred");
}
```

---

## Accessing Error Object

```javascript
try {
  undefinedFunction();
} catch (error) {
  console.log(error.name);    // error type
  console.log(error.message); // error message
}
```

---

## `finally` Block

Executes regardless of error.

```javascript
try {
  console.log("try block");
} catch (error) {
  console.log("error");
} finally {
  console.log("always runs");
}
```

---

## Throwing Errors

```javascript
function checkAge(age) {
  if (age < 18) {
    throw new Error("Not allowed");
  }
}

try {
  checkAge(15);
} catch (error) {
  console.log(error.message);
}
```

---

## Conditional Handling

```javascript
try {
  let result = riskyOperation();
} catch (error) {
  if (error instanceof TypeError) {
    console.log("Type error");
  } else {
    console.log("Other error");
  }
}
```

---

## Async Handling (with async/await)

```javascript
async function fetchData() {
  try {
    let res = await fetch("invalid-url");
  } catch (error) {
    console.log("Fetch failed");
  }
}
```

---
