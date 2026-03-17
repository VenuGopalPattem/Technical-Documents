# Different Ways of Declaring a Function in JavaScript

## Overview

JavaScript provides multiple ways to declare functions. Each form differs in syntax and behavior.

---

## Function Declaration

```javascript
function greet() {
  console.log("Hello");
}
```

* Hoisted
* Can be called before definition

---

## Function Expression

```javascript
const greet = function () {
  console.log("Hello");
};
```

* Not hoisted
* Assigned to a variable

---

## Arrow Function

```javascript
const greet = () => {
  console.log("Hello");
};
```

### With implicit return

```javascript
const add = (a, b) => a + b;
```

---

## Named Function Expression

```javascript
const greet = function sayHello() {
  console.log("Hello");
};
```

* Name is local to the function body

---

## Immediately Invoked Function Expression (IIFE)

```javascript
(function () {
  console.log("Runs immediately");
})();
```

---

## Function Constructor

```javascript
const add = new Function("a", "b", "return a + b");
```

---

## Method in Object

```javascript
const obj = {
  greet: function () {
    console.log("Hello");
  }
};
```

### Shorthand method

```javascript
const obj = {
  greet() {
    console.log("Hello");
  }
};
```

---

## Class Method

```javascript
class Person {
  greet() {
    console.log("Hello");
  }
}
```

---
