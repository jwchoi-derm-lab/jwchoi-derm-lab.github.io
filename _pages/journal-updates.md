---
layout: archive
title: "Journal Updates (Academic Briefs)"
permalink: /journal-updates/
author_profile: true
---

Monthly literature reviews covering **JAAD, BJD, JAMA Dermatology, and JID**.

{% for post in site.posts %}
  <div>
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    <p><small>{{ post.date | date: "%B %d, %Y" }}</small></p>
    <p>{{ post.excerpt }}</p>
  </div>
  <hr>
{% endfor %}
