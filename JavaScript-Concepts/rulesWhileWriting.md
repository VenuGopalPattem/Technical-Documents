

# JavaScript Best Practices

## Overview

Follow consistent coding practices to improve readability, maintainability, and reduce bugs.

---

## Indentation and Formatting

* Use consistent indentation (2 or 4 spaces)
* Avoid mixing tabs and spaces
* Keep line length reasonable

```javascript id="k3m9xp"
function greet(name) {
  if (name) {
    console.log(`Hello ${name}`);
  }
}
```

---

## Variable Naming

* Use meaningful names
* Use camelCase

```javascript id="v7p2as"
let userName = "Venu";
let totalPrice = 100;
```

---

## Loop Variable Naming

* Use short, clear names for loops
* Use meaningful names when needed

```javascript id="f8q4rd"
for (let i = 0; i < 10; i++) {}

for (let user of users) {
  console.log(user.name);
}
```

---

## Use `const` and `let`

* Prefer `const` by default
* Use `let` when reassignment is needed
* Avoid `var`

```javascript id="n6w1zt"
const PI = 3.14;
let count = 0;
```

---

## Avoid Global Variables

* Keep scope limited
* Use functions or modules

---

## Use Strict Equality

```javascript id="y2d8lc"
if (value === 10) {}
```

---

## Handle Errors Properly

```javascript id="x5c9qp"
try {
  risky();
} catch (error) {
  console.error(error);
}
```

---

## Keep Functions Small

* One responsibility per function

```javascript id="p4k7mz"
function calculateTotal(items) {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

---

## Avoid Code Duplication

* Reuse logic using functions

---

## Use Array Methods

* Prefer `map`, `filter`, `reduce` over manual loops

---

## Write Readable Conditions

```javascript id="z9t3vx"
if (isValidUser) {}
```

---

## Consistent Braces

```javascript id="w1q8bn"
if (condition) {
  doSomething();
}
```

---
