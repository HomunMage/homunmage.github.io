---
title: GameDesign

layout: practice
---


## Lists
<ul>
{% assign filter_pages = site.pages | where_exp: "page", "page.categories contains 'GameDesign'" %}
{% assign sorted_pages = filter_pages | sort: 'name' | reverse %}
{% for page in sorted_pages %}
    <li>
      <a href="{{ page.url | relative_url }}">{{ page.name }}</a>
    </li>
{% endfor %}
</ul>