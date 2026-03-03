---

# Common Header Meta Tags

## Definition

Meta tags are special tags placed inside the `<head>` section of an HTML document.

They provide information about the webpage to the browser, search engines, and social media platforms.

Meta tags do not display content on the page.
They give instructions or describe the page.

---

# Basic Structure

```html
<head>
  <meta attribute="value">
</head>
```

---

# Common Meta Tags and Their Types

## 1. Charset (Character Encoding)

```html
<meta charset="UTF-8">
```

### Type:

Character encoding meta tag

### What it does:

Tells the browser how to read characters.
UTF-8 supports most languages and symbols.

---

## 2. Viewport

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Type:

Responsive design meta tag

### What it does:

Makes the website responsive.
Adjusts layout based on device screen width.

* `width=device-width` → Matches screen width
* `initial-scale=1.0` → Sets default zoom level

This is required for mobile-friendly design.

---

## 3. Description

```html
<meta name="description" content="This is a sample webpage.">
```

### Type:

SEO meta tag

### What it does:

Provides a short summary of the page.
Search engines show this in search results.

---

## 4. Keywords

```html
<meta name="keywords" content="HTML, CSS, Web Development">
```

### Type:

SEO meta tag

### What it does:

Specifies related keywords for the page.
Used for search engine indexing (less important today).

---

## 5. Author

```html
<meta name="author" content="John Doe">
```

### Type:

Information meta tag

### What it does:

Specifies the author of the webpage.

---

## 6. Refresh

```html
<meta http-equiv="refresh" content="5">
```

### Type:

HTTP equivalent meta tag

### What it does:

Refreshes the page after 5 seconds.

You can also redirect:

```html
<meta http-equiv="refresh" content="5; url=https://example.com">
```

Redirects after 5 seconds.

---

## 7. Robots

```html
<meta name="robots" content="index, follow">
```

### Type:

SEO control meta tag

### What it does:

Tells search engines how to treat the page.

Common values:

* `index` → Allow indexing
* `noindex` → Do not index
* `follow` → Follow links
* `nofollow` → Do not follow links

---

# Simple Example of Head Section

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Sample webpage">
  <meta name="author" content="John Doe">
  <title>My Page</title>
</head>
<body>

<h1>Hello World</h1>

</body>
</html>
```

---