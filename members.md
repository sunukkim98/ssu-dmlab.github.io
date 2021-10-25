---
layout: article
title: ""
---

## Professor
{% assign member = site.data.members[0] %}
<div class="article-list grid grid--sm grid--p-3">
    <div class="cell cell--4 cell--md-4 cell--lg-3">
        <a href="{{ member.link }}" target="_blank" style="text-decoration: none;">
            <div class="card card--clickable card--sm">
              <div class="card__image">
                <img class="image" src="/assets/images/profile/{{member.img}}"/>
              </div>
              <div class="card__content">
                <div class="card__header" style="text-decoration: none;">
                    <span>{{ member.name.en }}</span>
                </div>
              </div>
            </div>
        </a>
    </div>
    <div class="cell cell--4 cell--md-4 cell--lg-1">
    </div>
    <div class="cell cell--4 cell--md-4 cell--lg-1">
    </div>
    <div class="cell cell--4 cell--md-4 cell--lg-1">
    </div>
</div>


## Gradudate Students

<div class="item">
  <div class="item__image">
      <i class="fas fa-star fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--info button--rounded button--sm" href="">Join Our Lab</a> 
                Currently, we have no graduate student in our lab.
                I am looking for self-motivated graduate students and undergraduate students.
                Please click the buttom if you're interested!
            </div>
        </div>
    </div>
  </div>
</div>


## Undergraduate Students
<div class="article-list grid grid--sm grid--p-3">
    {% for member in site.data.members %}
    {% if member.type == "undergrad" %}
    <div class="cell cell--4 cell--md-4 cell--lg-3">
        <a href="{{ member.link }}" target="_blank" style="text-decoration: none;">
            <div class="card card--clickable card--sm">
              <div class="card__image">
                {% if member.img != nil %}
                    <img class="image" src="/assets/images/profile/{{member.img}}"/>
                {% else %}
                    <img class="image" src="/assets/images/profile/default-{{member.gender}}.png"/>
                {% endif %}
              </div>
              <div class="card__content">
                <div class="card__header" style="text-decoration: none;">
                    <span>{{ member.name.en }}</span>
                </div>
              </div>
            </div>
        </a>
    </div>
    {% endif %}
    {% endfor %}
</div>
