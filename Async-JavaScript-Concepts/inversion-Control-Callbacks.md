# Inversion of Control in Callbacks

## What it Means

Inversion of control is a trust problem that comes with using callbacks.

When you pass a callback to another function — especially a third-party function — you are handing over control of when and how your code runs. You are no longer in charge of that decision. The function you passed your callback to is.

---

## Why it is a Problem

When you give your callback to an external function, you are trusting that it will:

- Call your callback at the right time
- Call it only once
- Call it with the correct arguments
- Not swallow errors silently

You have no guarantee of any of this. The external function could call your callback too early, too late, multiple times, or not at all. You cannot enforce the correct behavior from the outside.

---

## The Core Issue

Your code's behavior is now dependent on how well someone else's code behaves. This is what inversion of control means — the control over your own logic has been inverted and given to an external piece of code.

This becomes a real concern when working with third-party libraries or APIs where you cannot see or verify the internal implementation.

---

## How Promises Address This

Promises were designed with this problem in mind. Instead of passing your callback directly into another function, a Promise gives you an object back. You attach your logic to that object yourself, on your own terms.

This puts the control back in your hands. You decide what happens when the operation succeeds or fails, and the Promise specification enforces consistent behavior regardless of who wrote the underlying code.