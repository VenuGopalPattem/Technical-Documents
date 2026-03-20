# How JavaScript Executes Code

## What is a JavaScript Engine

JavaScript cannot run on its own. It needs a JavaScript engine to read and run the code. The engine is a program built into the browser or runtime. V8 is the engine used in Chrome and Node.js.

---

## Execution Context

Whenever JavaScript runs any code, it creates an **Execution Context**. This is the environment in which the code runs.

There are two types:

- **Global Execution Context** — created once when the script loads. Everything outside a function runs here.
- **Function Execution Context** — created every time a function is called.

---

## Two Phases of Execution

Every execution context goes through two phases:

**1. Creation Phase**
The engine scans the code before running it. It registers all variable and function declarations in memory. This is why functions and variables are available before the line they are written on — this behavior is called **hoisting**.

**2. Execution Phase**
The engine runs the code line by line, assigns values, and calls functions.

---

## The Call Stack

JavaScript uses a **call stack** to keep track of execution contexts.

When a function is called, its context is pushed onto the stack. When the function finishes, it is popped off. The global context sits at the bottom and is removed only when the program ends.

---

## Scope Chain

Each execution context has access to its own variables. If a variable is not found locally, JavaScript looks in the outer scope. This lookup chain is called the **scope chain**. It ends at the global context.

---
