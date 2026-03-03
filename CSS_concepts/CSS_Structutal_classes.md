---

# Common CSS Structural Classes

## What Are Structural Classes?

Structural classes are CSS classes used to define the basic layout structure of a webpage.

They help organize content into sections like header, body, sidebar, and footer.

These classes control layout, spacing, and arrangement — not small styling details like colors or fonts.

---

# Common Structural Classes

## 1. `.container`

Used to wrap the whole content inside a fixed width.

It keeps content centered and aligned.

```css
.container {
  width: 80%;
  margin: auto;
}
```

---

## 2. `.row`

Used to create a horizontal section that holds columns.

```css
.row {
  display: flex;
}
```

---

## 3. `.col`

Used inside a row to divide space into columns.

```css
.col {
  flex: 1;
}
```

---

## 4. `.header`

Top section of a webpage.

Usually contains logo and navigation.

```css
.header {
  padding: 20px;
}
```

---

## 5. `.main`

Main content area of the page.

```css
.main {
  padding: 20px;
}
```

---

## 6. `.sidebar`

Side section used for extra links or information.

```css
.sidebar {
  width: 250px;
}
```

---

## 7. `.footer`

Bottom section of the webpage.

```css
.footer {
  padding: 20px;
  text-align: center;
}
```

---

# Simple Example Structure

```html
<div class="container">

  <div class="header">Header</div>

  <div class="row">
    <div class="col main">Main Content</div>
    <div class="col sidebar">Sidebar</div>
  </div>

  <div class="footer">Footer</div>

</div>
```

---
