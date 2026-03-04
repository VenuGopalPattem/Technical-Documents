
---

# CSS Box Model

## Diagram

```
+---------------------------+
|          Margin           |
|   +-------------------+   |
|   |      Border       |   |
|   |  +-------------+  |   |
|   |  |   Padding   |  |   |
|   |  |  +-------+  |  |   |
|   |  |  |Content|  |  |   |
|   |  |  +-------+  |  |   |
|   |  +-------------+  |   |
|   +-------------------+   |
+---------------------------+
```

---

## Content

The actual text, image, or element inside the box.

## Padding

Space between the content and the border. It adds space inside the box.

## Border

The line that wraps around padding and content.

## Margin

Space outside the border. It creates distance from other elements.

---

# Simple Example

```html
<!DOCTYPE html>
<html>
<head>
<style>
.box {
    width: 200px;
    height: 100px;
    padding: 20px;
    border: 5px solid black;
    margin: 30px;
    background-color: lightblue;
}
</style>
</head>
<body>

<div class="box">
  Hello World
</div>

</body>
</html>
```
