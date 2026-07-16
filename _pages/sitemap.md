---
layout: archive
title: "사이트맵"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

사이트에서 공개하는 페이지와 논문 목록입니다. 검색 엔진용
[XML 사이트맵]({{ base_path }}/sitemap.xml)도 제공합니다.

<h2>페이지</h2>
{% for post in site.pages %}
  {% include archive-single.html %}
{% endfor %}

{% capture written_label %}'None'{% endcapture %}

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
  {% capture label %}{{ collection.label }}{% endcapture %}
  {% if label != written_label %}
  <h2>{{ label }}</h2>
  {% capture written_label %}{{ label }}{% endcapture %}
  {% endif %}
{% endunless %}
{% for post in collection.docs %}
  {% unless collection.output == false or collection.label == "posts" %}
  {% include archive-single.html %}
  {% endunless %}
{% endfor %}
{% endfor %}
