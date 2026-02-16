---
title: ch01 Functional
---

## Learn Coding - ch01 Functional Programming

We start from equations, not syntax

* You don't need math background
* If you can understand `f(x) = x + 1`, you can learn FP
* FP = describing **rules**, not giving **commands**
* Open your browser, press **F12**, go to **Console** tab — that's where we run code

## Why Functional Programming?

Most beginners learn programming as "telling the computer what to do step by step"

* Imperative: do this, then do that, then check this...
* Functional: describe **what things are**

> A program is a rule, not an order.

#### Compare:

| Imperative | Functional |
|------------|------------|
| step-by-step instructions | rules and equations |
| change variables | transform values |
| hard to predict | easy to reason about |

## Equation = Function

Everyone already knows how equations work:

`f(x) = x + 1`

* **f** is the name
* **x** is the input
* **x + 1** is the rule
* input goes in, output comes out

This is already a function. That's it.

## Try It: Your First Code

`f(x) = x + 1` in JavaScript:

```js
const f = x => x + 1

f(1)   // 2
f(10)  // 11
f(100) // 101
```

Open F12 Console, paste it, press Enter. You just ran your first function.

## Define and Call

`double(x) = x * 2`

```js
const double = x => x * 2

double(3)  // 6
double(10) // 20
double(0)  // 0
```

* `const double` = the name
* `x` = the input
* `=>` = equals sign (think of it as `=`)
* `x * 2` = the rule

## More Examples

| Equation | JavaScript |
|----------|------------|
| `f(x) = x + 1` | `const f = x => x + 1` |
| `square(x) = x * x` | `const square = x => x * x` |
| `negate(x) = -x` | `const negate = x => -x` |

Try them all in F12 Console:

```js
const square = x => x * x
const negate = x => -x

square(5) // 25
negate(3) // -3
```

## Substitution

FP works because we can replace values like algebra:

```
double(5)
= 5 * 2
= 10
```

Verify in Console:

```js
const double = x => x * 2
double(5) // 10
```

* No hidden state
* No side effects
* Same input always gives same output

## Composition: Combining Functions

We can build bigger rules from smaller rules:

`f(x) = x + 1` , `g(x) = x * 2` , `h(x) = f(g(x))`

```js
const f = x => x + 1
const g = x => x * 2
const h = x => f(g(x))

h(3) // f(g(3)) = f(6) = 7
h(5) // f(g(5)) = f(10) = 11
```

* Small functions are easy to understand
* Combine them to build complex behavior
* Each piece can be tested independently

## Apply a Rule to Every Element

What if we want to apply a function to every item in a list?

```js
[1, 2, 3].map(x => x + 1)
// [2, 3, 4]

[1, 2, 3].map(x => x * 2)
// [2, 4, 6]

[1, 2, 3].map(x => x * x)
// [1, 4, 9]
```

* `.map()` applies a function to every element
* The function is just our equation
* No loops, no counters, no index variables

## Multiple Inputs

Functions can take more than one input:

`add(x, y) = x + y`

```js
const add = (x, y) => x + y

add(1, 2)   // 3
add(10, 20) // 30
```

`area(w, h) = w * h`

```js
const area = (w, h) => w * h

area(3, 4)  // 12
area(5, 10) // 50
```

When there are multiple inputs, wrap them in `( )`

## Multiple Inputs: Vectors

A vector is just an array: `[x, y, z]`

`dot(a, b) = a.x*b.x + a.y*b.y + a.z*b.z`

```js
const dot = (a, b) =>
  a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

dot([1,0,0], [0,1,0]) // 0  (perpendicular)
dot([1,0,0], [1,0,0]) // 1  (same direction)
```

`cross(a, b)` — cross product of two 3D vectors:

```js
const cross = (a, b) => [
  a[1]*b[2] - a[2]*b[1],
  a[2]*b[0] - a[0]*b[2],
  a[0]*b[1] - a[1]*b[0]
]

cross([1,0,0], [0,1,0]) // [0, 0, 1]
```

## Pattern: Single vs Multiple Inputs

| Inputs | Equation | JavaScript |
|--------|----------|------------|
| 1 | `f(x) = x + 1` | `const f = x => x + 1` |
| 2 | `add(x, y) = x + y` | `const add = (x, y) => x + y` |
| 3 | `rgb(r, g, b) = ...` | `const rgb = (r, g, b) => ...` |

* 1 input: `x => ...`
* 2+ inputs: `(x, y) => ...`
* The `( )` is the only difference

## Combine Everything

Define functions, compose them, apply to a list:

```js
const add1 = x => x + 1
const double = x => x * 2
const add1ThenDouble = x => double(add1(x))

[1, 2, 3].map(add1ThenDouble)
// [4, 6, 8]
```

Step by step: `1 → add1 → 2 → double → 4`

This is the core of functional programming.

## Filter: Keep What You Want

`.filter()` keeps elements that pass a test:

```js
[1, 2, 3, 4, 5].filter(x => x > 3)
// [4, 5]

[1, 2, 3, 4, 5].filter(x => x % 2 === 0)
// [2, 4]
```

The function returns `true` or `false` for each element

* `true` → keep it
* `false` → remove it

## Filter: More Examples

```js
const isPositive = x => x > 0
const isEven = x => x % 2 === 0

[-2, -1, 0, 1, 2].filter(isPositive)
// [1, 2]

[1, 2, 3, 4, 5, 6].filter(isEven)
// [2, 4, 6]
```

Notice: the filter function is just another equation

`isPositive(x) = x > 0`

## Reduce: Combine Into One Value

`.reduce()` combines all elements into a single result:

```js
[1, 2, 3, 4].reduce((acc, x) => acc + x, 0)
// 10
```

* `acc` = accumulator (the running result)
* `x` = current element
* `0` = starting value

Step by step: `0+1=1 → 1+2=3 → 3+3=6 → 6+4=10`

## Reduce: More Examples

```js
// multiply all elements
[1, 2, 3, 4].reduce((acc, x) => acc * x, 1)
// 24

// find max value
[3, 1, 4, 1, 5].reduce((acc, x) => acc > x ? acc : x)
// 5

// count items
[1, 2, 3, 4, 5].reduce((acc, x) => acc + 1, 0)
// 5
```

## Map, Filter, Reduce Together

Chain them to build powerful data pipelines:

```js
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  .filter(x => x % 2 === 0)   // [2, 4, 6, 8, 10]
  .map(x => x * x)            // [4, 16, 36, 64, 100]
  .reduce((acc, x) => acc + x, 0) // 220
```

* **filter** — pick which elements
* **map** — transform each element
* **reduce** — combine into one result

No loops, no variables, just functions.

## Advanced: clamp and lerp

`clamp(value, min, max)` — keep a value within range:

```js
const clamp = (value, min, max) =>
  Math.min(Math.max(value, min), max)

clamp(5, 0, 10)   // 5
clamp(-3, 0, 10)  // 0
clamp(99, 0, 10)  // 10
```

`lerp(a, b, t)` — linear interpolation between two values:

```js
const lerp = (a, b, t) => a + (b - a) * t

lerp(0, 100, 0.5) // 50
lerp(0, 100, 0.1) // 10
lerp(0, 100, 1)   // 100
```

## Summary

* **Equation** = Function: `f(x) = x + 1` → `const f = x => x + 1`
* **Substitution**: replace and simplify, like algebra
* **Composition**: build big functions from small functions
* **Map**: apply a function to every element in a list
* **F12 Console**: your playground to try everything

FP is describing rules, then combining and applying them.
