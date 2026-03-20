# How to Consume Multiple Promises Using Promise.all

## The Idea

`Promise.all()` is used when you have multiple independent async operations that can run at the same time. Instead of waiting for each one to finish before starting the next, all of them run in parallel. `Promise.all()` waits for every Promise in the group to settle before moving forward.

---

## How it Works

You pass an array of Promises to `Promise.all()`. It returns a single Promise that:

- Fulfills when every Promise in the array has fulfilled. The result is an array of all the resolved values, in the same order as the input.
- Rejects as soon as any one Promise in the array rejects. The rejection reason is the error from that one failed Promise.

---

## Structure

```js
Promise.all([firstPromise, secondPromise, thirdPromise])
  .then(function(results) {
    // results is an array: [firstResult, secondResult, thirdResult]
  })
  .catch(function(error) {
    // called if any one of the promises rejects
  });
```

---

## Key Points

- The order of results in the array matches the order of the input Promises, not the order in which they completed.
- If even one Promise rejects, the entire `Promise.all()` rejects immediately. The other Promises still run to completion, but their results are ignored.
- It is best suited for independent operations where all results are needed before proceeding.
