# How to Chain Promises Using .then

## The Idea

Every `.then()` call returns a new Promise. This means you can attach another `.then()` to it, and another after that, forming a chain. Each step in the chain receives the value returned by the previous one.

This is how you handle a sequence of async operations without nesting them inside each other.

---

## How the Chain Flows

When a `.then()` handler returns a value, that value becomes the input to the next `.then()` in the chain.

If a `.then()` handler returns a Promise, the chain waits for that Promise to settle before moving to the next step.

---

## Structure

```js
somePromise
  .then(function(result) {
    // do something with result
    return newValue; // passed to the next .then()
  })
  .then(function(newValue) {
    // do something with newValue
    return anotherValue;
  })
  .then(function(anotherValue) {
    // final step
  })
  .catch(function(error) {
    // catches any error from any step above
  });
```

---

## Key Points

- Each `.then()` must return a value or a Promise for the chain to work correctly.
- If nothing is returned, the next `.then()` receives `undefined`.
- A single `.catch()` at the end handles rejections from any step in the chain.
- The chain runs sequentially — each step waits for the previous one to complete.
