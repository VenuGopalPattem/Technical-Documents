

# Truthy and Falsy Values in JavaScript

## Overview

In JavaScript, values are evaluated as either **truthy** or **falsy** in boolean contexts such as `if` statements, loops, and logical operations.

---

## Falsy Values

The following values are considered falsy:

```javascript
false
0
-0
0n
""
null
undefined
NaN
```

### Example

```javascript
if (0) {
  console.log("runs");
} else {
  console.log("does not run"); // executes
}
```

---

## Truthy Values

All values that are not falsy are truthy.

Examples:

```javascript
true
1
-1
"hello"
"0"
[]
{}
function() {}
```

### Example

```javascript
if ("hello") {
  console.log("runs"); // executes
}
```

---

## Boolean Conversion

Using `Boolean()`:

```javascript
Boolean(0);        // false
Boolean("text");   // true
Boolean(null);     // false
Boolean([]);       // true
```

---

## Common Usage

### Conditional Checks

```javascript
let name = "";

if (name) {
  console.log("has value");
} else {
  console.log("empty");
}
```

---

### Default Values

```javascript
let input = "";
let value = input || "default";
```

---
