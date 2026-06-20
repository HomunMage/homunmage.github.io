---
title: Learn JS - 01 Functions, Logic, HTML, CSS
---

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

## ch01 Summary

* `f(x) = x + 1` → `const f = x => x + 1`
* `=>` is just `=`
* Same input always gives same output
* Combine small functions into bigger ones
* **F12 Console** is your playground

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

## ch02 Summary

* `if` / `else` / `else if` — make decisions
* `===` `>` `<` — compare values
* `&&` AND, `||` OR, `!` NOT
* Logic + Functions = smart functions

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

## ch03 Summary

* HTML = elements in a tree
* `<body>` is what you see
* Create a `.html` file → open in browser → done

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

## ch04 Summary

* CSS = selector `{ property: value; }`
* Colors: named, hex, rgb
* Box Model: padding → border → margin
* Add `<style>` in `<head>` to style your page
