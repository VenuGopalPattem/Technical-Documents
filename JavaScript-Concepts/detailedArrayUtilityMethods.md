# JavaScript Array Utility Methods

---

## BASICS

### 1. Array.pop()

**What it does:** Removes last element
**Mutable/Immutable:** Mutable

**Syntax:**

```js
arr.pop()
```

**Example:**

```js
let arr = [1,2,3];
arr.pop();
// [1,2]
```

---

### 2. Array.push()

**What it does:** Adds element at end
**Mutable/Immutable:** Mutable

**Syntax:**

```js
arr.push(element)
```

**Example:**

```js
let arr = [1,2];
arr.push(3);
// [1,2,3]
```

---

### 3. Array.concat()

**What it does:** Merges arrays
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr1.concat(arr2)
```

**Example:**

```js
let a = [1,2];
let b = [3,4];
let c = a.concat(b);
// [1,2,3,4]
```

---

### 4. Array.slice()

**What it does:** Extracts portion
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.slice(start, end)
```

**Example:**

```js
let arr = [1,2,3,4];
arr.slice(1,3);
// [2,3]
```

---

### 5. Array.splice()

**What it does:** Insert/remove elements
**Mutable/Immutable:** Mutable

**Syntax:**

```js
arr.splice(start, deleteCount, item)
```

**Example:**

```js
let arr = [1,2,3];
arr.splice(1,1,99);
// [1,99,3]
```

---

### 6. Array.join()

**What it does:** Converts to string
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.join(separator)
```

**Example:**

```js
['a','b','c'].join('-');
// 'a-b-c'
```

---

### 7. Array.flat()

**What it does:** Flattens nested arrays
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.flat(depth)
```

**Example:**

```js
[1,[2,[3]]].flat(2);
// [1,2,3]
```

---

## FINDING METHODS

### 8. Array.find()

**What it does:** First matching value
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.find(callback)
```

**Example:**

```js
[1,2,3].find(x => x > 1);
// 2
```

---

### 9. Array.indexOf()

**What it does:** Finds index
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.indexOf(value)
```

**Example:**

```js
['a','b','c'].indexOf('b');
// 1
```

---

### 10. Array.includes()

**What it does:** Checks existence
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.includes(value)
```

**Example:**

```js
[1,2,3].includes(2);
// true
```

---

### 11. Array.findIndex()

**What it does:** Index via condition
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.findIndex(callback)
```

**Example:**

```js
[10,20,30].findIndex(x => x > 15);
// 1
```

---

## HIGHER ORDER FUNCTIONS

### 12. Array.forEach()

**What it does:** Loop through array
**Mutable/Immutable:** Immutable (but can mutate manually)

**Syntax:**

```js
arr.forEach(callback)
```

**Example:**

```js
[1,2,3].forEach(x => console.log(x));
```

---

### 13. Array.filter()

**What it does:** Filters values
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.filter(callback)
```

**Example:**

```js
[1,2,3,4].filter(x => x % 2 === 0);
// [2,4]
```

---

### 14. Array.map()

**What it does:** Transforms values
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.map(callback)
```

**Example:**

```js
[1,2,3].map(x => x * 2);
// [2,4,6]
```

---

### 15. Array.reduce()

**What it does:** Aggregates to single value
**Mutable/Immutable:** Immutable

**Syntax:**

```js
arr.reduce((acc, curr) => {}, initialValue)
```

**Example:**

```js
[1,2,3].reduce((acc, curr) => acc + curr, 0);
// 6
```

---

### 16. Array.sort()

**What it does:** Sorts array
**Mutable/Immutable:** Mutable

**Syntax:**

```js
arr.sort((a,b) => a - b)
```

**Example:**

```js
[3,1,2].sort((a,b) => a - b);
// [1,2,3]
```

---

## ADVANCED

### 17. Method Chaining

**What it does:** Combine methods

**Syntax:**

```js
arr.method1().method2().method3()
```

**Example:**

```js
[1,2,3,4]
  .filter(x => x % 2 === 0)
  .map(x => x * 10)
  .reduce((acc, curr) => acc + curr, 0);
// 60
```

---

## WHEN TO USE WHAT 

### Use forEach when:

* You just want to iterate
* No return value needed
* Performing side effects (logging, updating variables)

```js
let sum = 0;
[1,2,3].forEach(x => sum += x);
```

---

### Use map when:

* You want to transform data
* Always returns new array

```js
let prices = [100,200];
let discounted = prices.map(p => p * 0.9);
```

---

### Use filter when:

* You want subset based on condition

```js
let users = [18,25,16];
let adults = users.filter(age => age >= 18);
```

---

### Use reduce when:

* You want single output
* Sum, count, grouping, object creation

```js
let total = [10,20,30].reduce((acc,curr) => acc + curr, 0);
```

---

## Golden Rule

* forEach → just loop
* map → transform
* filter → select
* reduce → combine

---

## SUMMARY TABLE

| Method    | Mutable | Purpose     |
| --------- | ------- | ----------- |
| pop       | Yes     | Remove last |
| push      | Yes     | Add end     |
| concat    | No      | Merge       |
| slice     | No      | Copy        |
| splice    | Yes     | Modify      |
| join      | No      | String      |
| flat      | No      | Flatten     |
| find      | No      | First match |
| indexOf   | No      | Index       |
| includes  | No      | Exists      |
| findIndex | No      | Index cond  |
| forEach   | No*     | Loop        |
| filter    | No      | Filter      |
| map       | No      | Transform   |
| reduce    | No      | Aggregate   |
| sort      | Yes     | Sort        |



---
