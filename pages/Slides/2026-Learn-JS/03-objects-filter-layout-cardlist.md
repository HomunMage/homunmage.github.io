---
title: Learn JS - 03 Objects, Filter, Layout, Card List
---

## ch09 — Objects

Describe a thing with key-value pairs

## What is an Object?

```js
const person = {
  name: "Alice",
  age: 25,
  city: "Taipei"
}

person.name // "Alice"
person.age  // 25
person.city // "Taipei"
```

* Inside `{ }`
* Each line: `key: value`
* Access with `.key`

## Like a Form

Think of it like filling out a form:

| Field | Value |
|-------|-------|
| Name | Alice |
| Age | 25 |
| City | Taipei |

```js
const form = {
  name: "Alice",
  age: 25,
  city: "Taipei"
}
```

## Arrays of Objects

Real data is usually a list of things:

```js
const menu = [
  { name: "Coffee", price: 50 },
  { name: "Tea", price: 40 },
  { name: "Juice", price: 60 }
]

menu[0].name  // "Coffee"
menu[0].price // 50
menu[1].name  // "Tea"
```

## Map on Objects

Extract one field from every item:

```js
const menu = [
  { name: "Coffee", price: 50 },
  { name: "Tea", price: 40 },
  { name: "Juice", price: 60 }
]

menu.map(item => item.name)
// ["Coffee", "Tea", "Juice"]

menu.map(item => item.price)
// [50, 40, 60]
```

## ch09 Summary

* Object = `{ key: value }` — describe a thing
* Access with `.key`
* Array of Objects = list of things
* `.map()` works on arrays of objects too

## ch10 — Filter

Pick what you want from a list

## What is Filter?

Keep only the items that pass a test:

```js
[1, 2, 3, 4, 5].filter(x => x > 3)
// [4, 5]

[10, 20, 30, 40].filter(x => x >= 25)
// [30, 40]
```

* The function returns `true` → keep it
* The function returns `false` → remove it

## Filter with Logic

Use ch02 logic inside filter:

```js
const ages = [12, 25, 8, 30, 15, 45]

ages.filter(age => age >= 18)
// [25, 30, 45]

ages.filter(age => age < 18)
// [12, 8, 15]
```

## Filter Objects

```js
const menu = [
  { name: "Coffee", price: 50 },
  { name: "Cake", price: 120 },
  { name: "Tea", price: 40 },
  { name: "Steak", price: 350 }
]

menu.filter(item => item.price <= 100)
// [{ name: "Coffee", price: 50 }, { name: "Tea", price: 40 }]
```

## Map + Filter Together

Chain them:

```js
const menu = [
  { name: "Coffee", price: 50 },
  { name: "Cake", price: 120 },
  { name: "Tea", price: 40 },
  { name: "Steak", price: 350 }
]

// names of items under 100
menu
  .filter(item => item.price <= 100)
  .map(item => item.name)
// ["Coffee", "Tea"]
```

* **filter** — pick which items
* **map** — transform each item
* Chain them for powerful data processing

## ch10 Summary

* `.filter(fn)` — keep items where fn returns true
* Works on numbers, strings, objects
* Combine with `.map()` for data pipelines
* filter uses ch02 logic (comparisons)

## ch11 — Layout with Flexbox

Make elements sit side by side or stack nicely

## The Problem

By default, every `<div>` takes a full row:

```html
<div>A</div>
<div>B</div>
<div>C</div>
```

They stack vertically. What if we want them side by side?

## Flexbox

Add `display: flex` to the parent:

```html
<div style="display: flex; gap: 10px;">
  <div>A</div>
  <div>B</div>
  <div>C</div>
</div>
```

Now A, B, C sit side by side!

## Flex Direction

```css
.container {
  display: flex;
  flex-direction: row;    /* side by side (default) */
}

.container {
  display: flex;
  flex-direction: column; /* stacked vertically */
}
```

## Centering

```css
body {
  display: flex;
  justify-content: center; /* horizontal center */
  align-items: center;     /* vertical center */
  height: 100vh;           /* full screen height */
}
```

This is how we centered the counter in ch07!

## Try It in F12

```js
const box = document.createElement("div")
box.style.display = "flex"
box.style.gap = "10px"

;["A", "B", "C"].forEach(text => {
  const item = document.createElement("div")
  item.textContent = text
  item.style.padding = "20px"
  item.style.border = "1px solid white"
  box.appendChild(item)
})
document.body.appendChild(box)
```

## ch11 Summary

* `display: flex` — make children sit in a row
* `flex-direction: column` — stack vertically
* `justify-content: center` — center on main axis
* `align-items: center` — center on cross axis
* `gap` — spacing between items

## ch12 — Project: Card List

Combine arrays, objects, map, filter, and flexbox

## What We're Building

A list of cards from data, with a filter:

```
[Show All] [Under 100] [Over 100]

┌──────────┐ ┌──────────┐ ┌──────────┐
│ Coffee   │ │ Tea      │ │ Cake     │
│ $50      │ │ $40      │ │ $120     │
└──────────┘ └──────────┘ └──────────┘
```

## Step 1: The Data

```js
const menu = [
  { name: "Coffee", price: 50 },
  { name: "Tea", price: 40 },
  { name: "Cake", price: 120 },
  { name: "Juice", price: 60 },
  { name: "Steak", price: 350 },
  { name: "Salad", price: 80 }
]
```

## Step 2: Card Function

A function that creates one card — ch01 style:

```js
const Card = item => {
  const div = document.createElement("div")
  div.className = "card"
  div.innerHTML = "<h3>" + item.name + "</h3>"
    + "<p>$" + item.price + "</p>"
  return div
}
```

## Step 3: Render List

```js
const container = document.querySelector("#cards")

const render = items => {
  container.innerHTML = ""
  items
    .map(Card)
    .forEach(card => container.appendChild(card))
}

render(menu)
```

## Step 4: Filter Buttons

```js
document.querySelector("#all").addEventListener("click",
  () => render(menu))

document.querySelector("#cheap").addEventListener("click",
  () => render(menu.filter(item => item.price <= 100)))

document.querySelector("#expensive").addEventListener("click",
  () => render(menu.filter(item => item.price > 100)))
```

## Full Code

```html
<!DOCTYPE html>
<html>
<head>
  <title>Menu</title>
  <style>
    body {
      background: #1a1a2e; color: #eee;
      font-family: sans-serif; padding: 20px;
    }
    .filters { margin-bottom: 20px; }
    .filters button {
      padding: 8px 16px; margin: 4px;
      border: 1px solid #eee; background: none;
      color: #eee; cursor: pointer; border-radius: 4px;
    }
    .filters button:hover { background: #333; }
    #cards { display: flex; flex-wrap: wrap; gap: 10px; }
    .card {
      border: 1px solid #444; border-radius: 8px;
      padding: 16px; min-width: 120px;
    }
    .card h3 { margin: 0 0 8px 0; }
    .card p { margin: 0; color: #aaa; }
  </style>
</head>
<body>
  <h1>Menu</h1>
  <div class="filters">
    <button id="all">All</button>
    <button id="cheap">Under $100</button>
    <button id="expensive">Over $100</button>
  </div>
  <div id="cards"></div>
  <script>
    const menu = [
      { name: "Coffee", price: 50 },
      { name: "Tea", price: 40 },
      { name: "Cake", price: 120 },
      { name: "Juice", price: 60 },
      { name: "Steak", price: 350 },
      { name: "Salad", price: 80 }
    ]

    const Card = item => {
      const div = document.createElement("div")
      div.className = "card"
      div.innerHTML = "<h3>" + item.name + "</h3>"
        + "<p>$" + item.price + "</p>"
      return div
    }

    const container = document.querySelector("#cards")
    const render = items => {
      container.innerHTML = ""
      items.map(Card).forEach(c => container.appendChild(c))
    }

    document.querySelector("#all").addEventListener("click",
      () => render(menu))
    document.querySelector("#cheap").addEventListener("click",
      () => render(menu.filter(i => i.price <= 100)))
    document.querySelector("#expensive").addEventListener("click",
      () => render(menu.filter(i => i.price > 100)))

    render(menu)
  </script>
</body>
</html>
```

## What We Used

| Chapter | What |
|---------|------|
| ch01 | Functions — `Card`, `render` |
| ch02 | Logic — `price <= 100` |
| ch04 | CSS — styling cards |
| ch05 | DOM — createElement, appendChild |
| ch06 | Events — button clicks |
| ch08 | Arrays — list of menu items |
| ch09 | Objects — `{ name, price }` |
| ch10 | Filter — filter by price |
| ch11 | Flexbox — card layout |

## ch12 Summary

* Data (array of objects) → Functions (Card, render) → Page
* Filter buttons change what's displayed
* This is how real web apps work
* You built a menu filter app!
