

# Scopes in JavaScript

## Overview

Scope defines the accessibility of variables in JavaScript. It determines where variables can be used within a program.

JavaScript uses lexical scoping.

---

## Block Scope

Variables declared with `let` and `const` are limited to the block `{}` in which they are defined.

```javascript
if (true) {
  let a = 10;
  const b = 20;
}

// a and b are not accessible here
```

---

## Function Scope

Variables declared inside a function are accessible only within that function.

```javascript
function test() {
  let x = 5;
  console.log(x);
}

// console.log(x); // Error
```

---

## Lexical Scope

Inner functions can access variables from their outer scope.

```javascript
function outer() {
  let x = 10;

  function inner() {
    console.log(x);
  }

  inner();
}
```

---

## Closure

A closure is formed when a function retains access to its outer scope.

```javascript
function counter() {
  let count = 0;

  return function () {
    count++;
    return count;
  };
}

const c = counter();

c(); // 1
c(); // 2
```

---

## Variable Scope Behavior

### `var`

```javascript
if (true) {
  var x = 10;
}

console.log(x); // 10
```

---

### `let`

```javascript
if (true) {
  let y = 20;
}

// console.log(y); // Error
```

---

### `const`

```javascript
const z = 30;
```

* Cannot be reassigned
* Block scoped

---

## Scope Chain

JavaScript searches for variables in the current scope, then moves to outer scopes.

```javascript
let a = 1;

function first() {
  let b = 2;

  function second() {
    let c = 3;
    console.log(a, b, c);
  }

  second();
}

first();
```

---

## Common Issues

### Loop with `var`

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// 3 3 3
```

### Loop with `let`

```javascript
for (let i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// 0 1 2
```

---
