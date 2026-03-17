

# Closures in JavaScript

## Overview

A closure is created when a function retains access to variables from its outer scope even after the outer function has finished execution.

---

## Basic Example

```javascript id="j3k9sl"
function outer() {
  let count = 0;

  function inner() {
    count++;
    return count;
  }

  return inner;
}

const fn = outer();

console.log(fn()); // 1
console.log(fn()); // 2
```

---

## Key Concept

* Inner function remembers variables of outer function
* Outer function execution is completed, but variables are preserved

---

## Practical Use Case

### Data Encapsulation

```javascript id="q7p2dx"
function createCounter() {
  let count = 0;

  return {
    increment: () => ++count,
    decrement: () => --count
  };
}

const counter = createCounter();

console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.decrement()); // 1
```

---

## Function Factory

```javascript id="m8z1wk"
function multiplyBy(x) {
  return function(y) {
    return x * y;
  };
}

const double = multiplyBy(2);

console.log(double(5)); // 10
```

---

## Common Mistake (Loop Closure)

```javascript id="v5n3et"
for (var i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 100);
}

// Output: 3 3 3
```

### Fix with `let`

```javascript id="a2d9fr"
for (let i = 0; i < 3; i++) {
  setTimeout(() => {
    console.log(i);
  }, 100);
}

// Output: 0 1 2
```

---
