---
layout: article
title: ""
---

## About Seminar

In this seminar, we discuss diverse research topics such as data mining, graph machine learning, and applied data science including recommender systems. Here are the details of the seminar.

* Time: Every thursday, 19:00 - 20:00
* Place: 숭실대학교 정보과학관 301호

## Seminar Information

|Date|Title|Speaker|Slide|
|:---:|:---:|:---:|:---:|
{% for seminar in site.data.seminars -%}
{%- if forloop.first == true -%}
|{{seminar.date}}|`Upcoming` [{{seminar.title}}]({{seminar.paper}})|{{seminar.speaker}}| [[link]({{seminar.slide}})]
{%- else -%}
|{{seminar.date}}|[{{seminar.title}}]({{seminar.paper}})|{{seminar.speaker}}| [[link]({{seminar.slide}})]
{% endif %}
{% endfor %}