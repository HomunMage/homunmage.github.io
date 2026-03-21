---
title: Write Compilers with Rust
layout: slides
---

## I Have a Dream

I want to create my own programming language.

Because every language has something I hate.

demo:
https://github.com/homun-lang/homun/releases

## What's Wrong with Languages

* C++ hooks LLVM to a frontend — stupid. Claims to be the best compiler language, but actually the ML family (OCaml, Haskell) is better for compilers
* C++ has huge breaking changes every version — e.g. `constexpr` scope differs across C++11/14/17/20, not properly defined upfront
* Python syntax is nice, but lambda is single-line only — stupid. Python comprehension is actually bad practice
* Most languages use `.chaining()` not pipe — ugly in practice
* Rust lambda `|x| x*2` — ugly
* `=` vs `==` hell

## So I Want My Own Language

But making a language from scratch is too hard.

So start with a simpler example first.

## Mermaid-ASCII

Problem with current Mermaid: change one tiny thing, the entire layout shifts drastically.

Referenced existing repos:

* mermaid-ascii (Go)
* ascii-mermaid (TypeScript)

Also wanted to try Rust — major companies have been investing heavily in it the past two years.

Decided to write a compiler in Rust.

## But Rust Is Too Complex

Rust syntax is still too complex.

So the first version was written in Python.

## Compiler Pipeline

```
                    Mermaid DSL text
                           │
                           ▼
               ┌───────────────────────┐
               │  Tokenizer + Parser   │  parsers/registry.py
               │  (recursive descent)  │  parsers/flowchart.py
               └───────────┬───────────┘
                           │
       ┌───────────────────┼────────────────────┐
       │                   │                    │
       ▼                   ▼                    ▼
┌──────────────┐    ┌──────────────┐    ┌────────────────┐
│  Flowchart   │    │  Sequence    │    │ Architecture   │
│  AST         │    │  AST         │    │ AST            │
│  (current)   │    │  (future)    │    │ (future)       │
└──────┬───────┘    └──────┬───────┘    └───────┬────────┘
       │                   │                    │
       └───────────────┬───┴────────────────────┘
                       │
                       ▼
                ┌──────────────┐
                │  Layout IR   │
                │ LayoutNode[] │
                │ RoutedEdge[] │
                └──────┬───────┘
                       │
                 ┌─────┼─────┐
                 │           │
                 ▼           ▼
            ┌─────────┐ ┌─────────┐
            │  ASCII  │ │   SVG   │
            │Renderer │ │Renderer │
            │(current)│ │(future) │
            └─────────┘ └─────────┘
```

## Layout IR

Layout IR was designed after writing several versions — realized this design is better.

Can 1-to-1 output to ASCII or SVG.

## Python → Rust

```
Python (src/mermaid_ascii/)     Rust (src/rust/)
──────────────────────────      ─────────────────
parsers/flowchart.py            parsers/flowchart.rs
layout/sugiyama.py              layout/sugiyama.rs
layout/pathfinder.py            layout/pathfinder.rs
renderers/ascii.py              renderers/ascii.rs
api.py                          lib.rs
(no CLI)                        main.rs + wasm.rs
```

(Then plan to rewrite in my own language — Homun)

## Results

<img src="./mermaid-arch.webp" style="max-width:90%; height:auto;">

## Results (cont.)

<img src="./mermaid-td.webp" style="max-width:90%; height:auto;">

## Back to the Real Dream

OK, mermaid-ascii works. Time for the real dream: **my own language**.

But I had no idea how painful this would be.

## Stuck for Months: How Should Code Look?

Spent a very long time agonizing over syntax. Tried many approaches, none felt right.

The core question: how do you call methods on data?

```
// ts-like — .chaining()
res = [1,2,3,4,5,6,7,8,9]
  .filter(x -> x % 2 === 0)
  .map(x -> x * 2)
  .reduce((acc, x) -> acc + x, 0);

//rs-like — |ugly| lambdas
res = (1..=9)
    .filter(|x| x % 2 == 0)
    .map(|x| x * 2)
    .reduce(|a, b| a + b)
    .unwrap();
```

Both ugly. But what's the alternative?

## The `.member` vs `.method` Nightmare

Iterated over and over, trying to reconcile:

* `player.hp` — this is field access
* `player.attack()` — this is a method call
* `list.filter(...)` — is this a method? a field that holds a function?

If `.` does both, you need `self`, you need `impl`, you need the whole OOP machine.

I kept going in circles. Every version felt wrong.

## Giving Up on `.method()` — The Breakthrough

After many painful iterations, finally gave up on dot-chaining entirely.

Struct = no self. Can only hold data + fn signatures. Never methods.

**Pipe `|` replaces `.method()`**:

```
res := @[1,2,3,4,5,6,7,8,9]
  | filter((x) -> { x % 2 == 0 })
  | map((x) -> { x * 2 })
  | reduce((x, y) -> { x + y })
```

`.` is always field access. `|` is always pipe. No ambiguity. Finally.

## More Pain: 1-Base vs 0-Base

Initially wanted 1-based indexing — more intuitive for humans.

But then: should I write a full compiler from scratch?

...still too hard.

Learned from TypeScript & Svelte — just compile to Rust. Let Rust handle the hard parts.

But if I compile to Rust... Rust is 0-based. Translating 1-base to 0-base everywhere = nightmare.

Gave up on 1-base. Another dream killed by practicality.

## More Pain: Write a Full Compiler?

Thought about it seriously. Kept coming back to: too hard.

Learned from TS (compiles to JS) and Svelte (compiles to JS):

**Just compile to Rust.** Don't try to be a real language. Be a transpiler.

Every valid Homun program transpiles 1-to-1 to Rust.

```
identity := (x) -> { x }
// becomes: fn identity<T>(x: T) -> T { x }
```


## Yet Another Problem: Auto-Detection Hell

During `.hom` + `.rs` hemi-self-hosting, hit another wall.

Originally thought `:=` could auto-detect: rebind? reference? clone?

Sounded smart. Result: generated Rust code full of `Rc<RefCell<...>>`.

**Ugly. Unreadable. Tech debt everywhere.**

## The Fix: `::` in Parameters

Had to introduce `::` in parameter position to explicitly say "this is `&mut`":

```
// Before: auto-detect → Rc<RefCell<...>> everywhere
move := (pos, vel, dt) -> _ { ... }

// After: (p::Pos) = &mut, explicit and clean
move := (pos::Position, vel: Velocity, dt: float) -> _ {
  pos.x := pos.x + vel.dx * dt
}
```

Finally killed the `Rc<RefCell<...>>` tech debt.

## Svelte Had the Same Pain

Realized later: Svelte went through the exact same thing.

* **Svelte 4**: `let` magically auto-detects what becomes a reactive signal
* **Svelte 5**: gave up. Explicit `$state()` rune. You tell the compiler what's reactive.

Auto-detection sounds elegant. In practice it creates monsters.

## CI/CD: Needed Early for Hemi-Self-Hosting

Introduced GitHub Actions release pipeline early.

Why? Because hemi-self-hosting means **breaking syntax changes will happen**.

Need a safe way to evolve the language without breaking everything.

## 2-Stage Update

```
Stage 1: old syntax .hom + Rust core → build new compiler
Stage 2: update .hom to new syntax → compile again
```

* Stage 1: Rust core always compiles — it's the safety net
* Stage 2: migrate `.hom` to new syntax, recompile
* Fully self-hosting language would just break. Hemi = safe.


## Scoping Down: ECS Game Engine DSL

pipe + no-method struct + no self + transpile to Rust

Where does this combination actually make sense?

**ECS game engines.** Components = data structs. Systems = functions. No OOP needed.

UVP: **hemi-self-hosting** — Homun compiles to Rust, never fully self-hosts.

```
// Components — just data
Position := struct { x: float, y: float }
Velocity := struct { dx: float, dy: float }

// Systems — just functions, :: for mutation
move_system := (pos::Position, vel: Velocity, dt: float) -> _ {
  pos.x := pos.x + vel.dx * dt
  pos.y := pos.y + vel.dy * dt
}
```

No traits. No impl blocks. No derive macros.

## Demo

WASM playground: https://homun.posetmage.com/mermaid-ascii/

Homun playground: https://homun.posetmage.com/Homun-Lang/
