---
title: Why I use Jekyll + WC
---

## Why I use Jekyll + Web Components

A decade of trial and error to find the right architecture

## The Beginning: Blog Platforms

Like most people, I started with popular platforms:

* **Google Blogger** — easy, one-click publish
* **Medium** — great writing experience

But problems appeared quickly:

* Content not portable, formatting breaks when migrating
* SEO has to start from scratch
* Locked in by the platform — feels like "renting a house"

> I wanted my own land, my own house.

## First Attempt: Pure GitHub

Map routes directly to file system structure:

```
home/README.md        → homepage
about/README.md       → about me
tech/linux/README.md  → tech articles
```

* No backend, no render loop
* Raw HTTP file serving
* Simple, direct, ugly but functional

## The Pain of Pure GitHub

"Raw" quickly became painful:

* No shared navbar — copy-paste HTML header for every article
* No style management — the whole site looked like a 1990s bulletin board
* Maintenance cost grows linearly with number of articles

## Entering Jekyll

Jekyll gave me my first taste of **Template** power

* Apply a theme, site instantly looks professional
* Write content in Markdown, Jekyll handles structure
* Deploy on GitHub Pages for free

But as my needs grew, so did the pain...

## Jekyll's Bottleneck

I wanted interactive charts and dynamic code demos in my articles

In Jekyll's world, this is a disaster:

* Must create HTML in `_includes/`, filled with `<script>` tags and Liquid logic
* Use awkward syntax to call it from Markdown
* Project structure becomes spaghetti:
  * Markdown mixed with Liquid tags
  * HTML mixed with JavaScript logic
  * JS depends on Liquid-injected variables

Changing a chart's color means opening Markdown, HTML layout, and CSS files simultaneously

## Trying Other Frameworks

| Framework | Pros | Cons |
|-----------|------|------|
| **Hugo** | Extremely fast | Template syntax complex, Liquid is easier |
| **Gatsby** | React ecosystem | Too heavy, Webpack + GraphQL setup drains all energy |
| **MDsveX** | Svelte integration | Only works in specific folders, no flexible structure |
| **SvelteKit** | Closest to auto md → html | Folder structure still less flexible than Jekyll |

SvelteKit's closest approach:

```
src/
├── routes/
│   ├── blog/[slug]/
│   └── docs/[slug]/
├── content/
│   ├── blog/
│   └── docs/
└── lib/
```

But folder structure is still not flexible enough

## Discovering Web Components + Svelte

First time experiencing the real power of **Separation of Concerns**

* Tried **Lit** for WC — felt extremely unnatural to write
* Discovered **Svelte can also compile as WC**

Write a clean component in Svelte, compile to standard Web Component

In Markdown, just write:

```html
<my-chart data="[1,2,3]"></my-chart>
```

## Jekyll + WC = Islands Architecture

Jekyll becomes a **content routing shell**

Svelte takes over all **interactive logic**

* Markdown handles storytelling
* Components handle the magic
* They don't interfere with each other

> This is the modern Islands Architecture concept. Astro is the ultimate expression of this idea.

But in the end, Jekyll + WC is the most flexible.

## Conclusion: Why Jekyll + WC

* **Jekyll**: file system as routing, Markdown for content, zero-cost deployment
* **Web Components**: standard browser API, framework-agnostic, reusable
* **Svelte compile to WC**: great dev experience, outputs standard components

> No complex frameworks, no build pipeline
> Just Markdown + standard Web Components

## Thank You!
