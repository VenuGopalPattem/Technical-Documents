
# CSS Specificity

## Definition

CSS Specificity is the rule that decides **which CSS style will apply** when multiple CSS rules target the same element.

The selector with the higher specificity value wins.

---

# Specificity Format (Binary Style)

We represent specificity like this:

```
Inline  >  ID  >  Class  >  Element
```

In binary form:

```
( Inline , ID , Class , Element )
```

Example values:

```
1 0 0 0  → Inline style
0 1 0 0  → ID selector
0 0 1 0  → Class selector
0 0 0 1  → Element selector
```

Higher number from left side wins.

---

# Simple Program Example

```html
<!DOCTYPE html>
<html>
<head>
<style>

p {
  color: blue;
}

.text {
  color: green;
}

#para {
  color: red;
}

</style>
</head>
<body>

<p id="para" class="text">
  Hello World
</p>

</body>
</html>
```

---

# Step-by-Step Specificity Calculation

We have:

### 1. Element Selector

```css
p { color: blue; }
```

Specificity:

```
0 0 0 1
```

---

### 2. Class Selector

```css
.text { color: green; }
```

Specificity:

```
0 0 1 0
```

---

### 3. ID Selector

```css
#para { color: red; }
```

Specificity:

```
0 1 0 0
```

---

# Compare Using > Symbol

```
0 1 0 0  >  0 0 1 0  >  0 0 0 1
```

ID > Class > Element

So the final color will be:

```
red
```

---

# If We Add Inline Style

```html
<p id="para" class="text" style="color: purple;">
```

Inline specificity:

```
1 0 0 0
```

Now compare:

```
1 0 0 0  >  0 1 0 0
```

Inline > ID

So final color becomes:

```
purple
```

---

# One More Example

If a selector is:

```css
#para.text
```

Specificity:

```
0 1 1 0
```

Compare:

```
0 1 1 0  >  0 1 0 0
```

Because class adds extra strength.

---


Specificity Order:

```
Inline  >  ID  >  Class  >  Element
```

Binary Form:

```
Inline  = 1 0 0 0
ID      = 0 1 0 0
Class   = 0 0 1 0
Element = 0 0 0 1
```

The selector with the greater binary value wins.
