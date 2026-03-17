
# Difference Between `throw new Error()` and `throw "string"` in JavaScript

## Overview

Errors in JavaScript can be thrown using either an `Error` object or a plain value like a string. These approaches differ in structure and usability.

---

## `throw new Error("message")`

Throws an `Error` object.

```javascript
try {
  throw new Error("Something went wrong");
} catch (error) {
  console.log(error.message); // "Something went wrong"
  console.log(error.name);    // "Error"
}
```

### Characteristics

* Has properties: `name`, `message`, `stack`
* Provides stack trace
* Standard way to handle errors

---

## `throw "message"`

Throws a plain string.

```javascript
try {
  throw "Something went wrong";
} catch (error) {
  console.log(error); // "Something went wrong"
}
```

### Characteristics

* No structured properties
* No stack trace
* Limited debugging information

---

## Comparison

| Feature     | `new Error()`        | `"string"`      |
| ----------- | -------------------- | --------------- |
| Type        | Object               | Primitive       |
| Properties  | name, message, stack | None            |
| Stack Trace | Available            | Not available   |
| Usage       | Standard             | Not recommended |

---
