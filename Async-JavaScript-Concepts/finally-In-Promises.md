# The Finally Block in a Promise Chain

## What it Does

`.finally()` is a method you can attach to a Promise chain that runs regardless of whether the Promise was fulfilled or rejected. It does not care about the outcome — it always executes.

---

## Common Use Cases

It is typically used for cleanup work that needs to happen either way, such as:

- Hiding a loading spinner after a request completes
- Closing a database connection
- Re-enabling a button after a form submission

---

## Structure

```js
somePromise
  .then(function(result) {
    // handle success
  })
  .catch(function(error) {
    // handle failure
  })
  .finally(function() {
    // always runs, no arguments received
  });
```

---

## Key Points

- `.finally()` does not receive any argument. It has no access to the resolved value or the rejection reason.
- It does not modify the value passing through the chain. The original fulfilled value or rejection reason continues to the next handler after `.finally()`.
- If `.finally()` throws an error or returns a rejected Promise, that error propagates and overrides the original outcome.
