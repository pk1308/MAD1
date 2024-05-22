comprehensive CSS cheat sheet

```markdown
# CSS Cheat Sheet

## Basic Syntax

```css
selector {
    property: value;
}
```

## Selectors

### Universal Selector

```css
* {
    margin: 0;
    padding: 0;
}
```

### Element Selector

```css
p {
    color: blue;
}
```

### Class Selector

```css
.className {
    font-size: 14px;
}
```

### ID Selector

```css
#idName {
    background-color: yellow;
}
```

### Attribute Selector

```css
input[type="text"] {
    border: 1px solid #000;
}
```

### Pseudo-class Selector

```css
a:hover {
    color: red;
}
```

### Pseudo-element Selector

```css
p::first-line {
    font-weight: bold;
}
```

## Box Model

### Margin

```css
div {
    margin: 20px;
    margin-top: 10px;
    margin-right: 15px;
    margin-bottom: 10px;
    margin-left: 5px;
}
```

### Padding

```css
div {
    padding: 20px;
    padding-top: 10px;
    padding-right: 15px;
    padding-bottom: 10px;
    padding-left: 5px;
}
```

### Border

```css
div {
    border: 1px solid black;
    border-width: 2px;
    border-style: dashed;
    border-color: blue;
}
```

### Width and Height

```css
div {
    width: 100px;
    height: 50px;
}
```

## Background

```css
body {
    background-color: #f0f0f0;
    background-image: url('background.jpg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    background-size: cover;
}
```

## Text

### Color

```css
p {
    color: #333;
}
```

### Font

```css
p {
    font-family: Arial, sans-serif;
    font-size: 16px;
    font-weight: bold;
    font-style: italic;
    line-height: 1.5;
    text-align: center;
    text-decoration: underline;
    text-transform: uppercase;
    text-indent: 50px;
    letter-spacing: 2px;
    word-spacing: 5px;
}
```

## Lists

### Unordered List

```css
ul {
    list-style-type: disc;
    list-style-position: inside;
}
```

### Ordered List

```css
ol {
    list-style-type: decimal;
    list-style-position: outside;
}
```

## Display and Positioning

### Display

```css
div {
    display: none; /* block, inline, inline-block, flex, grid */
}
```

### Position

```css
div {
    position: static; /* relative, absolute, fixed, sticky */
    top: 10px;
    right: 10px;
    bottom: 10px;
    left: 10px;
}
```

### Float and Clear

```css
div {
    float: left; /* right, none */
    clear: both; /* left, right, none */
}
```

### Z-index

```css
div {
    position: relative;
    z-index: 10;
}
```

## Flexbox

### Container

```css
.container {
    display: flex;
    flex-direction: row; /* row-reverse, column, column-reverse */
    flex-wrap: nowrap; /* wrap, wrap-reverse */
    justify-content: flex-start; /* center, flex-end, space-between, space-around, space-evenly */
    align-items: stretch; /* flex-start, center, flex-end, baseline */
    align-content: stretch; /* flex-start, center, flex-end, space-between, space-around */
}
```

### Item

```css
.item {
    flex: 0 1 auto; /* flex-grow, flex-shrink, flex-basis */
    align-self: auto; /* flex-start, center, flex-end, baseline, stretch */
    order: 0;
}
```

## Grid

### Container

```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* or 100px 1fr 2fr */
    grid-template-rows: repeat(2, auto); /* or 100px 200px */
    gap: 10px; /* row-gap, column-gap */
    grid-auto-flow: row; /* column, dense */
}
```

### Item

```css
.item {
    grid-column: 1 / 3; /* or span 2 */
    grid-row: 1 / 2; /* or span 1 */
    justify-self: center; /* start, end, stretch */
    align-self: center; /* start, end, stretch */
}
```

## Media Queries

```css
@media (max-width: 600px) {
    body {
        background-color: lightblue;
    }
}
```

## Animations

### Keyframes

```css
@keyframes example {
    from {background-color: red;}
    to {background-color: yellow;}
}
```

### Animation

```css
div {
    animation-name: example;
    animation-duration: 4s;
    animation-timing-function: linear; /* ease, ease-in, ease-out, ease-in-out */
    animation-delay: 2s;
    animation-iteration-count: infinite; /* or a number */
    animation-direction: alternate; /* normal, reverse, alternate-reverse */
    animation-fill-mode: forwards; /* none, backwards, both */
    animation-play-state: running; /* paused */
}
```

## Transitions

```css
div {
    transition-property: background-color;
    transition-duration: 2s;
    transition-timing-function: ease-in-out; /* linear, ease, ease-in, ease-out */
    transition-delay: 1s;
}
```

## Transform

```css
div {
    transform: translate(50px, 100px);
    transform: rotate(45deg);
    transform: scale(1.5);
    transform: skew(20deg, 10deg);
    transform-origin: top left;
}
```

## Variables

```css
:root {
    --main-color: #06c;
    --padding: 10px;
}
div {
    color: var(--main-color);
    padding: var(--padding);
}
```

## Miscellaneous

### Overflow

```css
div {
    overflow: hidden; /* auto, scroll, visible */
}
```

### Opacity

```css
div {
    opacity: 0.5;
}
```

### Visibility

```css
div {
    visibility: hidden; /* visible, collapse */
}
```

### Cursor

```css
div {
    cursor: pointer; /* default, crosshair, text, wait, help, not-allowed, etc. */
}
```

### Box Shadow

```css
div {
    box-shadow: 10px 10px 5px #888888;
}
```

### Text Shadow

```css
p {
    text-shadow: 2px 2px 5px #555555;
}
```

### Outline

```css
div {
    outline: 2px solid red;
    outline-offset: 5px;
}
```

This CSS cheat sheet covers a wide range of CSS properties and techniques. Feel free to expand it with more specific properties and use cases as needed!

```

```
