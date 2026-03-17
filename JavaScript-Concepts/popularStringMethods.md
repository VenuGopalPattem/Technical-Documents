
# Popular String Utility Methods in JavaScript

## Overview

String methods are used to manipulate and inspect text.
Strings are **immutable** in JavaScript, so all methods return new values without modifying the original string.

---

## Basics

### `length` — immutable

Returns string length.

```javascript
const str = "hello";

console.log(str.length); // 5
```

---

### `toUpperCase()` — immutable

Converts to uppercase.

```javascript
const str = "hello";

const result = str.toUpperCase();

console.log(result); // "HELLO"
```

---

### `toLowerCase()` — immutable

Converts to lowercase.

```javascript
const str = "HELLO";

const result = str.toLowerCase();

console.log(result); // "hello"
```

---

### `trim()` — immutable

Removes whitespace from both ends.

```javascript
const str = "  hello  ";

const result = str.trim();

console.log(result); // "hello"
```

---

## Extraction

### `slice()` — immutable

Extracts part of a string.

```javascript
const str = "hello";

const result = str.slice(1, 4);

console.log(result); // "ell"
```

---

### `substring()` — immutable

Extracts part of a string.

```javascript
const str = "hello";

const result = str.substring(1, 4);

console.log(result); // "ell"
```

---

## Searching

### `includes()` — immutable

Checks if substring exists.

```javascript
const str = "hello";

console.log(str.includes("ell")); // true
```

---

### `indexOf()` — immutable

Returns index of substring.

```javascript
const str = "hello";

console.log(str.indexOf("e")); // 1
```

---

### `startsWith()` — immutable

Checks start of string.

```javascript
const str = "hello";

console.log(str.startsWith("he")); // true
```

---

### `endsWith()` — immutable

Checks end of string.

```javascript
const str = "hello";

console.log(str.endsWith("lo")); // true
```

---

## Modification

### `replace()` — immutable

Replaces first match.

```javascript
const str = "hello world";

const result = str.replace("world", "JS");

console.log(result); // "hello JS"
```

---

### `replaceAll()` — immutable

Replaces all matches.

```javascript
const str = "a-b-c";

const result = str.replaceAll("-", "_");

console.log(result); // "a_b_c"
```

---

## Conversion

### `split()` — immutable

Converts string to array.

```javascript
const str = "a,b,c";

const result = str.split(",");

console.log(result); // ["a", "b", "c"]
```

---

### `join()` (array method)

Used after `split()`.

```javascript
const str = "a,b,c";

const result = str.split(",").join("-");

console.log(result); // "a-b-c"
```

---
