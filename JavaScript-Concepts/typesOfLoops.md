

# Different Types of Loops in JavaScript

## Overview

JavaScript provides multiple looping constructs to iterate over data. Each loop is used based on the type of data and requirement.

---

## for Loop (Numbers / Index-Based)

Used when the number of iterations is known.

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
// 0 1 2 3 4
```

### Array Iteration

```javascript
const arr = [10, 20, 30];

for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```

---

## for...in Loop

Used to iterate over object keys.

```javascript
const obj = {
  name: "Venu",
  age: 22
};

for (let key in obj) {
  console.log(key, obj[key]);
}
```

### Array Usage (Not Recommended)

```javascript
const arr = [1, 2, 3];

for (let index in arr) {
  console.log(index); // "0", "1", "2"
}
```

---

## for...of Loop

Used to iterate over iterable values (arrays, strings).

```javascript
const arr = [10, 20, 30];

for (let value of arr) {
  console.log(value);
}
```

### String Example

```javascript
for (let char of "abc") {
  console.log(char);
}
```

---

## forEach Method

Used with arrays to execute a function for each element.

```javascript
const arr = [1, 2, 3];

arr.forEach(function (value, index) {
  console.log(value, index);
});
```

### Arrow Function

```javascript
arr.forEach((value) => console.log(value));
```

---

## while Loop

Used when the number of iterations is not known in advance.

```javascript
let i = 0;

while (i < 3) {
  console.log(i);
  i++;
}
```

---
