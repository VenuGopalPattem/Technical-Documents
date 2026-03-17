

# Why `value === undefined` is Better than `!value` in JavaScript

## Overview

`value === undefined` and `!value` are both used in condition checks, but they behave differently. Using `!value` can lead to incorrect results because it treats multiple values as falsy.

---

## Using `!value`

```javascript
if (!value) {
  console.log("Value is missing");
}
```

### Problem

`!value` is true for all falsy values:

```javascript
false
0
""
null
undefined
NaN
```

### Example

```javascript
let count = 0;

if (!count) {
  console.log("No value"); // runs, but 0 is valid
}
```

---

## Using `value === undefined`

```javascript
if (value === undefined) {
  console.log("Value is undefined");
}
```

### Behavior

* Checks only for `undefined`
* Does not affect valid falsy values

### Example

```javascript
let count = 0;

if (count === undefined) {
  console.log("Missing"); // does NOT run
}
```

---

## Comparison

| Check                 | What it detects  |
| --------------------- | ---------------- |
| `!value`              | All falsy values |
| `value === undefined` | Only `undefined` |

---

## When to Use

* Use `!value` when any falsy value is invalid
* Use `value === undefined` when only missing values should be checked

---

