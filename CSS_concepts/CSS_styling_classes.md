
---

# Common CSS Styling Classes

## What Are Styling Classes?

Styling classes are CSS classes used to control the **appearance** of elements.

They change how something looks — like color, size, spacing, alignment, or shape.

Unlike structural classes (which control layout), styling classes control design.

---

# Common Styling Classes

## 1. Text Color

Used to change text color.

```css
.text-red {
  color: red;
}

.text-blue {
  color: blue;
}
```

---

## 2. Background Color

Used to change background color.

```css
.bg-light {
  background-color: lightgray;
}

.bg-dark {
  background-color: black;
  color: white;
}
```

---

## 3. Text Alignment

Used to align text.

```css
.text-center {
  text-align: center;
}

.text-right {
  text-align: right;
}
```

---

## 4. Font Size

Used to change text size.

```css
.small {
  font-size: 12px;
}

.large {
  font-size: 24px;
}
```

---

## 5. Margin

Used to create space outside an element.

```css
.m-10 {
  margin: 10px;
}
```

---

## 6. Padding

Used to create space inside an element.

```css
.p-10 {
  padding: 10px;
}
```

---

## 7. Border

Used to add a border around elements.

```css
.border {
  border: 1px solid black;
}
```

---

# Simple Example

```html
<div class="bg-light p-10 border text-center">
  Styled Box
</div>
```
