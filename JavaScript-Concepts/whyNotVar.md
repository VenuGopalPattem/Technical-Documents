
# Why We Must Not Use `var` in JavaScript

## Overview

`var` has function scope and behavior that can lead to unintended side effects. Modern JavaScript provides `let` and `const` as safer alternatives.

---

## No Block Scope

`var` ignores block scope and becomes accessible outside `{}`.

```javascript
if (true) {
  var x = 10;
}

console.log(x); // 10
```

---

## Redeclaration Allowed

The same variable can be declared multiple times in the same scope.

```javascript
var a = 10;
var a = 20;

console.log(a); // 20
```

---

## Hoisting with Undefined

`var` is hoisted and initialized with `undefined`.

```javascript
console.log(a); // undefined
var a = 10;
```

---

## Issues in Loops

`var` does not create a new scope per iteration.

```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// 3 3 3
```

---

## Implicit Global Variables

Variables can become global if declared without `var`, `let`, or `const`.

```javascript
function test() {
  x = 10;
}

test();
console.log(x); // 10
```

---

## Function Scope Only

`var` is limited to function scope, not block scope.

```javascript
function test() {
  if (true) {
    var x = 5;
  }

  console.log(x); // 5
}
```

---
