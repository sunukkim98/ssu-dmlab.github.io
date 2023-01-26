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

## Announcement
<div class="item">
  <div class="item__image">
      <i class="fas fa-star fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--info button--rounded button--sm" href="">Join Our Lab</a> 
                We are looking for graduate students who are enthusiastically interested in artificial intelligence and meachine learning for data science. Please click <a href="/recruitments/grad" target="_blank">[link]</a> if you're interested!
            </div>
        </div>
    </div>
  </div>
</div>

## Gradudate Students
<div class="article-list grid grid--sm grid--p-3">
    {% for member in site.data.members %}
    {% if member.type == "grad" %}
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

<!--
## Gradudate Students
<div class="article-list grid grid--sm grid--p-3">
    {% for member in site.data.members %}
    {% if member.type == "grad" %}
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
-->


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

## Alumni or Past Members
<div class="article-list grid grid--sm grid--p-3">
    {% for member in site.data.members %}
    {% if member.type == "undergrad_alumni" %}
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
