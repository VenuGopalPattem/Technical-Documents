
# Passing Functions to Other Functions in JavaScript

## Overview

Functions in JavaScript are first-class citizens. They can be passed as arguments to other functions and executed when needed.

---

## Basic Example

```javascript id="k2x9pl"
function greet() {
  console.log("Hello");
}

function execute(fn) {
  fn();
}

execute(greet);
```

---

## Passing with Parameters

```javascript id="m7q4dx"
function add(a, b) {
  return a + b;
}

function calculate(fn, x, y) {
  return fn(x, y);
}

console.log(calculate(add, 2, 3)); // 5
```

---

## Anonymous Function

```javascript id="r5n8ty"
function execute(fn) {
  fn();
}

execute(function () {
  console.log("Running function");
});
```

---

## Arrow Function

```javascript id="p3v1ks"
function execute(fn) {
  fn();
}

execute(() => console.log("Arrow function"));
```

---

## Delayed Execution

```javascript id="x9c2zw"
setTimeout(() => {
  console.log("Executed later");
}, 1000);
```

---

## Conditional Invocation

```javascript id="t6b4qa"
function run(condition, fn) {
  if (condition) {
    fn();
  }
}

run(true, () => console.log("Executed"));
```

---
