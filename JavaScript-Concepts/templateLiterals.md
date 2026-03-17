
# Template Literals in JavaScript

## Overview

Template literals are string literals defined using backticks (`` ` ``). They allow embedding expressions, multi-line strings, and improved string formatting.

---

## Basic Syntax

```javascript
const str = `Hello World`;
```

---

## String Interpolation

Embed variables or expressions using `${}`.

```javascript
const name = "Venu";

const message = `Hello, ${name}`;

console.log(message); // Hello, Venu
```

---

## Expressions

```javascript
const a = 10;
const b = 20;

const result = `Sum: ${a + b}`;

console.log(result); // Sum: 30
```

---

## Multi-line Strings

```javascript
const text = `Line 1
Line 2
Line 3`;

console.log(text);
```

---

## Function Calls Inside

```javascript
function greet(name) {
  return `Hello, ${name}`;
}

const msg = `${greet("Venu")}`;

console.log(msg); // Hello, Venu
```

---

## Tagged Templates

```javascript
function tag(strings, value) {
  return strings[0] + value.toUpperCase();
}

const name = "venu";

const result = tag`Hello ${name}`;

console.log(result); // Hello VENU
```

---
