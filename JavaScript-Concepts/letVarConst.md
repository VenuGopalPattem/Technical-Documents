

# let, var, const in JavaScript

## Overview

`var`, `let`, and `const` are used to declare variables in JavaScript. They differ in scope, reassignment, and behavior.

---

## var

* Function scoped
* Can be redeclared
* Can be reassigned

```javascript
var x = 10;
var x = 20; // allowed

function test() {
  var y = 5;
}

// y not accessible here
```

### Behavior

```javascript
if (true) {
  var a = 10;
}

console.log(a); // 10
```

---

## let

* Block scoped
* Cannot be redeclared in the same scope
* Can be reassigned

```javascript
let x = 10;
x = 20; // allowed

// let x = 30; // Error
```

### Behavior

```javascript
if (true) {
  let a = 10;
}

// console.log(a); // Error
```

---

## const

* Block scoped
* Cannot be redeclared
* Cannot be reassigned

```javascript
const x = 10;

// x = 20; // Error
```

### Behavior with Objects

```javascript
const obj = { value: 10 };

obj.value = 20; // allowed
```

---

## Hoisting

### var

```javascript
console.log(a); // undefined
var a = 10;
```

---

### let and const

```javascript
// console.log(b); // Error
let b = 10;

// console.log(c); // Error
const c = 20;
```

---

## Temporal Dead Zone

Accessing `let` or `const` before declaration results in an error.

```javascript
// console.log(x); // Error
let x = 5;
```

---

## Differences

| Feature        | var      | let      | const    |
| -------------- | -------- | -------- | -------- |
| Scope          | Function | Block    | Block    |
| Redeclare      | Yes      | No       | No       |
| Reassign       | Yes      | Yes      | No       |
| Hoisting       | Yes      | Yes      | Yes      |
| Initialization | Optional | Optional | Required |

---
