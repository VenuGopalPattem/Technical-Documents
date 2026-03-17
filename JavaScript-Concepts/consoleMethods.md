

# Console Methods in JavaScript

## Overview

The `console` object provides methods for logging, debugging, and inspecting code execution.

---

## `console.log()`

General purpose logging.

```javascript id="k2p9vx"
console.log("Hello World");
```

---

## `console.error()`

Logs error messages.

```javascript id="m4x7qt"
console.error("Something went wrong");
```

---

## `console.warn()`

Logs warning messages.

```javascript id="r8d1sw"
console.warn("This is a warning");
```

---

## `console.info()`

Logs informational messages.

```javascript id="z6c3yn"
console.info("Information message");
```

---

## `console.table()`

Displays data in table format.

```javascript id="v3n5kp"
const users = [
  { name: "A", age: 20 },
  { name: "B", age: 25 }
];

console.table(users);
```

---

## `console.time()` and `console.timeEnd()`

Measures execution time.

```javascript id="t9w2hj"
console.time("loop");

for (let i = 0; i < 1000000; i++) {}

console.timeEnd("loop");
```

---

## `console.count()`

Counts how many times it is called.

```javascript id="y5q8rm"
console.count("counter");
console.count("counter");
```

---

## `console.clear()`

Clears the console.

```javascript id="p1x4zb"
console.clear();
```

---
