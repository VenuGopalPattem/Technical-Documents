# CSS Units 

## What Is a CSS Unit?

A CSS unit tells the browser **how big or small something should be**.

When you write:

```css
width: 200px;
```

`px` is the unit.

Without a unit, CSS does not know how to measure the size.

Units are used with:

* Width
* Height
* Font-size
* Margin
* Padding

---

## Why Units Are Important

If you use only fixed sizes, your design may not work properly on:

* Mobile phones
* Tablets
* Large screens

Some units are fixed.
Some units change depending on screen size.

Understanding this difference is very important for beginners.

---

# Two Main Types of Units

## 1. Absolute Unit

These units are fixed.
They do not change when screen size changes.

## 2. Relative Units

These units change depending on something:

* Parent element
* Root element
* Screen size

---

# Important Units (Simple Table)

| Unit | Type     | What It Depends On | Easy Meaning           |
| ---- | -------- | ------------------ | ---------------------- |
| px   | Absolute | Nothing            | Fixed size             |
| %    | Relative | Parent element     | Part of parent         |
| em   | Relative | Parent font-size   | Multiplies font        |
| rem  | Relative | Root font-size     | Stable scaling         |
| vw   | Relative | Screen width       | Based on screen width  |
| vh   | Relative | Screen height      | Based on screen height |

---

# Simple Explanation of Each Unit

## px (Pixel)

Fixed size.

```css
width: 200px;
```

The size will stay 200 pixels on any screen.

Use when you want exact control.

---

## % (Percentage)

Based on the parent element’s size.

```css
width: 50%;
```

This means:
The element takes 50% of its parent's width.

Good for flexible layouts.

---

## em

Based on parent font-size.

```css
font-size: 2em;
```

If parent font-size is 16px →
2em becomes 32px.

Good for scaling text inside components.

---

## rem

Based on root (html) font-size.

```css
font-size: 2rem;
```

If html font-size is 16px →
2rem becomes 32px.

More predictable than em.

Recommended for beginners.

---

## vw (Viewport Width)

Based on screen width.

```css
width: 50vw;
```

Means 50% of screen width.

Useful for full-width sections.

---

## vh (Viewport Height)

Based on screen height.

```css
height: 100vh;
```

Means full screen height.

Used for full-screen sections.

---

# Simple Comparison
```
px → fixed
% → based on parent
em → based on parent font
rem → based on root font
vw → based on screen width
vh → based on screen height
```

---
