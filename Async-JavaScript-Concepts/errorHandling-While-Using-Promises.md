# Error Handling When Using Promises

## How Errors Surface in Promises

An error in a Promise chain can come from two places — a Promise that explicitly rejects, or an error thrown inside a `.then()` handler. Both are treated the same way and both travel down the chain looking for a `.catch()`.

---

## Using .catch()

`.catch()` is the primary way to handle errors in a Promise chain. It intercepts any rejection or thrown error from the steps above it.

```js
somePromise
  .then(function(result) {
    return doSomething(result);
  })
  .catch(function(error) {
    // handle the error
  });
```

---

## Recovering From an Error

If you return a value inside `.catch()`, the chain recovers and continues. The next `.then()` after the `.catch()` receives that returned value.

If you want the failure to stop the chain entirely, you can either rethrow the error or return a rejected Promise from inside `.catch()`.

---

## Handling Errors in Promise.all

With `Promise.all()`, if any one Promise rejects, the entire thing rejects immediately. The `.catch()` receives the error from that one failed Promise. There is no built-in way to get the results of the ones that succeeded.

If you need each Promise to always fulfill regardless of failure, `Promise.allSettled()` is a better option — it waits for all Promises to settle and gives you the outcome of each one individually.

---

## Key Points

- Always attach a `.catch()` to every Promise chain.
- A single `.catch()` at the end covers the entire chain above it.
- Errors thrown inside `.then()` are automatically caught by the nearest `.catch()` below.
- An unhandled rejection does not crash the program visibly but produces a warning and can cause silent failures.



# Why Error Handling is the Most Important Part of Using a Promise

## Async Failures are Silent by Default

In synchronous code, an unhandled error throws immediately and stops execution. You notice it right away. With Promises, an unhandled rejection does not stop anything. The program continues running and the failure disappears silently. This makes bugs harder to detect and trace.

---

## The Real World is Unreliable

Promises are almost always used for operations that interact with the outside world — network requests, file reads, database calls. These operations can fail for reasons outside your control: the server is down, the network drops, the data is malformed. Assuming success and not accounting for failure is not realistic.

---

## Unhandled Rejections Cause Hidden Bugs

When a Promise rejects and there is no `.catch()`, the error is swallowed. The feature silently fails, the user sees nothing or gets stuck, and there is no error message pointing to what went wrong. These are among the most frustrating bugs to debug.

---

## A Promise Without Error Handling is Incomplete

Writing a Promise chain without a `.catch()` is essentially writing code that only works in the happy path. It is incomplete by design. Any production-quality code that uses Promises must account for what happens when things go wrong, not just when they go right.

---

## Key Point

The value of a Promise is not just that it handles async operations — it is that it gives you a structured, predictable way to handle both success and failure. Ignoring `.catch()` means using only half of what Promises were built to do.
