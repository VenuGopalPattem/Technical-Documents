# What is the Event Loop

## The Problem it Solves

JavaScript is single-threaded, meaning it can only execute one task at a time. But in practice, JavaScript handles timers, network requests, and user interactions without freezing. The event loop is the mechanism that makes this possible.

---

## Components Involved

**Call Stack**
Where JavaScript executes code. Functions are pushed onto the stack when called and popped off when they return.

**Web APIs**
When an async task is triggered — like a timer or a fetch request — it is handed off to the browser to handle. JavaScript does not wait for it.

**Callback Queue**
Once an async task completes, its callback is placed in the callback queue, waiting to be executed.

**Microtask Queue**
Promises use a separate queue called the microtask queue. It has higher priority than the callback queue.

---

## How the Event Loop Works

The event loop has one job — it constantly checks if the call stack is empty. If it is, it picks up the next task from the queues and pushes it onto the stack.

The order of priority is:

1. The call stack is cleared first.
2. The microtask queue is processed next (Promises).
3. The callback queue is processed after that (setTimeout, setInterval, etc).

This cycle repeats continuously as long as the program is running.

---

## Key Point

The event loop is not part of JavaScript itself. It is part of the browser runtime. JavaScript just uses it. This is what allows a single-threaded language to handle asynchronous operations without blocking.
