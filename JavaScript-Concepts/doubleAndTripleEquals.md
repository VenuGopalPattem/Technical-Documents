

# Difference Between `==` and `===` in JavaScript

## Overview

`==` and `===` are comparison operators used to check equality. They differ in how they handle type conversion.

---

## `==` (Loose Equality)

Compares values after type conversion.

```javascript
console.log(5 == "5");   // true
console.log(0 == false); // true
console.log(null == undefined); // true
```

### Characteristics

* Performs type coercion
* Can give unexpected results

---

## `===` (Strict Equality)

Compares values without type conversion.

```javascript
console.log(5 === "5");   // false
console.log(0 === false); // false
console.log(null === undefined); // false
```

### Characteristics

* No type coercion
* Safer and predictable

---

## Comparison

| Feature         | `==`  | `===`  |
| --------------- | ----- | ------ |
| Type Conversion | Yes   | No     |
| Strictness      | Loose | Strict |
| Predictability  | Low   | High   |

---
