

# Pass by Value and Pass by Reference in JavaScript

## Overview

JavaScript handles function arguments differently based on the type of data:

* Primitive types are passed by value
* Non-primitive types (objects, arrays) are passed by reference

---

## Pass by Value

A copy of the value is passed to the function. Changes inside the function do not affect the original variable.

```javascript
function updateValue(x) {
  x = x + 10;
}

let a = 5;

updateValue(a);

console.log(a); // 5
```

---

## Pass by Reference

A reference to the original object is passed. Changes inside the function affect the original object.

```javascript
function updateObject(obj) {
  obj.value = 20;
}

let data = { value: 10 };

updateObject(data);

console.log(data.value); // 20
```

---

## Reassignment vs Modification

Reassigning a reference does not affect the original object.

```javascript
function change(obj) {
  obj = { value: 50 };
}

let data = { value: 10 };

change(data);

console.log(data.value); // 10
```

Modifying properties affects the original object.

```javascript
function modify(obj) {
  obj.value = 50;
}

let data = { value: 10 };

modify(data);

console.log(data.value); // 50
```

---

## Array Example

```javascript
function updateArray(arr) {
  arr.push(4);
}

let nums = [1, 2, 3];

updateArray(nums);

console.log(nums); // [1, 2, 3, 4]
```

---
