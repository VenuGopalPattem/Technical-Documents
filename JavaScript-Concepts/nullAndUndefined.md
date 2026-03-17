
# Difference Between `null` and `undefined` in JavaScript

## Overview

`null` and `undefined` both represent absence of value, but they are used in different contexts.

---

## `undefined`

A variable that is declared but not assigned a value.

```javascript id="j4k8wp"
let a;

console.log(a); // undefined
```

### Cases

* Variable declared but not initialized
* Function without return
* Missing function arguments
* Non-existing object properties

---

## `null`

An intentional assignment representing no value.

```javascript id="x7p2ds"
let a = null;

console.log(a); // null
```

### Use Case

* Explicitly setting a variable to "no value"

---

## Comparison

| Feature     | `undefined`  | `null`              |
| ----------- | ------------ | ------------------- |
| Type        | undefined    | object              |
| Assigned by | JavaScript   | Developer           |
| Meaning     | Not assigned | Intentionally empty |

---

## Equality Check

```javascript id="r2m6fz"
console.log(null == undefined);  // true
console.log(null === undefined); // false
```

---

