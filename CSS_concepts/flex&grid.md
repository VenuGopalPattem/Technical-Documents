---

# Flexbox and Grid

## Flexbox Layout (One Direction Layout)

```
+---------------------------------------+
|           FLEX CONTAINER              |
|                                       |
|  +--------+  +--------+  +--------+   |
|  | Item 1 |  | Item 2 |  | Item 3 |   |
|  +--------+  +--------+  +--------+   |
|                                       |
+---------------------------------------+
```

## What Flexbox Does

Flexbox arranges items in a single direction.

It can arrange items:

* In a row (left to right)
* In a column (top to bottom)

It is mainly used to:

* Align items
* Distribute space
* Control spacing easily

Flexbox works on one main axis at a time (horizontal or vertical).

---

# Important Flexbox Properties

## display: flex;

Makes the parent a flex container.

```
display: flex;
```

Turns normal layout into flex layout.

---

## flex-direction

Controls direction of items.

```
flex-direction: row;
```

Items go left to right.

```
flex-direction: column;
```

Items go top to bottom.

---

## justify-content

Aligns items along the main axis.

```
justify-content: center;
```

Centers items horizontally (if row).

Other values:

* flex-start → items at beginning
* flex-end → items at end
* space-between → space between items
* space-around → space around items

---

## align-items

Aligns items on the cross axis.

```
align-items: center;
```

Centers items vertically (if row).

---

## gap

Adds space between items.

```
gap: 20px;
```

Adds equal spacing between boxes.

---

# Grid Layout (Two Direction Layout)

```
+----------------------------------+
|          GRID CONTAINER          |
|                                  |
|  +--------+  +--------+          |
|  | Item 1 |  | Item 2 |          |
|  +--------+  +--------+          |
|                                  |
|  +--------+  +--------+          |
|  | Item 3 |  | Item 4 |          |
|  +--------+  +--------+          |
|                                  |
+----------------------------------+
```

## What Grid Does

Grid arranges items in rows and columns at the same time.

It is used for:

* Complex layouts
* Full page structure
* Creating rows and columns together

Grid works in two dimensions (horizontal and vertical).

---

# Important Grid Properties

## display: grid;

Makes the parent a grid container.

```
display: grid;
```

Activates grid layout.

---

## grid-template-columns

Defines number and size of columns.

```
grid-template-columns: 1fr 1fr;
```

Creates two equal columns.

---

## grid-template-rows

Defines rows.

```
grid-template-rows: 100px 100px;
```

Creates two rows of 100px height.

---

## gap

Adds space between grid cells.

```
gap: 20px;
```

Adds spacing between rows and columns.

---

# Simple Difference

Flexbox:

* One direction (row or column)
* Best for small components

Grid:

* Two directions (rows and columns)
* Best for full layouts

---

