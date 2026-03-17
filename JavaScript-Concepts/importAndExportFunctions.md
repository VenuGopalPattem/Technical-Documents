
# Importing and Exporting Modules in JavaScript (CommonJS)

## Overview

CommonJS modules use `require` and `module.exports` to share code between files. This is commonly used in Node.js.

---

## Exporting from a File

### Export Single Value

```javascript id="a7k2qp"
// math.js
function add(a, b) {
  return a + b;
}

module.exports = add;
```

---

### Export Multiple Values

```javascript id="n5x8rt"
// math.js
function add(a, b) {
  return a + b;
}

function sub(a, b) {
  return a - b;
}

module.exports = { add, sub };
```

---

## Importing in Another File

### Import Single Export

```javascript id="q3w9ls"
// app.js
const add = require("./math");

console.log(add(2, 3)); // 5
```

---

### Import Multiple Exports

```javascript id="d1v6mz"
// app.js
const { add, sub } = require("./math");

console.log(add(5, 2)); // 7
console.log(sub(5, 2)); // 3
```

---

## Exporting with `exports`

```javascript id="p8k4yx"
// math.js
exports.add = (a, b) => a + b;
exports.sub = (a, b) => a - b;
```

---

## Important Points

* `module.exports` defines what is exported
* `require()` imports the module
* File path must be correct (`./` for local files)
* `exports` is a shortcut for `module.exports`

---
