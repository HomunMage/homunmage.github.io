---
title: Compile Mermaid to ASCII Art
---

## Why Mermaid to ASCII?

- **Mermaid** is the most popular text-based diagram syntax (GitHub, Notion, Obsidian)
- But rendering requires a browser + JavaScript runtime
- **Goal**: compile Mermaid DSL directly to ASCII/Unicode art — runs anywhere
- Terminal, CI logs, code comments, plain-text docs — no browser needed

```
echo 'graph TD
    A --> B --> C' | mermaid-ascii

┌───┐
│ A │
└─┬─┘
  │
  ▼
┌───┐
│ B │
└─┬─┘
  │
  ▼
┌───┐
│ C │
└───┘
```

## Why Rust?

- First attempt: **Python** prototype — fast to develop, works great
- But distributing Python binaries is painful:
  - PyInstaller, Docker multi-platform builds, QEMU emulation
  - macOS, Windows, Linux each need different CI pipelines
- **Rust** compiles to a single static binary — one Dockerfile, cross-compile everything
- Also enables **WASM** target for browser playground with `wasm-bindgen`

> Prototype in Python, ship in Rust

## Compiler Pipeline

- Treat it as a **multi-phase compiler** — each phase transforms one representation to the next
- Designed to support **multiple diagram types** (flowchart now, sequence/architecture future)
- All diagram types output the same **Layout IR** — renderers don't change

```
Mermaid DSL text
       │
       ▼
  Tokenizer + Parser (recursive descent)
       │
       ├─── Flowchart AST (current)
       ├─── Sequence AST  (future)
       └─── Architecture AST (future)
              │
              ▼
    Layout engine (Sugiyama / timeline / force)
              │
              ▼
       Layout IR (LayoutResult)
       LayoutNode[] + RoutedEdge[]
              │
              ├─── ASCII Renderer (current)
              └─── SVG Renderer  (future)
```

## AST Graph (Parser Output)

- **Recursive descent parser** — no regex line-by-line, handles chained edges `A --> B --> C`
- Supports: 4 node shapes, 9 edge types, subgraphs, multi-line labels, comments
- Parser outputs an **AST Graph** — the structured representation of the diagram

```
Graph {
    nodes:     Node[]      # id, label, shape
    edges:     Edge[]      # from, to, edge_type, label
    subgraphs: Subgraph[]  # nested groups
    direction: Direction   # TD | BT | LR | RL
}
```

- Each diagram type (flowchart, sequence, etc.) has its **own AST** and its **own parser**
- Registry pattern: `detect_type()` dispatches to the right parser

## Sugiyama Layout Algorithm

- Classic **layered graph drawing** algorithm — used by Graphviz, Dagre, ELK
- 8 phases transform the AST Graph into positioned Layout IR:

| Phase | Algorithm | Purpose |
|-------|-----------|---------|
| 1. `collapse_subgraphs()` | — | Replace subgraph members with compound node |
| 2. `remove_cycles()` | Greedy-FAS | Reverse back-edges to make a DAG |
| 3. `assign_layers()` | Longest-path | Assign each node a rank (layer) |
| 4. `insert_dummy_nodes()` | — | Break multi-layer edges into unit segments |
| 5. `minimise_crossings()` | Barycenter (24-pass) | Reorder nodes within layers to reduce edge crossings |
| 6. `assign_coordinates()` | Layer centering | Compute x,y positions with refinement |
| 7. `expand_compound_nodes()` | — | Position subgraph members inside compounds |
| 8. `route_edges()` | **A* pathfinding** | Compute waypoints avoiding obstacles |

## A* Pathfinding for Edge Routing

- After Sugiyama places nodes, edges need **routed paths** that avoid overlapping nodes
- Build an **OccupancyGrid** — 2D boolean grid marking which cells are blocked by node boxes
- Run **A* search** from edge source to edge target on this grid

#### How it works:

- **Heuristic**: Manhattan distance with +1 corner penalty — prefers straight paths
- **4-directional** movement (up/down/left/right) — produces orthogonal routes
- **Goal exception**: target cell allowed to be blocked (it's on a node border)
- **Path simplification**: remove collinear intermediate points, keep only direction changes

```
OccupancyGrid (. = free, # = blocked by node)

. . . . . . . . .
. # # # . # # # .
. # A # . # B # .     A* finds path: down, across, up
. # # # . # # # .     Simplified to 3 waypoints
. . . * * * . . .
. . . . . . . . .
```

> Every edge in the final output was routed by A* — no overlapping, no crossing through nodes

## Layout IR (The Boundary)

- **Layout IR** = `LayoutResult` — the contract between layout and rendering
- All diagram types produce the same Layout IR — renderers are diagram-agnostic
- This is the key architectural decision: **one IR, multiple frontends and backends**

```
LayoutResult {
    nodes:  LayoutNode[]    # x, y, width, height, label, shape
    edges:  RoutedEdge[]    # waypoints (from A*), edge_type, label
    direction: Direction
}
```

- `LayoutNode` = positioned box in character coordinates
- `RoutedEdge` = list of `Point` waypoints (orthogonal path segments from A*)
- Adding a new renderer (SVG, HTML) just means consuming this same IR

## ASCII Renderer (7 Phases)

- Takes Layout IR, paints to a **Canvas** (2D character grid)
- Handles 4 directions (TD, BT, LR, RL) via **geometry transforms**

| Phase | What it does |
|-------|-------------|
| 1. Direction transform | Transpose x/y for LR/RL |
| 2. Paint subgraph borders | Compound node boxes |
| 3. Paint node boxes | Shape-aware: `┌┐└┘` rect, `╭╮╰╯` rounded, `/\` diamond, `()` circle |
| 4. Paint edges | Solid `─│`, dotted `╌╎`, thick `═║` with smart junction merging |
| 5. Paint arrowheads | `▼ ▲ ► ◄` outside boxes + edge labels at midpoint |
| 6. Paint exit stubs | `┬ ┴ ├ ┤` on source node borders |
| 7. Direction flip | Reverse rows for BT, reverse cols for RL |

## Comparison with Other Tools

```
┌──────────────┬──────────────────┬──────────────────┬──────────────────┬──────────────────┐
│              │ Ours             │ Go (mermaid-     │ TS (ascii-       │ D2               │
│              │                  │ ascii)           │ mermaid)         │                  │
├──────────────┼──────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Parser       │ Recursive        │ Regex            │ Regex            │ Custom DSL       │
│              │ descent          │ line-by-line     │ line-by-line     │ parser           │
├──────────────┼──────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Layout       │ Sugiyama (full)  │ Grid BFS + A*    │ Grid BFS + A*    │ Dagre / ELK      │
├──────────────┼──────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Crossing Min │ Barycenter       │ None             │ None             │ Barycenter       │
│              │ 24-pass          │                  │                  │ (via Dagre)      │
├──────────────┼──────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Edge Routing │ A* pathfinding   │ A* pathfinding   │ A* pathfinding   │ Spline curves    │
├──────────────┼──────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Node Shapes  │ 4                │ 1 (rect only)    │ 13               │ Many             │
├──────────────┼──────────────────┼──────────────────┼──────────────────┼──────────────────┤
│ Target       │ ASCII/Unicode    │ ASCII/Unicode    │ ASCII/Unicode    │ SVG              │
└──────────────┴──────────────────┴──────────────────┴──────────────────┴──────────────────┘
```

## Dual-Language Architecture

- **Python** = prototype + ground truth (fast iteration with `pytest`)
- **Rust** = production binary + WASM (single static binary, cross-platform)
- 1:1 module mapping — every Python file has a Rust counterpart

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

> Iterate fast in Python, ship in Rust, play in WASM

## Demo

```
cat <<'EOF' | mermaid-ascii
graph TD
    Start[Start] --> Decision{Decision}
    Decision -->|yes| ProcessA[Process A]
    Decision -->|no| ProcessB[Process B]
    ProcessA --> End[End]
    ProcessB --> End
EOF

          ┌───────┐
          │ Start │
          └───┬───┘
              │
              ▼
        /──────────\
        │ Decision │
        \─────┬────/
      yes     │        no
      ┌───────┴────────┐
      ▼                ▼
┌───────────┐    ┌───────────┐
│ Process A │    │ Process B │
└─────┬─────┘    └─────┬─────┘
      │                │
      └───────┬────────┘
              ▼
           ┌─────┐
           │ End │
           └─────┘
```

WASM playground: https://homun.posetmage.com/mermaid-ascii/
