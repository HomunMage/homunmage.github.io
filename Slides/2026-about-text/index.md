---
title: The Engineer's Familiar Stranger - Adventures with Text
---

## The Engineer's Familiar Stranger

Adventures with Text

We write code every day, but "text" has always been a hidden minefield.

## Self Introduction

PosetMage

* Software Engineer
* Personal website, blog, publishing — all DIY
* Fell into every text-processing trap so you don't have to

## Outline

1. PDF Layout Hell → Content vs Layout
2. Writing a Book in Markdown → Pipeline
3. Knowledge Management → Why Markdown
4. Blogging → Jekyll + Web Components
5. Japanese Game OCR → Screenshot Translation
6. Web Articles → TTS
7. Video Subtitles → Whisper

## Part 1: PDF Layout Hell

We've all been there:

* A perfectly formatted Word doc explodes on another machine
* Missing fonts, broken spacing, shifted images
* Mixing "content" with "layout" = disaster

## The Pitfall: Print to PDF

You think "just print to PDF" is easy?

* Linux server has no Chinese fonts installed → PDF full of tofu boxes `□□□`
* `apt-get install fonts-noto-cjk` — now you know this by heart
* Different OS renders different line breaks → pagination completely wrong
* WeasyPrint, wkhtmltopdf, Puppeteer — each has its own quirks

> The moment you realize "rendering text" is not trivial

## Solution: Separate Content from Layout

Split "what you write" from "how it looks"

* **LaTeX** — academic standard, precise but steep learning curve
* **HTML/CSS** — web tech for layout, the tool engineers know best

> Key insight: write content in plain text (Markdown), let template engines handle the rest

## Part 2: Writing a Book in Markdown?

Markdown is great for writing, but a book is more than one article.

You need a pipeline:

1. Multiple `.md` files → merge in chapter order
2. Convert formats → PDF / EPUB / HTML
3. Auto-generate TOC, page numbers, cross-references

## The Pitfalls of Book Pipeline

Sounds simple? Here's what actually happens:

* Pandoc converts `.md` → PDF, but CJK fonts break again
* Page breaks at wrong places — a heading sits alone at page bottom
* Image paths work locally but break after merge
* Cross-references between chapters? Good luck with relative links

> Every "simple conversion" hides 10 edge cases

## So I Built markbook

A Python pipeline that handles the mess for me:

* Define chapter structure, auto-merge
* Output to multiple formats
* Writing a book like writing code: version control + CI/CD

* [markbook](https://github.com/HomunMage/markbook)

## Part 3: Knowledge Management

Once you start writing in Markdown, you accumulate a LOT of files.

How do you organize hundreds of notes across different topics?

## The Problem: Knowledge Is Cross-Domain

Modern knowledge doesn't fit in folders:

```
Documents/
├── Work/
├── Personal/
└── Study/
    └── "AI for game design" — is this AI? Game? Design?
```

A single topic can span art, science, engineering, business simultaneously.

Traditional library classification (tree structure) breaks down.

## Tags > Folders

The answer: **tag-based** classification, not tree-based.

* One note can have multiple tags — lives in ALL categories at once
* Network structure matches how the brain actually works — neural networks
* AI (ChatGPT) can help auto-classify and suggest tags

```
note: "Rust WASM for game dev"
tags: [Rust, WASM, GameDev, WebDev]
  → belongs everywhere, not stuck in one folder
```

## Second Brain: References

Zettelkasten (卡片盒筆記法) — write atomic notes, link them into a knowledge web.

* ★★★★★ [我如何用第二大脑"记住"所有事情？｜老石谈芯](https://youtu.be/pjPgmaHIDAE)
* ★★★☆☆ [如何构造高效的知识管理系统](https://youtu.be/5Yn4-aSggI0)
* ★★★☆☆ [Zettelkasten 卡片盒笔记法](https://youtu.be/2VurHJtWKtk)

## Knowledge Management Tools

| Tool | Pros | Cons |
|------|------|------|
| **Confluence** | Team collaboration | Heavy, paid, vendor lock-in |
| **HackMD** | Real-time collab, Markdown | Cloud-dependent |
| **Roam Research** | Bidirectional links | Paid, proprietary format |
| **Obsidian** | Local-first, graph view | Plugin ecosystem fragile |
| **Logseq** | Open source, outliner | Smaller community |
| **Google Docs** | Everyone has it | Not Markdown, not portable |

All of these have one problem: **your data lives in their format**.

## Why Markdown Wins

* Simpler than Word — no formatting distractions, focus on content
* **You own the file** — it's just a `.md` text file
  * Move it anywhere: GitHub, USB, Dropbox, Obsidian
  * Edit with anything: VS Code, Sublime, Notepad, vim
  * Render anywhere: GitHub Pages, Jekyll, Hugo, or just `cat`
* Future-proof — plain text never becomes obsolete

> Word files from 2005 need special software. Markdown from 2005 still opens in Notepad.

## From Knowledge to Publishing

OK, knowledge management is solved: write `.md`, tag it, link it.

But **publishing** is a different beast. How do I turn Markdown into a website?

This is where the next decade of pain begins...

## Part 4: The Article Management Journey

Google Blogger → Medium → Obsidian → VS Code Foam → Jekyll

The path from renting a platform to owning your own words.

## Phase 1: Platform Era

* **Google Blogger** — easy, one-click publish, but zero control over layout
* **Medium** — great writing experience, beautiful typography

But problems appeared quickly:

* Content not portable, formatting breaks when migrating
* SEO has to start from scratch every time you move
* Locked in by the platform — feels like "renting a house"

> I wanted to OWN my content, not rent a platform.

## Phase 2: Note-Taking Tools

So I moved content to local tools:

* **Obsidian** — Markdown + local files, finally I own the data
* **VS Code + Foam** — wiki-style linking, lives in a git repo

Ownership problem solved! But new problem:

* These are personal knowledge bases, not publishing tools
* No public-facing output — how do readers see it?
* Still need a separate system for the actual website

## Phase 3: Jekyll — Own Everything

The answer: Markdown files in a git repo, Jekyll renders them into a website.

* Content is plain `.md` files — you own them forever
* Version control with git — full history, no lock-in
* GitHub Pages deploys for free — no server to manage

> Google Blogger → Medium → Obsidian → Foam → Jekyll: the path to owning your own words.

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

## So I Built Jekyll Layouts

* **Jekyll**: file system as routing, Markdown for content, zero-cost deployment
* **Web Components**: standard browser API, framework-agnostic, reusable
* **Svelte compile to WC**: great dev experience, outputs standard components
* Supports slides, notes, mindmaps — one content, multiple outputs

> This talk you're watching right now is rendered by this system.

* [Jekyll Layouts](https://github.com/PosetMage/jekyll_layouts)

## Part 5: I Just Want to Play Japanese Games

Playing a Japanese visual novel, the story looks amazing — but I can't read it.

* Copy text? Impossible — it's rendered in the game engine
* Google Translate camera? Unstable, slow, breaks immersion
* Fan translation patches? Not available for most games

> So I thought: what if I just screenshot and OCR it?

## OCR Pitfalls Nobody Warns You About

* Tesseract? Great for English, garbage for Japanese vertical text
* Game fonts are stylized — OCR engines choke on anti-aliased text
* Furigana (small reading hints above kanji) confuses the model
* Screenshot timing matters — dialogue boxes have animations

## So I Built JP_OCR_translate

After weeks of tuning: screenshot → OCR → translate pipeline that actually works

* OCR engine reads Japanese text from screen captures
* Auto-translates to Chinese
* Works for games, novels, and web pages

* [JP_OCR_translate](https://github.com/LatticeMage/JP_OCR_translate)

## Part 6: My Eyes Are Dying

I read a lot of long-form articles — blog posts, documentation, research.

* Sitting at a screen for 12 hours coding, then reading MORE text?
* I wanted to go for a walk and listen to articles like a podcast
* Browser read-aloud extensions? Robotic, can't handle code blocks, reads nav menus

> I just wanted someone to read the article to me. So I built it.

## TTS Pitfalls: Text Is Not What You Think

* HTML is not text — you need to strip nav, footer, ads, code blocks
* What about `<pre>` tags? You don't want TTS reading `console.log("hello")`
* CJK punctuation vs ASCII punctuation → different pause lengths
* Article behind a paywall or SPA? Good luck extracting content

The real challenge was never "text to speech" — it was "web page to clean text"

## So I Built Browser-TTS

* Extract article content from web pages, strip the junk
* Convert clean text to audio via TTS engine
* Play directly in the browser — no app install needed

* [Browser-TTS](https://github.com/LatticeMage/Browser-TTS)

## Part 7: I Want Subtitles on My Videos

Recording a talk or tutorial, but adding subtitles manually is torture.

* YouTube auto-captions? Decent for English, chaos for mixed-language content
* Professional subtitling services? Expensive for personal projects
* Manual transcription? Life is too short

> Whisper changed everything — but it's not magic

## Whisper Pitfalls: Close But Not Perfect

* Mixed language (English terms in Chinese speech) → model gets confused
* Speaker changes not detected — who said what?
* Timestamps drift on long recordings — subtitles slowly go out of sync
* Raw transcript has no punctuation, no paragraphs — a wall of text

Still needs post-processing: sentence splitting, timestamp correction, formatting

## Connecting the Dots

Every problem boils down to **text transformation and flow**

```
Audio ──Whisper──→ Text
Text ──Markdown──→ Book / Blog / Slides
Text ──TTS──→ Audio
Image ──OCR──→ Text ──Translate──→ Another Language
```

> Text seems simple until you actually try to process it. As engineers, we can automate these flows — and that's our superpower.

## Thank You!
