# What Happens When an Error is Thrown Inside .then With a .catch Present

## The Behavior

If an error is thrown inside a `.then()` handler, the Promise returned by that `.then()` is automatically rejected with that error. The remaining `.then()` steps in the chain are skipped, and the error travels down until it reaches the nearest `.catch()`.

---

## What .catch Receives

The `.catch()` handler receives the error that was thrown, the same way it would receive a rejection from a Promise. From `.catch()`'s perspective, there is no difference between a thrown error and a rejected Promise — both are treated the same way.

---

## Structure

```js
somePromise
  .then(function(result) {
    throw new Error("something went wrong");
  })
  .then(function(value) {
    // this step is skipped entirely
  })
  .catch(function(error) {
    // catches the error thrown above
    console.log(error.message); // "something went wrong"
  });
```

---

## Key Point

This behavior is what makes a single `.catch()` at the end of a chain reliable. It does not just catch rejected Promises — it also catches any errors thrown inside any `.then()` handler above it in the chain.
