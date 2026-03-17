
# Function Hoisting in JavaScript

## Overview

Hoisting in JavaScript is the behavior where function declarations are moved to the top of their scope during execution. This allows functions to be called before they are defined in the code.

---

## Function Declaration Hoisting

Function declarations are fully hoisted.

```javascript
greet();

function greet() {
  console.log("Hello");
}
```

---

## Function Expression (Not Hoisted)

Function expressions are not hoisted in the same way.

```javascript
// greet(); // Error

var greet = function () {
  console.log("Hello");
};
```

---

## Behavior with `var`

Only the variable declaration is hoisted, not the function assignment.

```javascript
console.log(greet); // undefined

// greet(); // Error

var greet = function () {
  console.log("Hello");
};
```

---

## Behavior with `let` and `const`

Variables declared with `let` and `const` are not accessible before initialization.

```javascript
// greet(); // Error

const greet = function () {
  console.log("Hello");
};
```

---

## Named Function Expression

```javascript
const greet = function sayHello() {
  console.log("Hello");
};

// sayHello(); // Error
greet(); // works
```

---
