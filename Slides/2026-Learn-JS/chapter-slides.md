# ch01 Functions

## ch01 — Functions

We start from equations, not syntax

* You don't need math background
* If you can understand `f(x) = x + 1`, you can learn programming
* Open your browser, press **F12**, go to **Console** tab

## What is F12 Console?

* Every browser has a built-in code playground
* Press **F12** (or right-click → Inspect → Console)
* Type code, press Enter, see the result

Try it now:

```js
1 + 1
```

You should see `2`.

## Equation = Function

Everyone already knows this:

`f(x) = x + 1`

* **f** is the name
* **x** is the input
* **x + 1** is the rule
* input goes in, output comes out

This is a function. That's it.

## Your First Code

`f(x) = x + 1` in JavaScript:

```js
const f = x => x + 1

f(1)
f(10)
f(100)
```

* `const f` = the name
* `x` = the input
* `=>` = equals sign
* `x + 1` = the rule

Paste it in F12 Console. You just ran your first function.

## Another Function

`double(x) = x * 2`

```js
const double = x => x * 2

double(3)
double(10)
double(0)
```

The pattern is always the same:

`name(input) = rule` → `const name = input => rule`

## Try More

```js
const square = x => x * x
square(3)
square(5)
```

```js
const half = x => x / 2
half(10)
half(100)
```

Make your own! Change the rule, see what happens.

## Same Input = Same Output

```js
const double = x => x * 2
double(5)
double(5)
double(5)
```

Always `10`. Every time. No surprises.

## Combine Functions

Build bigger rules from smaller rules:

```js
const add1 = x => x + 1
const double = x => x * 2

const add1ThenDouble = x => double(add1(x))

add1ThenDouble(3)
// add1(3) = 4, double(4) = 8
```

## Summary

* `f(x) = x + 1` → `const f = x => x + 1`
* `=>` is just `=`
* Same input always gives same output
* Combine small functions into bigger ones
* **F12 Console** is your playground

---

# ch02 Logic

## ch02 — Logic

In ch01 we learned: input → rule → output

Now we learn how to make **decisions**

## If It Rains, the Ground Gets Wet

We already use logic in daily life:

* **If** it rains → bring an umbrella
* **If** light is red → stop
* **If** customer orders coffee → prepare coffee

This is `if P → Q`

## If in JavaScript

```js
const weather = "rain"

if (weather === "rain") {
  console.log("Bring an umbrella")
}
```

* `===` means "is equal to?"
* `{ }` wraps what to do when true
* If false, nothing happens

## If...Else

What if it's NOT raining?

```js
const weather = "sunny"

if (weather === "rain") {
  console.log("Bring an umbrella")
} else {
  console.log("Enjoy the sunshine")
}
```

* `if` — when true
* `else` — when false
* One of the two will always run

## True and False

Conditions are either `true` or `false`:

```js
3 > 1    // true
5 < 2    // false
3 === 3  // true
3 === 5  // false
```

| Symbol | Meaning |
|--------|---------|
| `===` | is equal to |
| `!==` | is not equal to |
| `>` | greater than |
| `<` | less than |
| `>=` | greater or equal |
| `<=` | less or equal |

## If...Else If...Else

Multiple conditions:

```js
const temp = 35

if (temp > 30) {
  console.log("Very hot")
} else if (temp > 20) {
  console.log("Nice weather")
} else {
  console.log("Bring a jacket")
}
```

Checks from top to bottom. Runs the first one that's true.

## Logic Inside Functions

Put logic inside a function — still input → output:

```js
const advice = temp => {
  if (temp > 30) {
    return "Drink water"
  } else if (temp > 20) {
    return "Nice weather"
  } else {
    return "Bring a jacket"
  }
}

advice(35)
advice(25)
advice(10)
```

## And, Or, Not

Combine conditions:

```js
// AND: both must be true
if (age >= 18 && hasTicket) {
  console.log("You can enter")
}

// OR: at least one true
if (age < 12 || age >= 65) {
  console.log("Discount")
}

// NOT: flip
if (!hasTicket) {
  console.log("Buy a ticket")
}
```

| Symbol | Meaning |
|--------|---------|
| `&&` | AND |
| `\|\|` | OR |
| `!` | NOT |

## Real Example: Restaurant

```js
const getPrice = (item, isMember) => {
  if (item === "coffee") {
    if (isMember) {
      return 40
    } else {
      return 50
    }
  } else if (item === "tea") {
    if (isMember) {
      return 30
    } else {
      return 40
    }
  } else {
    return 0
  }
}

getPrice("coffee", true)   // 40
getPrice("coffee", false)  // 50
```

## Summary

* `if` / `else` / `else if` — make decisions
* `===` `>` `<` — compare values
* `&&` AND, `||` OR, `!` NOT
* Logic + Functions = smart functions

---

# ch03 HTML

## ch03 — HTML

Now we learn what a web page actually is

## What is HTML?

HTML is the structure of every web page:

```html
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello</h1>
    <p>This is a paragraph</p>
  </body>
</html>
```

* `<head>` — metadata (title)
* `<body>` — what you see on screen
* Each `<tag>` is an **element**

## Common Elements

| Element | What it does |
|---------|-------------|
| `<h1>` to `<h6>` | Headings (h1 biggest) |
| `<p>` | Paragraph |
| `<div>` | Container box |
| `<span>` | Inline container |
| `<a href="...">` | Link |
| `<img src="...">` | Image |
| `<button>` | Button |
| `<input>` | Text input |
| `<ul>` / `<li>` | List |

## Boxes Inside Boxes

HTML is layers of boxes:

```
html
├── head
│   └── title
└── body
    ├── h1
    ├── p
    └── div
        └── button
```

* `body` is the outer box
* `h1`, `p`, `div` are inside `body`
* `button` is inside `div`
* Like folders inside folders on your computer

## Create Your First HTML File

Create a file called `my-page.html`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Page</title>
</head>
<body>
  <h1>Hello World</h1>
  <p>This is my first web page!</p>
  <button>Click me</button>
</body>
</html>
```

Open it in your browser. You made a web page!

## Summary

* HTML = elements in a tree
* `<body>` is what you see
* Create a `.html` file → open in browser → done

---

# ch04 CSS Basics

## ch04 — CSS Basics

HTML is the structure. CSS makes it look good.

## What is CSS?

```css
h1 {
  color: red;
  font-size: 32px;
}
```

* `h1` — which element to style
* `color: red` — what to change
* The browser handles the rest

## Add CSS to HTML

Add `<style>` in `<head>`:

```html
<head>
  <title>My Page</title>
  <style>
    h1 { color: red; }
    p { font-size: 20px; }
    body {
      background: #1a1a2e;
      color: #eee;
      font-family: sans-serif;
    }
  </style>
</head>
```

## Colors

```css
color: red;              /* named */
color: #ff0000;          /* hex */
color: rgb(255, 0, 0);   /* rgb */
```

Common: `red`, `blue`, `green`, `white`, `black`, `gray`, `orange`

Try in F12:

```js
document.querySelector("h1").style.color = "red"
```

## Box Model

Every element is a box:

```
┌──────── margin ────────┐
│ ┌───── border ───────┐ │
│ │ ┌── padding ─────┐ │ │
│ │ │    content      │ │ │
│ │ └────────────────┘ │ │
│ └────────────────────┘ │
└────────────────────────┘
```

```css
div {
  padding: 10px;
  border: 1px solid white;
  margin: 20px;
}
```

## Style a Button

```css
button {
  font-size: 20px;
  padding: 10px 24px;
  border: 1px solid #eee;
  background: none;
  color: #eee;
  cursor: pointer;
  border-radius: 8px;
}
```

Copy this into your `<style>`. The button looks much better now.

## Summary

* CSS = selector `{ property: value; }`
* Colors: named, hex, rgb
* Box Model: padding → border → margin
* Add `<style>` in `<head>` to style your page

---

# ch05 DOM

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

## Summary

* `querySelector` — find an element
* `.textContent` — change text
* `.style` — change CSS
* `createElement` + `appendChild` — add new elements
* `.remove()` — delete elements

---

# ch06 Events

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

## Summary

* `addEventListener("click", () => { })` — respond to clicks
* Combine with DOM to update the page
* This is how all interactive websites work

---

# ch07 Project: Counter

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

## Summary

* One `.html` file = HTML + CSS + JS
* Start simple, add features step by step
* You just built a real interactive web app!

---

# ch08 Arrays

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

## Summary

* Array = list in `[ ]`
* Access with `[0]`, `[1]`, `[2]`...
* `.map(fn)` — apply function to every item
* Map is ch01 equations applied to lists

---

# ch09 Objects

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

## Summary

* Object = `{ key: value }` — describe a thing
* Access with `.key`
* Array of Objects = list of things
* `.map()` works on arrays of objects too

---

# ch10 Filter

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

## Summary

* `.filter(fn)` — keep items where fn returns true
* Works on numbers, strings, objects
* Combine with `.map()` for data pipelines
* filter uses ch02 logic (comparisons)

---

# ch11 Layout

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

## Summary

* `display: flex` — make children sit in a row
* `flex-direction: column` — stack vertically
* `justify-content: center` — center on main axis
* `align-items: center` — center on cross axis
* `gap` — spacing between items

---

# ch12 Project: Card List

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

## Summary

* Data (array of objects) → Functions (Card, render) → Page
* Filter buttons change what's displayed
* This is how real web apps work
* You built a menu filter app!

---

# ch13 Multiple Inputs

## ch13 — Multiple Inputs

Functions with more than one input

## Two Inputs

```js
const add = (x, y) => x + y

add(1, 2)   // 3
add(10, 20) // 30
```

```js
const area = (w, h) => w * h

area(3, 4)  // 12
area(5, 10) // 50
```

* 1 input: `x => ...`
* 2+ inputs: `(x, y) => ...`
* The `( )` is the only difference

## Three Inputs

```js
const volume = (w, h, d) => w * h * d

volume(2, 3, 4)  // 24
volume(10, 5, 2) // 100
```

```js
const fullName = (first, middle, last) =>
  first + " " + middle + " " + last

fullName("John", "F", "Kennedy")
// "John F Kennedy"
```

## Vectors

A vector is just an array: `[x, y, z]`

```js
const dot = (a, b) =>
  a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

dot([1,0,0], [0,1,0]) // 0
dot([1,0,0], [1,0,0]) // 1
```

```js
const cross = (a, b) => [
  a[1]*b[2] - a[2]*b[1],
  a[2]*b[0] - a[0]*b[2],
  a[0]*b[1] - a[1]*b[0]
]

cross([1,0,0], [0,1,0]) // [0, 0, 1]
```

## Summary

* 1 input: `x => ...`
* 2+ inputs: `(x, y) => ...`
* Works for any number of inputs

---

# ch14 Advanced Data

## ch14 — Advanced Data

More powerful ways to work with data

## Reduce

Combine all items into one value:

```js
[1, 2, 3, 4].reduce((total, x) => total + x, 0)
// 10
```

* `total` = running result
* `x` = current item
* `0` = starting value
* Step by step: `0+1=1 → 1+2=3 → 3+3=6 → 6+4=10`

## Reduce: More

```js
// total price
const prices = [50, 40, 120, 60]
prices.reduce((total, p) => total + p, 0)
// 270

// find max
[3, 1, 4, 1, 5].reduce((max, x) =>
  max > x ? max : x)
// 5
```

## Destructuring

Pull values out of an object:

```js
const person = { name: "Alice", age: 25 }

const { name, age } = person

name // "Alice"
age  // 25
```

Pull values out of an array:

```js
const [r, g, b] = [255, 128, 0]

r // 255
g // 128
b // 0
```

## Spread

Copy and merge arrays:

```js
const a = [1, 2, 3]
const b = [4, 5, 6]
const c = [...a, ...b]  // [1, 2, 3, 4, 5, 6]
```

Copy and update objects:

```js
const person = { name: "Alice", age: 25 }
const updated = { ...person, age: 26 }
// { name: "Alice", age: 26 }
```

The original is never changed.

## JSON

How data travels over the internet:

```js
const data = { name: "Alice", scores: [90, 85, 92] }

JSON.stringify(data)
// '{"name":"Alice","scores":[90,85,92]}'

JSON.parse('{"name":"Bob","age":30}')
// { name: "Bob", age: 30 }
```

## Summary

* **Reduce** — combine list into one value
* **Destructuring** — pull values out
* **Spread** `...` — copy and merge
* **JSON** — data format for the web

---

# ch15 Advanced Functions

## ch15 — Advanced Functions

Functions that are even more powerful

## Currying

A function that returns a function:

```js
const add = x => y => x + y

const add5 = add(5)
add5(3)  // 8
add5(10) // 15
```

Create specialized functions from general ones.

## Currying: Practical

```js
const multiply = x => y => x * y

const double = multiply(2)
const triple = multiply(3)

[1, 2, 3].map(double) // [2, 4, 6]
[1, 2, 3].map(triple) // [3, 6, 9]
```

## Closures

Inner function remembers outer variables:

```js
const counter = () => {
  let count = 0
  return () => {
    count = count + 1
    return count
  }
}

const c = counter()
c() // 1
c() // 2
c() // 3
```

## Clamp and Lerp

```js
const clamp = (value, min, max) =>
  Math.min(Math.max(value, min), max)

clamp(5, 0, 10)   // 5
clamp(-3, 0, 10)  // 0
clamp(99, 0, 10)  // 10
```

```js
const lerp = (a, b, t) => a + (b - a) * t

lerp(0, 100, 0.5) // 50
lerp(0, 100, 0.1) // 10
```

## Summary

* **Currying** — functions returning functions
* **Closures** — remembering variables
* **Clamp** — keep value in range
* **Lerp** — smooth interpolation

---

# ch16 Advanced CSS

## ch16 — Advanced CSS

## Grid

For 2D layouts:

```css
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}
```

## Responsive

Change layout based on screen size:

```css
.container { flex-direction: column; }

@media (min-width: 768px) {
  .container { flex-direction: row; }
}
```

| Name | Width |
|------|-------|
| Mobile | `< 768px` |
| Tablet | `768 - 1024px` |
| Desktop | `> 1024px` |

## Transitions

Smooth animations:

```css
button {
  background: blue;
  transition: background 0.3s;
}
button:hover {
  background: red;
}
```

## CSS Variables

```css
:root {
  --primary: #3498db;
  --bg: #1a1a2e;
}
h1 { color: var(--primary); }
body { background: var(--bg); }
```

Change one variable, everything updates.

## Summary

* **Grid** — 2D layout
* **Responsive** — adapt to screen size
* **Transitions** — smooth changes
* **CSS Variables** — reusable values
