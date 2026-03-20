# How to Create a Promise

## The Promise Constructor

A Promise is created using the `new Promise()` constructor. It takes a single function as an argument. That function is called the **executor function** and it runs immediately when the Promise is created.

The executor function receives two arguments:

**resolve**
A function you call when the operation succeeds. Whatever you pass into it becomes the fulfilled value of the Promise.

**reject**
A function you call when the operation fails. Whatever you pass into it becomes the rejection reason.

---

## Structure

```js
const myPromise = new Promise(function(resolve, reject) {
  // perform some operation
  // call resolve() if it succeeds
  // call reject() if it fails
});
```

---

## Consuming the Promise

Once created, you attach `.then()` to handle the fulfilled value and `.catch()` to handle any rejection.

```js
myPromise
  .then(function(result) {
    // handle success
  })
  .catch(function(error) {
    // handle failure
  });
```

---

## Important Points

- The executor function runs synchronously the moment the Promise is created.
- Only the first call to `resolve` or `reject` takes effect. Any further calls are ignored.
- If an error is thrown inside the executor, the Promise is automatically rejected with that error.
