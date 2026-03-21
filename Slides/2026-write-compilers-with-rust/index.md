---
title: Write Compilers with Rust
layout: slides
---

## I Have a Dream

I want to create my own programming language.

Because every language has something I hate.

demo:
https://github.com/homun-lang/homun/releases


## Why 2026 Is the Right Time

Programming language syntax has been fully explored — no truly new paradigms left.

What remains is **engineering combination**: picking the best ideas and assembling them.

Before writing a single line of code, spent months discussing design with AI — iterating through trade-offs, edge cases, and syntax choices.

In 2026, designing a language is no longer about invention. It's about **curation**.

## What's Wrong with Languages

* C++ hooks LLVM to a frontend — stupid. ML family (OCaml, Haskell) is better for compilers
* C++ has huge breaking changes every version — `constexpr` scope differs across C++11/14/17/20
* Python syntax is nice, but lambda is single-line only — stupid
* Most languages use `.chaining()` not pipe — ugly in practice
* Rust lambda `|x| x*2` — ugly
* `=` vs `==` hell

## So I Want My Own Language

But making a language from scratch is too hard.

So start with a simpler example first.

## What Is a Compiler?


```
Source Code (text)
       │
       ▼
   Tokenizer      "if" "(" "x" ">" "0" ")"  →  tokens
       │
       ▼
   Parser          builds AST (Abstract Syntax Tree)
       │
       ▼
   AST             tree structure of the program
       │
       ▼
   IR              Intermediate Representation
       │
       ▼
   Backend         machine code / another language
```

## Tokenizer

Break source text into tokens:

```
"if (x > 0)"  →  [IF, LPAREN, IDENT("x"), GT, INT(0), RPAREN]
```

* Just string splitting — find keywords, symbols, literals
* No understanding of structure yet

## Parser → AST

Tokens → tree structure (Abstract Syntax Tree):

```
       IfStmt
      /      \
  Condition   Body
    /  |  \
   x   >   0
```

* Recursive descent — most common approach
* Each grammar rule = one function
* Tree captures the **meaning**, not the text

## AST → IR → Output

* **AST** = what the programmer wrote (structured)
* **IR** = intermediate form, easier to transform
* **Output** = target language or machine code

For Homun: AST → Rust source code (no IR needed, 1-to-1 transpile)

For mermaid-ascii: AST → Layout IR → ASCII art

## Mermaid-ASCII

Problem with current Mermaid: change one tiny thing, the entire layout shifts drastically.

Referenced existing repos: mermaid-ascii (Go), ascii-mermaid (TypeScript)

Wanted to try Rust — decided to write a compiler in Rust.

But Rust syntax is too complex. So first version written in Python, then ported to Rust.


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

<img src="./mermaid-arch.webp" style="max-width:90%; height:auto;">

## Mermaid-ASCII Results (cont.)

<img src="./mermaid-td.webp" style="max-width:90%; height:auto;">

## Back to the Real Dream

OK, mermaid-ascii works. Time for the real dream: **my own language**.

But I had no idea how painful this would be.

## Stuck for Months: Lambda Syntax Evolution

Spent months agonizing over syntax. Tried 

```
v0.1   lambda()              // too verbose
v0.3   () -> Type {}          // ok but messy
v0.6   \() -> Type {}         // Haskell-ish, weird
v0.7   || -> Type {}          // Rust-ish, ugly
v0.8   |params| -> Type {}    // still ugly
v0.13  (params) -> { body }   // ← finally! clean.
```


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

Every version felt wrong until `| (params) -> { body }`.

## The `.member` vs `.method` Nightmare

The deeper problem: how do you call methods on data?

* `player.hp` — field access
* `player.attack()` — method call
* `list.filter(...)` — method? field holding a function?

If `.` does both, you need `self`, `impl`, the whole OOP machine.

I kept going in circles. Every version felt wrong.

## Pipe Evolution: From `|>` to `|`

Also iterated on the pipe operator:

```
v0.4   |>              // F#/Elixir style, too long
v0.5   . (UFCS)        // ambiguous with field access
v0.12  newline-. pipe   // whitespace-sensitive = fragile
v0.13  |               // ← simple. explicit. done.
```

`.` is always field access. `|` is always pipe. No ambiguity. 

Finally:

```
res := @[1,2,3,4,5,6,7,8,9]
  | filter((x) -> { x % 2 == 0 })
  | map((x) -> { x * 2 })
  | reduce((x, y) -> { x + y })
```

## More Pain: 1-Base vs 0-Base

Initially wanted 1-based indexing — more intuitive for humans.

But then: should I write a full compiler from scratch?

...still too hard.

Learned from TypeScript & Svelte — just compile to Rust. Let Rust handle the hard parts.

But if I compile to Rust... Rust is 0-based. Translating 1-base to 0-base everywhere = nightmare.

Gave up on 1-base. Another dream killed by practicality.

## Write a Full Compiler? No — Transpile to Rust

Thought about it seriously. Kept coming back to: too hard.

Learned from TS (compiles to JS) and Svelte (compiles to JS):

**Just compile to Rust.** Don't try to be a real language. Be a transpiler.

Every valid Homun program transpiles 1-to-1 to Rust.

```
identity := (x) -> { x }
// becomes: fn identity<T>(x: T) -> T { x }
```

## Haskell POC → Rust Rewrite

Started with **Haskell** for the compiler (v0.23–v0.29):

* ML family is great for writing compilers (pattern matching, ADTs)
* Quickly validated: lexer → parser → sema → codegen pipeline works

But then: if Homun transpiles to Rust, the compiler should also be in Rust.

**v0.30**: full rewrite from Haskell to Rust. Same architecture, better ecosystem fit.

## Self-Hosting: .hom + .rs Mixed Source

Starting v0.60, the compiler compiles itself:

`.hom` = logic in Homun. `_imp.rs` = Rust helpers (FFI, state, I/O).

This is **hemi-self-hosting**: never fully self-host, always keep Rust as safety net.

## Auto-Detection Hell

Originally thought `:=` could auto-detect: rebind? reference? clone?

Sounded smart. Result: generated Rust code full of `Rc<RefCell<...>>`.

**Ugly. Unreadable. Tech debt everywhere.**

## The Fix: `::` in Parameters

Introduced `::` in parameter position to explicitly say "this is `&mut`":

```
// Before: auto-detect → Rc<RefCell<...>> everywhere
move := (pos, vel, dt) -> _ { ... }

// After: (pos::Position) = &mut, explicit and clean
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

## CI/CD: 2-Stage Update for Hemi-Self-Hosting

Hemi-self-hosting means **breaking syntax changes will happen**.

```
Stage 1: old syntax .hom + Rust core → build new compiler
Stage 2: update .hom to new syntax → compile again
```

* Stage 1: Rust core always compiles — it's the safety net
* Stage 2: migrate `.hom` to new syntax, recompile
* Fully self-hosting language would just break. Hemi = safe.

## Why Not Existing Scripting Solutions?

For game engines, current options all have problems:

* **Rhai (Bevy)** — dynamic, no type safety, performance overhead
* **Lua (mlua/rlua)** — need FFI binding glue, ecosystem split from Rust
* **GDScript** — locked to Godot, can't use with other engines

Homun: transpiles to Rust directly. Zero-cost abstraction. No FFI. No runtime overhead.

## Scoping Down: ECS Game Engine DSL

pipe + no-method struct + no self + transpile to Rust

This combination naturally fits **ECS game engines**:

Components = data structs. Systems = functions. No OOP needed.

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


## UVP: Homun = Rust Syntax Sugar

Homun is not trying to replace Rust. It **is** Rust — with nicer syntax.

* `:=` instead of `let` / `let mut`
* `(x) -> { body }` instead of `|x| body`
* `|` pipe instead of `.method()` chains
* `::` for `&mut` — explicit, no magic
* Structs hold data only — no `impl`, no `self`

Every `.hom` file transpiles to valid `.rs`. Always.

## Lessons Learned

1. **Prototype in a high-level language first** — Python for mermaid-ascii, Haskell for Homun POC
2. **Transpile, don't compile** — TS→JS, Svelte→JS, Homun→Rust. Standing on giants' shoulders.
3. **Auto-detection is a trap** — explicit `::` beats magic `Rc<RefCell<...>>`
4. **Hemi-self-hosting > full self-hosting** — safety net for breaking changes
5. **Design takes longer than implementation** — 22 spec versions before writing real code

## Demo

WASM playground: https://homun.posetmage.com/mermaid-ascii/

Homun playground: https://homun.posetmage.com/Homun-Lang/
