

# Mutable and Immutable Methods in JavaScript

## Overview

Methods in JavaScript can either modify the original data (**mutable**) or return a new value without changing the original (**immutable**).

---

## Mutable Methods

Modify the original data.

### Array Examples

```javascript
const arr = [1, 2, 3];

arr.push(4);
console.log(arr); // [1, 2, 3, 4]
```

```javascript
const arr = [1, 2, 3];

arr.pop();
console.log(arr); // [1, 2]
```

```javascript
const arr = [3, 1, 2];

arr.sort();
console.log(arr); // [1, 2, 3]
```

```javascript
const arr = [1, 2, 3];

arr.splice(1, 1);
console.log(arr); // [1, 3]
```

---

### Object Example

```javascript
const obj = { a: 1 };

obj.a = 2;

console.log(obj); // { a: 2 }
```

---

## Immutable Methods

Do not modify the original data. Return new values.

### Array Examples

```javascript
const arr = [1, 2, 3];

const result = arr.concat([4]);

console.log(result); // [1, 2, 3, 4]
console.log(arr);    // [1, 2, 3]
```

```javascript
const arr = [1, 2, 3];

const result = arr.slice(1);

console.log(result); // [2, 3]
```

```javascript
const arr = [1, 2, 3];

const result = arr.map(x => x * 2);

console.log(result); // [2, 4, 6]
```

---

### String Example (Always Immutable)

```javascript
const str = "hello";

const result = str.toUpperCase();

console.log(result); // "HELLO"
console.log(str);    // "hello"
```

---

### Object Copy (Immutable Pattern)

```javascript
const obj = { a: 1 };

const updated = { ...obj, a: 2 };

console.log(updated); // { a: 2 }
console.log(obj);     // { a: 1 }
```

---
