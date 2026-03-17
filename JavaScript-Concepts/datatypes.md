
## Introduction

In JavaScript, data types define the kind of values that variables can hold and the operations that can be performed on them. Unlike statically typed languages, JavaScript determines data types at runtime, which makes it highly flexible but also prone to subtle bugs if not properly understood.

JavaScript data types are broadly categorized into:

1. Primitive Data Types
2. Non-Primitive (Reference) Data Types

---

## 1. Primitive Data Types

Primitive data types are immutable and stored directly in memory. When assigned or copied, their values are duplicated.

### 1.1 Number

The `Number` type represents both integer and floating-point numbers.

```javascript
let a = 10;
let b = 3.14;
```

Special numeric values:

```javascript
Infinity
-Infinity
NaN // Not a Number
```

Example:

```javascript
console.log(10 / 0); // Infinity
console.log("abc" / 2); // NaN
```

---

### 1.2 String

Strings represent sequences of characters enclosed in single quotes, double quotes, or backticks.

```javascript
let name = "Venu";
let greeting = `Hello, ${name}`;
```

Key features:

* Immutable
* Supports template literals (`` ` ``)

---

### 1.3 Boolean

Represents logical values: `true` or `false`.

```javascript
let isLoggedIn = true;
let hasPermission = false;
```

Commonly used in conditions:

```javascript
if (isLoggedIn) {
  console.log("User logged in");
}
```

---

### 1.4 Undefined

A variable that has been declared but not assigned a value is `undefined`.

```javascript
let x;
console.log(x); // undefined
```

---

### 1.5 Null

Represents an intentional absence of value.

```javascript
let data = null;
```

Note:

```javascript
typeof null; // "object" (this is a known JavaScript bug)
```

---

### 1.6 BigInt

Used for representing large integers beyond the safe limit of `Number`.

```javascript
let bigNumber = 123456789012345678901234567890n;
```

---

### 1.7 Symbol

Represents a unique and immutable value, often used as object keys.

```javascript
let id = Symbol("id");
```

Each Symbol is unique:

```javascript
Symbol("id") === Symbol("id"); // false
```

---

## 2. Non-Primitive (Reference) Data Types

Non-primitive types are mutable and stored as references in memory.

### 2.1 Object

Objects store collections of key-value pairs.

```javascript
let person = {
  name: "Venu",
  age: 22
};
```

Accessing properties:

```javascript
console.log(person.name);
```

---

### 2.2 Array

Arrays are ordered collections of values.

```javascript
let numbers = [1, 2, 3, 4];
let mixed = [1, "hello", true];
```

Access elements:

```javascript
console.log(numbers[0]); // 1
```

---

### 2.3 Function

Functions are first-class objects in JavaScript.

```javascript
function greet() {
  return "Hello";
}
```

Functions can be assigned:

```javascript
let sayHello = greet;
```

---

## 3. Type Checking in JavaScript

### Using `typeof`

```javascript
typeof 10;        // "number"
typeof "hello";   // "string"
typeof true;      // "boolean"
typeof undefined; // "undefined"
typeof null;      // "object"
```

### Checking Arrays

```javascript
Array.isArray([1, 2, 3]); // true
```

---

## 4. Primitive vs Reference Types

| Feature       | Primitive Types | Reference Types  |
| ------------- | --------------- | ---------------- |
| Storage       | Stack           | Heap             |
| Mutability    | Immutable       | Mutable          |
| Copy Behavior | Value copied    | Reference copied |
| Examples      | Number, String  | Object, Array    |

Example:

```javascript
let a = 10;
let b = a;
b = 20;
console.log(a); // 10
```

```javascript
let obj1 = { value: 10 };
let obj2 = obj1;
obj2.value = 20;
console.log(obj1.value); // 20
```

---

## 5. Type Coercion

JavaScript automatically converts types when needed.

### Implicit Coercion

```javascript
"5" + 2; // "52"
"5" - 2; // 3
```

### Explicit Coercion

```javascript
Number("10"); // 10
String(100);  // "100"
Boolean(1);   // true
```

---

## 6. Common Pitfalls

### 6.1 `NaN` Comparison

```javascript
NaN === NaN; // false
```

### 6.2 `null` vs `undefined`

```javascript
null == undefined;  // true
null === undefined; // false
```

### 6.3 Floating Point Precision

```javascript
0.1 + 0.2 === 0.3; // false
```

---
