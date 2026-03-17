

# Difference Between Named and Anonymous Functions in JavaScript

## Overview

Functions in JavaScript can be declared with a name (named functions) or without a name (anonymous functions). They differ in readability, reuse, and debugging.

---

## Named Functions

A function with an identifier.

```javascript id="k7p2dx"
function greet() {
  console.log("Hello");
}

greet();
```

### Characteristics

* Has a name
* Can be reused
* Easier to debug (name appears in stack trace)

---

## Anonymous Functions

A function without a name.

```javascript id="m4q9zs"
const greet = function () {
  console.log("Hello");
};

greet();
```

---

## Used as Arguments

```javascript id="t8x3vn"
setTimeout(function () {
  console.log("Executed");
}, 1000);
```

---

## Arrow Function (Anonymous)

```javascript id="p2c6ly"
const greet = () => {
  console.log("Hello");
};
```

---

## Comparison

| Feature     | Named Function | Anonymous Function     |
| ----------- | -------------- | ---------------------- |
| Name        | Yes            | No                     |
| Reusability | High           | Limited                |
| Debugging   | Easier         | Harder                 |
| Usage       | Standalone     | Callbacks, expressions |

---
