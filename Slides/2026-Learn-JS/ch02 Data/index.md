---
title: ch02 Data
---

## ch02 Data Structures & Higher-Order Functions

In ch01 we learned how to transform data with functions

Now we learn what data looks like, and how to build powerful functions

## Arrays

An array is a list of values: `[1, 2, 3]`

```js
const nums = [1, 2, 3, 4, 5]
const names = ["Alice", "Bob", "Charlie"]
const mixed = [1, "hello", true]

nums[0]    // 1  (first element)
nums[2]    // 3  (third element)
nums.length // 5
```

* Index starts from `0`, not `1`
* Arrays can hold any type of value
* We already used arrays with `.map()` and `.filter()`

## Objects

An object is a collection of key-value pairs: `{}`

```js
const person = {
  name: "Alice",
  age: 25,
  city: "Taipei"
}

person.name // "Alice"
person.age  // 25
```

* Access values with `.key`
* Like a dictionary: look up by name, get a value

## Arrays of Objects

This is how real-world data looks:

```js
const users = [
  { name: "Alice", age: 25 },
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 20 }
]

users[0].name // "Alice"
users[1].age  // 30
```

Now we can combine with ch01:

```js
users.map(u => u.name)
// ["Alice", "Bob", "Charlie"]

users.filter(u => u.age >= 25)
// [{ name: "Alice", age: 25 }, { name: "Bob", age: 30 }]
```

## Map + Filter on Real Data

```js
const products = [
  { name: "Phone", price: 999 },
  { name: "Cable", price: 10 },
  { name: "Laptop", price: 1500 },
  { name: "Mouse", price: 25 }
]

// get names of expensive items
products
  .filter(p => p.price > 100)
  .map(p => p.name)
// ["Phone", "Laptop"]

// total price of cheap items
products
  .filter(p => p.price <= 100)
  .reduce((acc, p) => acc + p.price, 0)
// 35
```

## Destructuring: Objects

Pull values out of an object into variables:

```js
const person = { name: "Alice", age: 25, city: "Taipei" }

const { name, age } = person

name // "Alice"
age  // 25
```

Very useful in function parameters:

```js
const greet = ({ name, age }) =>
  name + " is " + age + " years old"

greet(person) // "Alice is 25 years old"
```

## Destructuring: Arrays

Pull values out of an array by position:

```js
const rgb = [255, 128, 0]

const [r, g, b] = rgb

r // 255
g // 128
b // 0
```

Skip values with `,`:

```js
const [first, , third] = [10, 20, 30]

first // 10
third // 30
```

## Spread: Arrays

`...` spreads an array into individual elements:

```js
const a = [1, 2, 3]
const b = [4, 5, 6]

const c = [...a, ...b]
// [1, 2, 3, 4, 5, 6]

const d = [0, ...a, 99]
// [0, 1, 2, 3, 99]
```

* Copy an array: `const copy = [...original]`
* Merge arrays without mutating the original

## Spread: Objects

`...` also works with objects:

```js
const person = { name: "Alice", age: 25 }

const updated = { ...person, age: 26 }
// { name: "Alice", age: 26 }

const withCity = { ...person, city: "Taipei" }
// { name: "Alice", age: 25, city: "Taipei" }
```

* Create a new object with some fields changed
* The original is never modified — this is the FP way

## JSON

JSON = JavaScript Object Notation

```js
const data = { name: "Alice", scores: [90, 85, 92] }

// object → string
const str = JSON.stringify(data)
// '{"name":"Alice","scores":[90,85,92]}'

// string → object
const obj = JSON.parse(str)
obj.name     // "Alice"
obj.scores   // [90, 85, 92]
```

* JSON is how data travels over the internet (APIs)
* It looks exactly like JS objects (that's where the name comes from)

## Higher-Order Functions

A function can take another function as input — we already know this:

```js
[1, 2, 3].map(x => x * 2)
```

`.map()` is a higher-order function — it takes `x => x * 2` as input

A function can also **return** a function:

```js
const add = x => y => x + y

const add5 = add(5)
add5(3)  // 8
add5(10) // 15
```

## Currying

When a function returns a function, it's called **currying**:

`add(x, y) = x + y` → `add(x)(y) = x + y`

```js
// normal
const add = (x, y) => x + y
add(3, 5) // 8

// curried
const addC = x => y => x + y
addC(3)(5) // 8

// partial application
const add10 = addC(10)
add10(1) // 11
add10(5) // 15
```

Why? We can create specialized functions from general ones.

## Currying: Practical Example

```js
const multiply = x => y => x * y

const double = multiply(2)
const triple = multiply(3)

[1, 2, 3].map(double) // [2, 4, 6]
[1, 2, 3].map(triple) // [3, 6, 9]
```

```js
const greaterThan = min => x => x > min

const above18 = greaterThan(18)
const above100 = greaterThan(100)

[10, 20, 30].filter(above18)  // [20, 30]
[50, 150, 200].filter(above100) // [150, 200]
```

Create reusable filters and transformers with currying.

## Closures

When a function returns a function, the inner function **remembers** the outer variables:

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

* `count` lives inside `counter`, hidden from outside
* The inner function "closes over" `count` — that's a **closure**

## Build Your Own Map

`.map()` is not magic — it's just a function:

```js
const myMap = (arr, fn) =>
  arr.reduce((acc, x) => [...acc, fn(x)], [])

myMap([1, 2, 3], x => x * 2)
// [2, 4, 6]
```

## Build Your Own Filter

```js
const myFilter = (arr, fn) =>
  arr.reduce((acc, x) =>
    fn(x) ? [...acc, x] : acc, [])

myFilter([1, 2, 3, 4, 5], x => x > 3)
// [4, 5]
```

map, filter, reduce — **reduce** is the most powerful. You can build everything with it.

## Summary

* **Arrays** `[]` — ordered list of values
* **Objects** `{}` — key-value pairs
* **Destructuring** — pull values out: `const { name } = obj`
* **Spread** `...` — copy and merge without mutation
* **JSON** — data format for the web
* **Higher-Order Functions** — functions that take or return functions
* **Currying** — `x => y => x + y` create specialized functions
* **Closures** — inner functions remember outer variables
