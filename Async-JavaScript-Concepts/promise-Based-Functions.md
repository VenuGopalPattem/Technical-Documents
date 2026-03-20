# Promise Static Methods

## Promise.resolve

Creates a Promise that is already fulfilled with a given value. Useful when you need to return a Promise from a function but already have the value synchronously.

```js
Promise.resolve(42)
  .then(function(value) {
    console.log(value); // 42
  });
```

---

## Promise.reject

Creates a Promise that is already rejected with a given reason. Useful for returning a failed Promise immediately without performing any async operation.

```js
Promise.reject(new Error("something failed"))
  .catch(function(error) {
    console.log(error.message);
  });
```

---

## Promise.all

Takes an array of Promises and returns a single Promise that fulfills when all of them fulfill. If any one rejects, the whole thing rejects immediately.

Use it when all results are needed and the operations are independent of each other.

```js
Promise.all([p1, p2, p3])
  .then(function(results) {
    // results is an array of all resolved values
  })
  .catch(function(error) {
    // called if any one rejects
  });
```

---

## Promise.allSettled

Takes an array of Promises and waits for all of them to settle — fulfilled or rejected. It never rejects. Each result in the returned array includes a `status` field with either `"fulfilled"` or `"rejected"`, along with the value or reason.

Use it when you need the outcome of every Promise regardless of whether some fail.

```js
Promise.allSettled([p1, p2, p3])
  .then(function(results) {
    results.forEach(function(result) {
      console.log(result.status, result.value || result.reason);
    });
  });
```

---

## Promise.any

Takes an array of Promises and fulfills as soon as any one of them fulfills. It ignores rejections unless all of them reject, in which case it rejects with an `AggregateError`.

Use it when you only need one success and do not care which one.

```js
Promise.any([p1, p2, p3])
  .then(function(result) {
    // first fulfilled value
  })
  .catch(function(error) {
    // only if all rejected
  });
```

---

## Promise.race

Takes an array of Promises and settles as soon as the first one settles — fulfilled or rejected. Whatever the first Promise does, that becomes the outcome of `Promise.race()`.

Use it when you only care about the fastest result.

```js
Promise.race([p1, p2, p3])
  .then(function(result) {
    // result of the first settled Promise
  })
  .catch(function(error) {
    // if the first settled Promise rejected
  });
```
