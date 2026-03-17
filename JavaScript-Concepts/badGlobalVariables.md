
# Why Using Global Variables is Bad in JavaScript

## Overview

Global variables are accessible from anywhere in the program. This unrestricted access can lead to unintended side effects, conflicts, and difficult-to-maintain code.

---

## Uncontrolled Access

Any part of the code can read or modify a global variable.

```javascript
let count = 0;

function increment() {
  count++;
}

function reset() {
  count = 0;
}
```

---

## Naming Conflicts

Global variables can be overwritten by other parts of the code.

```javascript
let data = "User Data";

// Somewhere else
let data = "Admin Data"; // conflict
```

---

## Difficult Debugging

Changes to global variables can happen from multiple places, making issues harder to trace.

```javascript
let status = "active";

function update() {
  status = "inactive";
}
```

---

## Tight Coupling

Functions become dependent on external variables instead of inputs.

```javascript
let value = 10;

function calculate() {
  return value * 2;
}
```

---

## Reduced Reusability

Functions using global variables cannot be reused easily.

```javascript
let tax = 5;

function total(price) {
  return price + tax;
}
```

---

## Accidental Modification

Values can be changed unintentionally.

```javascript
let config = { mode: "dark" };

function change() {
  config.mode = "light";
}
```

---
