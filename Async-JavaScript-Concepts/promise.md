# What is a Promise

## The Idea

A Promise is an object that represents the eventual result of an asynchronous operation. Instead of passing a callback into a function and hoping it gets called correctly, the function returns a Promise object. You then attach your own logic to that object.

This puts the control back with you rather than with the function you called.

---

## States of a Promise

A Promise is always in one of three states:

**Pending**
The operation has started but has not completed yet.

**Fulfilled**
The operation completed successfully. A result value is available.

**Rejected**
The operation failed. A reason or error is available.

Once a Promise moves from pending to either fulfilled or rejected, it cannot change its state again.

---

## Handling a Promise

A Promise exposes two methods to handle its outcome:

**.then()**
Called when the Promise is fulfilled. Receives the result value.

**.catch()**
Called when the Promise is rejected. Receives the error or reason for failure.

These methods can be chained, which keeps the code flat and readable compared to nested callbacks.

---

## Promise Chaining

Each `.then()` returns a new Promise. This means you can chain multiple `.then()` calls one after another, where each step receives the result of the previous one. This is how Promises solve the nesting problem of callback hell.

---

## Key Guarantees

Unlike raw callbacks, a Promise guarantees:

- It will resolve or reject only once.
- It will always call `.then()` or `.catch()` asynchronously, never synchronously.
- Errors can be caught in a single `.catch()` at the end of a chain rather than handling them at every step.
