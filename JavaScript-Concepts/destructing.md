

# Destructuring in JavaScript

## Overview

Destructuring is used to extract values from arrays or objects into variables in a concise way.

---

## Array Destructuring

```javascript id="z7k2dp"
const arr = [1, 2, 3];

const [a, b, c] = arr;

console.log(a, b, c); // 1 2 3
```

---

## Skipping Values

```javascript id="p1x9fw"
const arr = [1, 2, 3];

const [a, , c] = arr;

console.log(a, c); // 1 3
```

---

## Default Values

```javascript id="t6r4mz"
const arr = [1];

const [a, b = 10] = arr;

console.log(a, b); // 1 10
```

---

## Object Destructuring

```javascript id="n8q3ls"
const user = { name: "Venu", age: 22 };

const { name, age } = user;

console.log(name, age);
```

---

## Renaming Variables

```javascript id="g2v8yd"
const user = { name: "Venu" };

const { name: userName } = user;

console.log(userName);
```

---

## Default Values in Objects

```javascript id="d9k1hf"
const user = { name: "Venu" };

const { name, age = 18 } = user;

console.log(name, age);
```

---

## Nested Destructuring

```javascript id="w4m7qb"
const user = {
  name: "Venu",
  address: { city: "Bangalore" }
};

const { address: { city } } = user;

console.log(city);
```

---

## Function Parameters

```javascript id="k3p9ax"
function greet({ name }) {
  console.log(`Hello ${name}`);
}

greet({ name: "Venu" });
```

---
