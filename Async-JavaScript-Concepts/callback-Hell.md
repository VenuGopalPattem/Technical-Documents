# What is Callback Hell

## What it is

Callback hell refers to a situation where multiple asynchronous operations are nested inside each other using callbacks. Each operation depends on the result of the previous one, so each callback is written inside another callback, creating a deeply nested structure.

The code ends up growing horizontally rather than vertically, becoming difficult to read, follow, and maintain.

---

## Why it Happens

When an async operation needs to trigger another async operation after it completes, the only way to do that with callbacks is to nest one inside the other. If there are several such operations chained together, the nesting keeps growing deeper with each step.

---

## The Problems it Causes

**Readability**
Deeply nested code is hard to read. The actual logic gets buried inside layers of indentation.

**Error Handling**
Each callback needs its own error handling. Managing errors across multiple nested callbacks becomes repetitive and inconsistent.

**Maintainability**
Adding, removing, or changing a step in the chain requires touching multiple nested levels, which increases the chance of introducing bugs.

---

## How it was Solved

Callback hell was one of the main reasons Promises were introduced in JavaScript. Promises allowed async operations to be chained in a flat, readable structure instead of being nested. Async/Await took this further by making the code look almost synchronous, eliminating the nesting problem entirely.
