touch popular

# Popular Array Utility Methods in JavaScript

## Overview

Array methods are used to add, remove, search, and transform data.
They can be **mutable** (modify original array) or **immutable** (return new array).

---

## Basics

### `pop()` — mutable

Removes last element.

```javascript
const arr = [1, 2, 3];
arr.pop();

console.log(arr); // [1, 2]
```

---

### `push()` — mutable

Adds element to end.

```javascript
const arr = [1, 2];
arr.push(3);

console.log(arr); // [1, 2, 3]
```

---

### `concat()` — immutable

Merges arrays.

```javascript
const a = [1, 2];
const b = [3, 4];

const result = a.concat(b);

console.log(result); // [1, 2, 3, 4]
```

---

### `slice()` — immutable

Returns portion of array.

```javascript
const arr = [1, 2, 3, 4];

const result = arr.slice(1, 3);

console.log(result); // [2, 3]
```

---

### `splice()` — mutable

Adds/removes elements.

```javascript
const arr = [1, 2, 3];

arr.splice(1, 1);

console.log(arr); // [1, 3]
```

---

### `join()` — immutable

Converts array to string.

```javascript
const arr = ["a", "b", "c"];

const result = arr.join("-");

console.log(result); // "a-b-c"
```

---

### `flat()` — immutable

Flattens nested arrays.

```javascript
const arr = [1, [2, 3], [4]];

const result = arr.flat();

console.log(result); // [1, 2, 3, 4]
```

---

## Finding

### `find()` — immutable

Returns first matching element.

```javascript
const arr = [1, 2, 3];

const result = arr.find(x => x > 1);

console.log(result); // 2
```

---

### `indexOf()` — immutable

Returns index of value.

```javascript
const arr = [1, 2, 3];

console.log(arr.indexOf(2)); // 1
```

---

### `includes()` — immutable

Checks if value exists.

```javascript
const arr = [1, 2, 3];

console.log(arr.includes(2)); // true
```

---

### `findIndex()` — immutable

Returns index of matching element.

```javascript
const arr = [1, 2, 3];

const index = arr.findIndex(x => x > 1);

console.log(index); // 1
```

---

## Higher Order Functions

### `forEach()` — mutable (no return)

Executes function for each element.

```javascript
const arr = [1, 2, 3];

arr.forEach(x => console.log(x));
```

---

### `filter()` — immutable

Returns filtered array.

```javascript
const arr = [1, 2, 3];

const result = arr.filter(x => x > 1);

console.log(result); // [2, 3]
```

---

### `map()` — immutable

Transforms array.

```javascript
const arr = [1, 2, 3];

const result = arr.map(x => x * 2);

console.log(result); // [2, 4, 6]
```

---

### `reduce()` — immutable

Reduces array to single value.

```javascript
const arr = [1, 2, 3];

const sum = arr.reduce((acc, curr) => acc + curr, 0);

console.log(sum); // 6
```

---

### `sort()` — mutable

Sorts array.

```javascript
const arr = [3, 1, 2];

arr.sort();

console.log(arr); // [1, 2, 3]
```

---

## Advanced

### Method Chaining — immutable flow

```javascript
const arr = [1, 2, 3, 4];

const result = arr
  .filter(x => x > 2)
  .map(x => x * 2);

console.log(result); // [6, 8]
```

---
