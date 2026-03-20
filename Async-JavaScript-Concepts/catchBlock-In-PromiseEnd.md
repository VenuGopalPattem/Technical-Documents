# Why .catch Must Be Placed Towards the End of a Promise Chain

## The Core Reason

A `.catch()` only catches errors from the steps that come before it in the chain. It has no awareness of anything that comes after it. If you place `.catch()` in the middle of the chain, any error thrown in a `.then()` below it will go unhandled.

---

## What Happens When .catch is in the Middle

```js
somePromise
  .then(function(result) {
    return doSomething(result);
  })
  .catch(function(error) {
    // only catches errors from the .then() above
  })
  .then(function(value) {
    throw new Error("this error is not caught");
    // no .catch() below — this goes unhandled
  });
```

The `.catch()` here only covers the first `.then()`. The error thrown in the second `.then()` has nothing to catch it.

---

## When .catch is at the End

Placing `.catch()` at the end means it covers every `.then()` above it in the chain. A single handler is enough to catch any rejection or thrown error from the entire chain.

```js
somePromise
  .then(function(result) {
    return doSomething(result);
  })
  .then(function(value) {
    return doSomethingElse(value);
  })
  .catch(function(error) {
    // catches errors from any step above
  });
```

---

## Key Point

The position of `.catch()` determines its coverage. Placing it at the end is a convention that ensures no error in the chain goes unhandled, without needing multiple catch handlers scattered across every step.
