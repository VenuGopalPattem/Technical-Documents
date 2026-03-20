# How to Consume Multiple Promises by Chaining

## The Idea

When you have multiple async operations that depend on each other — where the output of one is the input of the next — you chain them using `.then()`. Each step waits for the previous one to complete before running.

---

## How it Works

If a `.then()` handler returns a Promise, the next `.then()` in the chain waits for that Promise to settle before it runs. This is what makes sequential async operations possible without nesting.

---

## Structure

```js
firstPromise
  .then(function(result) {
    return secondPromise(result); // returns a new Promise
  })
  .then(function(result) {
    return thirdPromise(result); // returns another Promise
  })
  .then(function(finalResult) {
    // work with the final result
  })
  .catch(function(error) {
    // handles any error from any step above
  });
```

---

## Key Points

- Each `.then()` must return the next Promise for the chain to wait on it properly.
- If a `.then()` returns a plain value instead of a Promise, the next step receives that value immediately without waiting.
- The operations run in sequence — one after another, not at the same time.
- If any step rejects or throws, the remaining steps are skipped and the nearest `.catch()` handles the error.

---

## When Chaining is Not the Right Tool

Chaining is suited for operations that depend on each other sequentially. If the operations are independent and can run at the same time, `Promise.all()` is a better approach as it runs them in parallel and waits for all of them to complete.
