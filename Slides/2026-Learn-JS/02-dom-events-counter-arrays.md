---
title: Learn JS - 02 DOM, Events, Counter, Arrays
layout: slides
---

## ch05 — DOM

JavaScript can read and change any element on the page

## Select an Element

```js
document.querySelector("h1")
document.querySelector("p")
document.querySelector("button")
```

* Finds the first matching element
* Try it in F12 on any website

## Change Text

```js
const h1 = document.querySelector("h1")
h1.textContent = "I changed this!"
```

The page updates instantly. No reload needed.

## Change Style

```js
const h1 = document.querySelector("h1")
h1.style.color = "red"
h1.style.fontSize = "50px"
```

This is the same as CSS, but controlled by JavaScript.

## Create New Elements

```js
const p = document.createElement("p")
p.textContent = "I was created by JavaScript!"
document.body.appendChild(p)
```

* `createElement` — make a new element
* `appendChild` — add it to the page
* It appears immediately

## Remove Elements

```js
document.querySelector("h1").remove()
```

Try it on any website — remove things you don't like!

## ch05 Summary

* `querySelector` — find an element
* `.textContent` — change text
* `.style` — change CSS
* `createElement` + `appendChild` — add new elements
* `.remove()` — delete elements

## ch06 — Events

Make the page respond to clicks and actions

## Click Event

```js
const btn = document.querySelector("button")

btn.addEventListener("click", () => {
  alert("You clicked!")
})
```

* `addEventListener` — listen for something to happen
* `"click"` — the type of event
* `() => { ... }` — what to do when it happens

## Click Counter

Create a button that counts clicks:

```js
const btn = document.querySelector("button")
let count = 0

btn.addEventListener("click", () => {
  count = count + 1
  btn.textContent = "Clicked: " + count
})
```

Paste in F12 Console. The button now counts!

## Change Content on Click

```js
const btn = document.querySelector("button")
const h1 = document.querySelector("h1")

btn.addEventListener("click", () => {
  h1.textContent = "Button was clicked!"
  h1.style.color = "green"
})
```

Functions from ch01 + DOM from ch05 + Events = interactive page!

## Common Events

| Event | When |
|-------|------|
| `click` | User clicks |
| `mouseover` | Mouse enters |
| `mouseout` | Mouse leaves |
| `keydown` | Key pressed |
| `input` | Input value changes |

## ch06 Summary

* `addEventListener("click", () => { })` — respond to clicks
* Combine with DOM to update the page
* This is how all interactive websites work

## ch07 — Project: Counter

Combine everything into one file!

## What We're Building

```
┌─────────────────────┐
│                     │
│        42           │
│                     │
│   [ - ]    [ + ]    │
│                     │
│   [ Reset ]         │
│                     │
└─────────────────────┘
```

## Step 1: HTML

Create `counter.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Counter</title>
</head>
<body>
  <h1 id="count">0</h1>
  <button id="dec">-</button>
  <button id="inc">+</button>
  <button id="reset">Reset</button>
</body>
</html>
```

Open in browser. You see 0 and three buttons.

## Step 2: JavaScript

Add `<script>` before `</body>`:

```html
<script>
  let count = 0
  const display = document.querySelector("#count")

  document.querySelector("#inc").addEventListener("click", () => {
    count = count + 1
    display.textContent = count
  })

  document.querySelector("#dec").addEventListener("click", () => {
    count = count - 1
    display.textContent = count
  })

  document.querySelector("#reset").addEventListener("click", () => {
    count = 0
    display.textContent = count
  })
</script>
```

The buttons work now!

## Step 3: Refactor with Functions

There's repeated code. Use a function:

```html
<script>
  let count = 0
  const display = document.querySelector("#count")

  const update = fn => {
    count = fn(count)
    display.textContent = count
  }

  document.querySelector("#inc").addEventListener("click",
    () => update(n => n + 1))
  document.querySelector("#dec").addEventListener("click",
    () => update(n => n - 1))
  document.querySelector("#reset").addEventListener("click",
    () => update(() => 0))
</script>
```

`update` takes a function — ch01 equation style!

## Step 4: Add CSS

Add `<style>` in `<head>`:

```html
<style>
  body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    background: #1a1a2e;
    color: #eee;
    font-family: sans-serif;
  }
  #count { font-size: 80px; margin: 20px; }
  button {
    font-size: 24px; padding: 10px 24px; margin: 5px;
    border: 1px solid #eee; background: none; color: #eee;
    cursor: pointer; border-radius: 8px;
  }
  button:hover { background: #333; }
</style>
```

## Step 5: Add Color with Logic

Use ch02 logic to change color:

```js
const getColor = n => {
  if (n > 0) {
    return "green"
  } else if (n < 0) {
    return "red"
  } else {
    return "#eee"
  }
}

const update = fn => {
  count = fn(count)
  display.textContent = count
  display.style.color = getColor(count)
}
```

## What We Used

| Chapter | What | How |
|---------|------|-----|
| ch01 | Functions | `n => n + 1` |
| ch02 | Logic | `getColor` with if/else |
| ch03 | HTML | h1, button |
| ch04 | CSS | styling, flexbox |
| ch05 | DOM | querySelector, textContent |
| ch06 | Events | addEventListener click |

## ch07 Summary

* One `.html` file = HTML + CSS + JS
* Start simple, add features step by step
* You just built a real interactive web app!

## ch08 — Arrays

A list of things

## What is an Array?

```js
const fruits = ["Apple", "Banana", "Cherry"]
const nums = [1, 2, 3, 4, 5]
const prices = [50, 30, 40, 60]
```

* A list inside `[ ]`
* Can hold any values
* Values separated by `,`

## Access Items

```js
const fruits = ["Apple", "Banana", "Cherry"]

fruits[0]  // "Apple"   (first)
fruits[1]  // "Banana"  (second)
fruits[2]  // "Cherry"  (third)

fruits.length // 3
```

* Index starts from `0`, not `1`
* `.length` tells you how many items

## Map: Transform Every Item

Apply a function to every item in the list:

```js
[1, 2, 3].map(x => x * 2)
// [2, 4, 6]

[1, 2, 3].map(x => x + 10)
// [11, 12, 13]

["apple", "banana"].map(s => s.toUpperCase())
// ["APPLE", "BANANA"]
```

* `.map()` creates a new list
* The original list is unchanged
* The function is just our ch01 equation!

## Map: Real Example

Calculate prices with tax:

```js
const prices = [100, 200, 50]

prices.map(p => p * 1.1)
// [110, 220, 55]
```

Double all scores:

```js
const scores = [80, 90, 70]

scores.map(s => s * 2)
// [160, 180, 140]
```

## ch08 Summary

* Array = list in `[ ]`
* Access with `[0]`, `[1]`, `[2]`...
* `.map(fn)` — apply function to every item
* Map is ch01 equations applied to lists
