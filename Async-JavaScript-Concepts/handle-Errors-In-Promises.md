# How to Handle Errors in a Promise Chain Using .catch

## How Errors Propagate

When a Promise is rejected or an error is thrown inside a `.then()` handler, the error skips all remaining `.then()` steps in the chain and travels down until it finds a `.catch()`. This is similar to how a try/catch block works in synchronous code.

---

## Where to Place .catch()

A single `.catch()` at the end of the chain is enough to catch any rejection or thrown error from any step above it.

```js
somePromise
  .then(function(result) {
    return doSomething(result);
  })
  .then(function(value) {
    return doSomethingElse(value);
  })
  .catch(function(error) {
    // handles any error from any step above
  });
```

---

## Catching at a Specific Step

You can also place a `.catch()` in the middle of a chain if you want to handle an error at a specific point and allow the chain to continue after that.

```js
somePromise
  .then(function(result) {
    return doSomething(result);
  })
  .catch(function(error) {
    // handle this specific error and recover
    return fallbackValue;
  })
  .then(function(value) {
    // chain continues with fallbackValue
  });
```

---

## Key Points

- If no `.catch()` is present and a Promise rejects, the error goes unhandled.
- A `.catch()` itself returns a Promise, so the chain can continue after it if needed.
- If you return a value inside `.catch()`, the next `.then()` in the chain receives that value as if nothing went wrong.
- If you throw inside `.catch()`, the error continues propagating down the chain.
