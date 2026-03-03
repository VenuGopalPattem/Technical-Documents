
---

# Positioning: Relative and Absolute

## Before Positioning 

```
+-----------+
|  Box 1    |
+-----------+

+-----------+
|  Box 2    |
+-----------+
```

Both boxes:

* Start on a new line
* Follow normal document flow
* Do not overlap

### Before Code

```html
<div class="box box1">Box 1</div>
<div class="box box2">Box 2</div>

<style>
.box {
  width: 100px;
  height: 100px;
  margin: 10px;
}

.box1 { background: lightblue; }
.box2 { background: lightcoral; }
</style>
```

---

# After Positioning

```
+-----------------------+
|   Box 1 (Relative)    |
|        +-----------+  |
|        |  Box 2    |  |
|        | (Absolute)|  |
|        +-----------+  |
+-----------------------+
```

Now:

* Box 1 moves slightly but keeps its space (relative)
* Box 2 is removed from flow and placed freely (absolute)
* Box 2 can overlap

### After Code

```html
<div class="container">
  <div class="box box1">Relative</div>
  <div class="box box2">Absolute</div>
</div>

<style>
.container { position: relative; }

.box {
  width: 100px;
  height: 100px;
}

.box1 {
  background: lightblue;
  position: relative;
  top: 20px;
  left: 20px;
}

.box2 {
  background: lightcoral;
  position: absolute;
  top: 40px;
  left: 120px;
}
</style>
```

---
