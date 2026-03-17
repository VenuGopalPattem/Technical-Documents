

# Difference Between Arrow Functions and Regular Functions in JavaScript

## Overview

Arrow functions and regular functions differ in syntax, `this` behavior, and usage.

---

## Syntax

### Regular Function

```javascript id="r3k9qp"
function add(a, b) {
  return a + b;
}
```

### Arrow Function

```javascript id="m8x2lt"
const add = (a, b) => a + b;
```

---

## `this` Behavior

### Regular Function

```javascript id="d7v1az"
const obj = {
  value: 10,
  getValue: function () {
    return this.value;
  }
};

console.log(obj.getValue()); // 10
```

### Arrow Function

```javascript id="c4n6yb"
const obj = {
  value: 10,
  getValue: () => {
    return this.value;
  }
};

console.log(obj.getValue()); // undefined
```

* Regular functions have their own `this`
* Arrow functions inherit `this` from outer scope

---

## Arguments Object

### Regular Function

```javascript id="x5p8dh"
function test() {
  console.log(arguments);
}
```

### Arrow Function

```javascript id="f2k7zs"
const test = () => {
  // arguments is not available
};
```

---

## Constructor Usage

```javascript id="p9q3nv"
// Regular function
function Person(name) {
  this.name = name;
}

const p = new Person("Venu");

// Arrow function (invalid)
// const Person = (name) => {
//   this.name = name;
// };
// new Person("Venu"); // error
```

* Arrow functions cannot be used as constructors

---

## Implicit Return

```javascript id="y1t6mw"
const square = x => x * x;
```

---
