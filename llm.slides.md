# Slide Creation Guidelines

## Format

- Each `##` is one slide page
- Front matter has `title:` field
- No `<div class="slide">` wrappers

```md
---
title: Your Title
---

## Slide Title

content here

## Next Slide

content here
```

## Content Style

- Each slide should have enough content to actually teach from
- Use bullet points with explanations, not just single words
- Use **bold** for key terms
- Use tables for comparisons
- Use `code blocks` for code examples
- Use `inline code` for equations or short code references
- Use `>` blockquotes for key takeaways
- Use `####` for sub-sections within a slide
- Include images with `<img>` when relevant

## What a Good Slide Looks Like

- Has a clear title that tells you what this slide teaches
- Has 3-8 bullet points, or a table, or a code block with explanation
- Is self-contained — you can understand it without reading other slides
- Has enough context that the speaker can talk through it

## What a Bad Slide Looks Like

- Just a one-liner with no explanation
- Too much text (wall of text)
- No structure (no bullets, no code, no table)
- Title only, no content

## Equations

- Use inline code for equations: `f(x) = x + 1`
- No LaTeX, no MathJax, no KaTeX
- Keep equations readable as plain text

## Code Examples

- Use `js` code blocks for JavaScript
- Keep code short and focused
- Add comments `//` to show output when helpful
- No TypeScript unless the talk is specifically about TypeScript

## mermaid graph
use pattern like 
<!-- prettier-ignore -->
<mermaid-renderer>
graph LR
    ssot[SSOT Nodes]

    A[Modify Nodes]
    B[Modify Edges]
    
    A --modify--> ssot
    B --update--> ssot
    ssot --signals--> edges

    backend[Backend]

    ssot --"run graphs.json"--> backend

    outputs(("`LLM
      Outputs`"))
    backend --> outputs
</mermaid-renderer>

## Embedded Components

- YouTube: `<div class="embed_youtube" yt-title="title" yt-url="VIDEO_ID" yt-width="700">Loading content...</div>`
  - Requires: `<script src="https://posetmage.com/cdn/js/EmbedYoutubeVideo.js"></script>`
- Images: `<img src="./image.webp" width="600">`

## Slide Flow

- First slide: title + cover image or intro
- Middle slides: teach concepts progressively
- Last slide: summary or "Thank You"
