---
layout: article
title: ""
---

## About Seminar

In this seminar, we discuss diverse research topics such as data mining, graph machine learning, and applied data science including recommender systems. Here are the details of the seminar.

* Time: Every thursday
* Place: 숭실대학교 정보과학관 301호

## Seminar Information
{% assign now_in_seconds = site.time | date: '%s' | plus: 0 %}
{% assign one_week_from_now = now_in_seconds | plus: 604800 %}

{% assign sorted_seminars = site.data.seminars | sort: "Date" | reverse %}
{% assign grouped_seminars = sorted_seminars | group_by_exp: "item", "item.Date | date: '%Y'" %}

{% for group in grouped_seminars %}
### {{ group.name }}

|Date|Title|Speaker|Slide|
|:---:|:---:|:---:|:---:|
    {% for seminar in group.items -%}
        {% assign target_date_seconds = seminar.Date | date: '%s' | plus: 0 -%}
        {% if target_date_seconds < now_in_seconds and seminar.Title != "" -%}
|{{seminar.Date | date: "%y/%m/%d"}}|[{{seminar.Title}}]({{seminar.Paper.URL}})|{{seminar.Speaker}}| [[link]({{seminar.Slide.URL}})]|
        {% elsif target_date_seconds <= one_week_from_now and seminar.Title != "" -%}
|{{seminar.Date | date: "%y/%m/%d"}}|`Upcoming`<br> [{{seminar.Title}}]({{seminar.Paper.URL}})|{{seminar.Speaker}}| [[link]({{seminar.Slide.URL}})]|
        {% endif -%}
    {% endfor -%}
{% endfor %}