---

# Inline vs Block Elements

## Block Elements

Block elements take the full width available.
They always start on a new line.

Examples: `div`, `p`, `h1`, `section`

## Inline Elements

Inline elements take only the width they need.
They do not start on a new line.

Examples: `span`, `a`, `strong`, `em`

---

# Difference Between Block and Inline

| Feature                     | Block Element      | Inline Element                       |
| --------------------------- | ------------------ | ------------------------------------ |
| Starts on new line          | Yes                | No                                   |
| Takes full width            | Yes                | No                                   |
| Width and height can be set | Yes                | No (not properly)                    |
| Margin and padding          | Works on all sides | Top and bottom may not work properly |
| Common examples             | div, p, h1         | span, a, strong                      |

---

# Simple Code Example

```html
<!DOCTYPE html>
<html>
<head>
<style>
.block {
  background-color: lightblue;
  margin: 10px;
}

.inline {
  background-color: lightgreen;
  margin: 10px;
}
</style>
</head>
<body>

<div class="block">Block Element 1</div>
<div class="block">Block Element 2</div>

<span class="inline">Inline 1</span>
<span class="inline">Inline 2</span>

</body>
</html>
```

When you run this:

* The `div` elements will appear one below the other.
* The `span` elements will appear side by side.

---
