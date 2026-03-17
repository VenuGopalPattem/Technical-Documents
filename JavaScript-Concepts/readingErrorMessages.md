

# Reading Error Messages and Stack Traces in JavaScript

## Overview

Error messages and stack traces help identify where and why a program failed. Understanding them is essential for debugging.

---

## Error Structure

```javascript
TypeError: Cannot read properties of undefined (reading 'name')
    at getUser (app.js:10:15)
    at main (app.js:20:5)
```

### Parts

* **Error Type**: `TypeError`
* **Message**: description of the issue
* **Stack Trace**: list of function calls with file and line numbers

---

## Example

```javascript
function getUser(user) {
  return user.name;
}

function main() {
  let data = undefined;
  getUser(data);
}

main();
```

### Error

```text
TypeError: Cannot read properties of undefined (reading 'name')
    at getUser (app.js:2:15)
    at main (app.js:7:3)
```

---

## How to Read Stack Trace

1. Start from the top line (error type and message)
2. Go to the first `at` line
3. Locate file and line number
4. Trace back through function calls

---

## Common Error Types

```javascript
TypeError        // wrong type usage
ReferenceError   // variable not defined
SyntaxError      // invalid syntax
RangeError       // value out of range
```

---

## Debugging Steps

1. Read the error message
2. Identify the exact line number
3. Check the variable causing the issue
4. Trace function calls
5. Fix the root cause

---

## Practice Examples

### Example 1

```javascript
let arr;

console.log(arr.length);
```

---

### Example 2

```javascript
function test() {
  console.log(x);
}

test();
```

---

### Example 3

```javascript
JSON.parse("{ invalid json }");
```

---
