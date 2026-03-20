# Synchronous vs Asynchronous in JavaScript

## Synchronous

Synchronous code runs line by line. Each line waits for the previous one to finish before moving forward. If one operation takes time, everything else is blocked until it completes.

This is the default behavior of JavaScript.

---

## Asynchronous

Asynchronous code does not wait. When an operation takes time — like fetching data from a server or reading a file — JavaScript moves on to the next line and comes back to handle the result once it is ready.

This prevents the program from getting blocked on slow operations.

---

## Why This Matters

JavaScript is single-threaded. It can only do one thing at a time. Without asynchronous behavior, any slow operation would freeze the entire program.

Asynchronous programming is how JavaScript handles tasks that take an unknown amount of time without stopping everything else.

---

## How Async Works in JavaScript

JavaScript handles asynchronous operations through:

- **Callbacks** — a function passed in to be called later once the task finishes.
- **Promises** — an object that represents a value which will be available in the future.
- **Async/Await** — a cleaner syntax built on top of Promises.

These are just different ways to write and manage asynchronous code. The underlying mechanism is the **Event Loop**, which checks if the call stack is empty and then processes pending async tasks.

---
