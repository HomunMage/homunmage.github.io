---
title: Learn JS - 04 Advanced Data, Functions, CSS
layout: slides
---

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

## ch13 Summary

* 1 input: `x => ...`
* 2+ inputs: `(x, y) => ...`
* Works for any number of inputs

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

## ch14 Summary

* **Reduce** — combine list into one value
* **Destructuring** — pull values out
* **Spread** `...` — copy and merge
* **JSON** — data format for the web

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

## ch15 Summary

* **Currying** — functions returning functions
* **Closures** — remembering variables
* **Clamp** — keep value in range
* **Lerp** — smooth interpolation

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

## ch16 Summary

* **Grid** — 2D layout
* **Responsive** — adapt to screen size
* **Transitions** — smooth changes
* **CSS Variables** — reusable values
