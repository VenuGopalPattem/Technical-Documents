# States of a Promise

## Overview

Every Promise has an internal state that reflects the current status of the async operation it represents. A Promise will always be in one of three states at any given point.

---

## Pending

This is the initial state. The operation has been started but has not yet completed. The Promise has no result or error yet.

A Promise stays in this state until it is either resolved or rejected.

---

## Fulfilled

The operation completed successfully. The Promise now holds a result value. At this point, any `.then()` handler attached to it will be called with that value.

---

## Rejected

The operation failed. The Promise now holds a reason for the failure, typically an error. At this point, any `.catch()` handler attached to it will be called with that reason.

---

## Key Rules

- A Promise starts in **pending** and moves to either **fulfilled** or **rejected**.
- Once it moves out of pending, the state is final. It cannot change again.
- A Promise that has settled — either fulfilled or rejected — is said to be **resolved**.

---

## Settled vs Resolved

These two terms are often confused.

**Settled** means the Promise has finished — it is either fulfilled or rejected. It is no longer pending.

**Resolved** is a broader term. A Promise is resolved when its outcome has been determined, which includes being fulfilled, rejected, or even locked in to follow another Promise.
