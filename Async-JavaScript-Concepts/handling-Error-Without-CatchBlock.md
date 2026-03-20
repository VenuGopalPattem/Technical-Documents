# What Happens When an Error is Thrown Inside .then With No .catch

## The Behavior

If an error is thrown inside a `.then()` handler and there is no `.catch()` anywhere in the chain, the error has nowhere to go. The Promise is rejected silently and the error goes unhandled.

The rest of your code continues to run as if nothing happened. There is no crash, no visible failure — the error just disappears unless you are specifically looking for it.

---

## Unhandled Promise Rejection

Modern JavaScript environments detect this situation and emit an **unhandled promise rejection** warning.

In browsers, this triggers an `unhandledrejection` event on the window.
In Node.js, it prints a warning to the console and in newer versions can terminate the process entirely.

---

## Why This is Dangerous

Because JavaScript does not crash visibly, unhandled rejections are easy to miss. A feature can silently fail and the user or developer may not notice until much later. This makes debugging harder because there is no clear point of failure.

---

## Structure

```js
somePromise
  .then(function(result) {
    throw new Error("something went wrong");
    // no .catch() below — this error is silently lost
  })
  .then(function(value) {
    // this is skipped
  });
```

---

## Key Point

Always attach a `.catch()` at the end of a Promise chain. Even if you only use it to log the error, it ensures that failures are visible and do not go unnoticed.
