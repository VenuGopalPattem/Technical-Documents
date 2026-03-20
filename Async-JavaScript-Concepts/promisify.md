# How to Promisify an Asynchronous Callback-Based Function

## What Promisification Means

Promisification is the process of wrapping a callback-based async function inside a Promise. The goal is to convert the older callback pattern into a Promise so it can be used with `.then()`, `.catch()`, and `async/await`.

---

## The Pattern

You wrap the callback-based function inside a `new Promise()`. Inside the executor, you call the original function and use its callback to either resolve or reject the Promise.

```js
function delay(ms) {
  return new Promise(function(resolve) {
    setTimeout(resolve, ms);
  });
}
```

For functions that can fail, you also handle the error case:

```js
function readFile(path) {
  return new Promise(function(resolve, reject) {
    fs.readFile(path, 'utf8', function(error, data) {
      if (error) {
        reject(error);
      } else {
        resolve(data);
      }
    });
  });
}
```

---

## The Standard Callback Convention

Most built-in Node.js async functions follow a convention where the callback receives two arguments — the error first, then the result. This is called the **error-first callback** pattern. When promisifying, you check the first argument and reject if it exists, otherwise resolve with the result.

---

## util.promisify in Node.js

Node.js provides a built-in utility called `util.promisify` that automatically wraps any error-first callback-based function into a Promise-returning function, without writing the wrapper manually.

```js
const { promisify } = require('util');
const readFile = promisify(fs.readFile);
```

---

## Key Point

Promisification is a bridge between old callback-based APIs and modern Promise-based code. It lets you use older functions in a consistent way alongside newer async patterns.
