---
title: Selfhosted Visualizing AI Workflows with LangGraph-GUI & CrewAI-GUI
---

<div class="slide">

## Self-hosted AI Workflow Visualization with LangGraph-GUI & CrewAI-GUI


<img src="https://langgraph-gui.github.io/cover.webp" style="height: 400px;">

slide link: https://homun.posetmage.com/Content/Slides/2025/COSCUP/

</div>

<div class="slide">

## LangGraph-GUI Demo

<img src="./langgraph-gui-demo.gif">

* visulization, low code, easy to prompt
* simple for dev tools

</div>


<div class="slide">

## Motivation & Goals

1. **Local GPU Support** (e.g., Ollama)
2. **Full Customization** of UI and backend logic
3. **LangGraph Compatibility** for flexible graph-based workflows
4. **Easy Deployment** with Docker Compose and Kubernetes

other tool usually limited shape, you cannot drag some node to any node you want

* Other similar software
  * dify
    * <img src="https://framerusercontent.com/images/7IPPObp2xkFVLH1IyW9QvFQ0a2I.gif" width="600">
    * https://framerusercontent.com/images/7IPPObp2xkFVLH1IyW9QvFQ0a2I.gif
  * coze
    * <img src="https://pbs.twimg.com/media/GP5rEiZaEAAUqWu?format=jpg&name=4096x4096" width="600">
    * https://pbs.twimg.com/media/GP5rEiZaEAAUqWu
  * n8n
    * <img src="https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-screenshot-readme.png" width="600">
    * https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-screenshot-readme.png


</div>





<div class="slide">

## First attempts - CrewAI-Qt

Build CrewAI-GUI with pyside6

* **Pros** of CrewAI : 
  * Beginner-friendly introduction to AI agents
  * LangGraph, LangChain resource not friendly to green hands

<img src="../JSDC-LLM//crew-ai.webp" height="200">


<img src="./crewai-gui.gif">


<img src="https://raw.githubusercontent.com/LangGraph-GUI/CrewAI-GUI-Qt/refs/heads/main/frontend.webp" style="height: 400px;">

</div>

<div class="slide">

## Why Not CrewAI?


* **Cons** of CrewAI : 
  * Abstracts too many steps (limited visibility)
  * Frequent updates may breaks existing code
  * <img src="crewai-fail.webp" width="600">

</div>



<div class="slide">

## Abadon PyQt

- **Containerization Challenges:** Qt-based UIs proved unreliable when deployed in Docker/Kubernetes.
- **Frontend Modernization:** Switched from PySide6 to a React-based UI for faster iteration and broader ecosystem support.
- **Architecture Validation:** Demonstrated our JSON-contract design lets us swap out frontends with zero backend changes.

* frontend change:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Python_and_Qt.svg/164px-Python_and_Qt.svg.png" width="50">
-> <img src="https://avatars.githubusercontent.com/u/5429470?" width="50">
-> <img src="https://upload.wikimedia.org/wikipedia/commons/3/30/React_Logo_SVG.svg" width="50"> 
-> <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/Svelte_Logo.svg" width="50"> 


</div>

<div class="slide">

## Why Not LangChain?

Both langchain and  crewai are Fragility

* **Not Modularity:** Tool usage is isolated, hard to combine
* **Fragility:** Breaking changes across versions
* **Bad Abstraction:** Layers obscure data flow
<img src="abadon-langchain.webp" width="600">

[why we no longer use LangChain for building our AI agents](https://octomind.dev/blog/why-we-no-longer-use-langchain-for-building-our-ai-agents)

</div>


<div class="slide">

## Why Choose LangGraph

* Pros of LangGraph:
  * **Graph-Centric Design**: Focus on nodes and edges
  * **Model-Agnostic**: Plug in any LLM or agent
  * **Composable**: Mix-and-match components seamlessly

* My core recommand reason:
  * state machine concept align to LLM
  * very native
  * elegant, can loop, condition to change branch


* Learning Resource:
  * [LangGraph-GUI/LangGraph-learn](https://github.com/LangGraph-GUI/LangGraph-learn)

moreover we can do graph in graph like small agent but just use origin keywords



</div>


<div class="slide">

## Design of LangGraph-GUI

1. **JSON Contract**: text based, easy to decouple
2. **Frontend Agnostic**: ReactFlow, SvelteFlow, or custom
3. **Backend Flexible**: Python, etc.
4. **Extensible**: Add custom properties via `ext:` fields

* other design: subgraph:

<img src="subgraph.webp" width="300">


</div>

<div class="slide">

## Extend Ability

<img src="./extend-demo.gif">

</div>



<div class="slide">

## python backend

- **Framework Upgrade:** Started with Flask for its simplicity, then migrated to FastAPI for async support and superior performance.  
- **Declarative Routing:** Leveraged Python decorators to keep endpoint definitions clean and self-documented.  
- **Modular Extensions:** Easy to add features—JWT authentication, per-user workspaces, custom middleware.  
- **Developer-Friendly:** Clear JSON contract and pluggable modules make onboarding and iteration a breeze.


<img src="https://cdn.prod.website-files.com/63d926b37ec0d886c2d5d538/66bb668df8a571178f9bbe61_66964499d8592c7ca862b5ff_Flask-vs-FastAPI.png" width="400"><br/>image source: https://www.imaginarycloud.com/blog/flask-vs-fastapi

</div>


<div class="slide">

## DevOps

* Support Kubernetes
  * Ollama in NV-container

* Support Docker Compose
  * easy for local debug 



</div>


<div class="slide">

## Thank You!


</div>