---

# CSS Responsive Queries

## Definition

CSS Responsive Queries (also called Media Queries) are used to change the design of a webpage based on screen size or device type.

They help make websites work properly on:

* Mobile phones
* Tablets
* Laptops
* Large screens

Responsive queries allow the layout to adjust automatically depending on the screen width, height, or other conditions.

---

# Basic Syntax

```css
@media (condition) {
  /* CSS rules here */
}
```

Example:

```css
@media (max-width: 600px) {
  body {
    background-color: lightblue;
  }
}
```

This means:
If screen width is 600px or less, change background color.

---

# Types of Media Queries

## 1. Based on Width

Most common type.

```css
@media (max-width: 768px) { }
@media (min-width: 1024px) { }
```

* `max-width` → Applies when screen is smaller than given value
* `min-width` → Applies when screen is bigger than given value

---

## 2. Based on Height

```css
@media (max-height: 500px) { }
```

Used when screen height matters.

---

## 3. Based on Device Orientation

```css
@media (orientation: portrait) { }
@media (orientation: landscape) { }
```

* Portrait → vertical screen
* Landscape → horizontal screen

---

## 4. Combining Conditions

```css
@media (min-width: 600px) and (max-width: 900px) { }
```

You can combine multiple conditions.

---

# How It Works

1. The browser checks the screen size.
2. It compares it with the media query condition.
3. If condition is true → CSS inside the block is applied.
4. If condition is false → That CSS is ignored.

The normal CSS is loaded first.
Media queries override styles only when the condition matches.

---

# Simple Working Example

```html
<!DOCTYPE html>
<html>
<head>
<style>

.box {
  width: 400px;
  height: 200px;
  background-color: lightcoral;
}

@media (max-width: 600px) {
  .box {
    width: 200px;
    background-color: lightblue;
  }
}

</style>
</head>
<body>

<div class="box"></div>

</body>
</html>
```

What happens:

* On large screens → Box is 400px and coral color
* On small screens (600px or less) → Box becomes 200px and blue

---
