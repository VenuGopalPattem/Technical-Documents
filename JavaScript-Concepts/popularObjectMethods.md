
# Popular Object Utility Methods in JavaScript

## Overview

Object methods are used to access, modify, and transform object data.
Some methods are **mutable** (modify the original object), while others are **immutable** (return new values).

---

## Basics

### `Object.keys()` — immutable

Returns array of keys.

```javascript
const obj = { a: 1, b: 2 };

const keys = Object.keys(obj);

console.log(keys); // ["a", "b"]
```

---

### `Object.values()` — immutable

Returns array of values.

```javascript
const obj = { a: 1, b: 2 };

const values = Object.values(obj);

console.log(values); // [1, 2]
```

---

### `Object.entries()` — immutable

Returns array of `[key, value]` pairs.

```javascript
const obj = { a: 1, b: 2 };

const entries = Object.entries(obj);

console.log(entries); // [["a", 1], ["b", 2]]
```

---

## Conversion

### `Object.fromEntries()` — immutable

Converts entries back to object.

```javascript
const entries = [["a", 1], ["b", 2]];

const obj = Object.fromEntries(entries);

console.log(obj); // { a: 1, b: 2 }
```

---

## Copying and Merging

### `Object.assign()` — mutable

Copies properties to target object.

```javascript
const target = { a: 1 };
const source = { b: 2 };

Object.assign(target, source);

console.log(target); // { a: 1, b: 2 }
```

---

### Spread Operator `{...}` — immutable

Creates a shallow copy.

```javascript
const obj1 = { a: 1 };
const obj2 = { b: 2 };

const result = { ...obj1, ...obj2 };

console.log(result); // { a: 1, b: 2 }
```

---

## Property Checks

### `hasOwnProperty()` — immutable

Checks if key exists.

```javascript
const obj = { a: 1 };

console.log(obj.hasOwnProperty("a")); // true
```

---

### `in` operator — immutable

Checks key in object (including prototype).

```javascript
const obj = { a: 1 };

console.log("a" in obj); // true
```

---

## Object Freezing / Sealing

### `Object.freeze()` — mutable (locks object)

Prevents changes.

```javascript
const obj = { a: 1 };

Object.freeze(obj);

// obj.a = 2; // ignored

console.log(obj.a); // 1
```

---

### `Object.seal()` — mutable

Prevents adding/removing properties.

```javascript
const obj = { a: 1 };

Object.seal(obj);

// obj.b = 2; // not allowed
obj.a = 5;   // allowed

console.log(obj); // { a: 5 }
```

---


