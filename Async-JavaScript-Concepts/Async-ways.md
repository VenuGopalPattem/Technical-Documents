# Ways to Write Asynchronous Code in JavaScript

## Callbacks

A callback is a function passed as an argument to another function, to be called once the task is done.

It was the original way to handle async operations in JavaScript. The problem with callbacks is that they become hard to read and manage when multiple async operations depend on each other. This is commonly referred to as **callback hell**.

---

## Promises

A Promise is an object that represents the eventual result of an async operation. It can be in one of three states:

- **Pending** — the operation is still in progress.
- **Fulfilled** — the operation completed successfully.
- **Rejected** — the operation failed.

Promises made the code more readable compared to callbacks and gave a structured way to handle success and failure cases.

---

## Async / Await

Async/Await is syntax built on top of Promises. It allows asynchronous code to be written in a way that looks synchronous, which makes it easier to read and reason about.

A function marked with `async` always returns a Promise. The `await` keyword pauses the execution inside that function until the Promise resolves.

This is the most commonly used approach in modern JavaScript.

---

## Event Listeners

Event listeners are also a form of asynchronous programming. The code inside an event listener does not run immediately — it runs only when the specified event occurs, such as a button click or a network response.

---

## setTimeout and setInterval

These are browser-provided functions that schedule code to run after a delay or at repeated intervals. They do not block the main thread — they hand the task off and the code runs later through the event loop.
