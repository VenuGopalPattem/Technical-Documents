# How to Consume an Existing Promise

## What it Means to Consume a Promise

Consuming a Promise means attaching handlers to it so you can react to its outcome — whether it fulfilled or rejected. You do not create the Promise yourself in this case. You receive it from a function and decide what to do with the result.

---

## .then()

Used to handle a fulfilled Promise. It receives the resolved value as its argument.

```js
promise.then(function(result) {
  // use the result
});
```

---

## .catch()

Used to handle a rejected Promise. It receives the error or rejection reason as its argument.

```js
promise.catch(function(error) {
  // handle the error
});
```

---

## .finally()

Runs regardless of whether the Promise was fulfilled or rejected. It is used for cleanup tasks that need to happen either way, like hiding a loading spinner.

```js
promise.finally(function() {
  // always runs
});
```

---

## Chaining

`.then()`, `.catch()`, and `.finally()` all return a new Promise, which means they can be chained together in a sequence.

```js
promise
  .then(function(result) {
    // handle success
  })
  .catch(function(error) {
    // handle failure
  })
  .finally(function() {
    // runs either way
  });
```

---

## Error Handling in a Chain

A single `.catch()` at the end of a chain will catch any rejection that occurs at any point in the chain above it. You do not need a separate error handler at every step.
