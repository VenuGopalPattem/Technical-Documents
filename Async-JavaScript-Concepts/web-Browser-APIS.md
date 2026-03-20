# What are Web Browser APIs

## Overview

JavaScript on its own is a fairly limited language. It can do basic logic, work with data, and manipulate values — but it cannot interact with the browser, make network requests, or access the user's device by itself.

Browser APIs are features provided by the browser that JavaScript can use to do these things. They are not part of the JavaScript language itself. They are built into the browser and exposed to JavaScript so your code can talk to them.

---

## Common Browser APIs

**DOM API**
Allows JavaScript to read and manipulate the structure, content, and styling of a webpage.

**Fetch API**
Used to make network requests — sending and receiving data from a server.

**setTimeout / setInterval**
Schedule code to run after a delay or repeatedly at a set interval.

**localStorage / sessionStorage**
Store data in the browser. localStorage persists even after the tab is closed. sessionStorage is cleared when the session ends.

**Geolocation API**
Provides access to the user's geographic location, with their permission.

**Canvas API**
Used to draw graphics and animations directly in the browser.

**Notification API**
Allows web pages to send notifications to the user's device.

---

## How They Relate to Async

Many browser APIs are asynchronous by nature. When JavaScript calls a browser API — like fetching data or waiting for a timer — the browser handles that task in the background. JavaScript does not wait. Once the task is done, the result is handed back through the event loop.

This is a key reason why understanding async behavior matters when working with browser APIs.