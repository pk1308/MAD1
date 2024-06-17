Comprehensive HTML cheat sheet

````markdown
# HTML Cheat Sheet

## Basic Structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
````

## Document Metadata

```html
<!DOCTYPE html> <!-- Document type declaration -->
<html lang="en"> <!-- Sets the language of the document -->
<head>
    <meta charset="UTF-8"> <!-- Character encoding -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Responsive design -->
    <title>Document</title> <!-- Document title -->
</head>
<body>
    <!-- Body content -->
</body>
</html>
```

## Headings

```html
<h1>This is a Heading 1</h1>
<h2>This is a Heading 2</h2>
<h3>This is a Heading 3</h3>
<h4>This is a Heading 4</h4>
<h5>This is a Heading 5</h5>
<h6>This is a Heading 6</h6>
```

## Paragraphs and Line Breaks

```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
<p>This is a paragraph with a <br> line break.</p>
```

## Text Formatting

```html
<b>Bold</b> or <strong>Strong</strong> <!-- Bold text -->
<i>Italic</i> or <em>Emphasized</em> <!-- Italic text -->
<u>Underline</u> <!-- Underlined text -->
<del>Deleted</del> <!-- Strikethrough text -->
<mark>Highlighted</mark> <!-- Highlighted text -->
<sup>Superscript</sup> <!-- Superscript text -->
<sub>Subscript</sub> <!-- Subscript text -->
```

## Links

```html
<a href="https://www.example.com">This is a link</a> <!-- Simple link -->
<a href="https://www.example.com" target="_blank">Open link in new tab</a> <!-- Open in new tab -->
<a href="mailto:someone@example.com">Send Email</a> <!-- Email link -->
<a href="tel:+1234567890">Call Number</a> <!-- Phone link -->
```

## Lists

### Unordered List

```html
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

### Ordered List

```html
<ol>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

### Definition List

```html
<dl>
    <dt>Term 1</dt>
    <dd>Definition of Term 1</dd>
    <dt>Term 2</dt>
    <dd>Definition of Term 2</dd>
</dl>
```

## Images

```html
<img src="image.jpg" alt="Description of Image"> <!-- Basic image -->
<img src="image.jpg" alt="Description of Image" width="500" height="600"> <!-- Image with size -->
```

## Tables

```html
<table>
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
    </tr>
    <tr>
        <td>Data 1</td>
        <td>Data 2</td>
    </tr>
</table>
```

## Forms

```html
<form action="/submit-form" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
  
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
  
    <input type="submit" value="Submit">
</form>
```

### Common Form Elements

```html
<input type="text" placeholder="Text input"> <!-- Single-line text input -->
<input type="password" placeholder="Password"> <!-- Password input -->
<input type="email" placeholder="Email address"> <!-- Email input -->
<textarea placeholder="Multi-line text input"></textarea> <!-- Multi-line text input -->
<select>
    <option value="option1">Option 1</option>
    <option value="option2">Option 2</option>
</select> <!-- Drop-down list -->
<input type="radio" name="radio" value="option1"> Option 1 <!-- Radio button -->
<input type="checkbox" name="checkbox" value="option1"> Option 1 <!-- Checkbox -->
```

## Semantic HTML

```html
<header>
    <!-- Header content -->
</header>

<nav>
    <!-- Navigation links -->
</nav>

<main>
    <!-- Main content -->
</main>

<article>
    <!-- Article content -->
</article>

<section>
    <!-- Section content -->
</section>

<aside>
    <!-- Sidebar content -->
</aside>

<footer>
    <!-- Footer content -->
</footer>
```

## Media

### Audio

```html
<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>
```

### Video

```html
<video controls>
    <source src="video.mp4" type="video/mp4">
    Your browser does not support the video element.
</video>
```

## Embedding

### Iframe

```html
<iframe src="https://www.example.com" title="Iframe Example"></iframe>
```

### Embed

```html
<embed src="file.pdf" type="application/pdf">
```

### Object

```html
<object data="file.pdf" type="application/pdf">
    <p>Alternative text for browsers that do not support the object element.</p>
</object>
```

## Scripting

### Internal JavaScript

```html
<script>
    console.log('Hello, world!');
</script>
```

### External JavaScript

```html
<script src="script.js"></script>
```

## Meta Tags

```html
<meta charset="UTF-8"> <!-- Character encoding -->
<meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Responsive design -->
<meta name="description" content="Description of the webpage"> <!-- Description -->
<meta name="keywords" content="HTML, CSS, JavaScript"> <!-- Keywords -->
<meta name="author" content="Author Name"> <!-- Author -->
```

## Miscellaneous

### Comments

```html
<!-- This is a comment -->
```

### Doctype

```html
<!DOCTYPE html>
```

### Character Encoding

```html
<meta charset="UTF-8">
```

## HTML Entities

```html
<  <!-- Less than -->
>  <!-- Greater than -->
& <!-- Ampersand -->
" <!-- Double quote -->
' <!-- Single quote -->
© <!-- Copyright -->
® <!-- Registered trademark -->
  <!-- Non-breaking space -->
```

This cheat sheet covers a broad range of basic and advanced HTML elements and attributes. Feel free to expand it with more specific tags and use cases as needed!
