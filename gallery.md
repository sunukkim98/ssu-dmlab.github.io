---
layout: article
title: ""
---

## Photos

<div class="article-list grid grid--sm grid--p-3">
    {% for image in site.static_files reversed %}
        {% if image.path contains 'images/photos' %}
          <div class="cell cell--4 cell--md-4 cell--lg-3">
              <a href="{{ image.path }}" target="_blank" style="text-decoration: none;">
                  <div class="card card--clickable card--xl">
                    <div class="card__image">
                      <img class="image" src="{{ site.baseurl }} {{ image.path }}"/>
                    </div>
                  </div>
              </a>
          </div>
        {% endif %}
    {% endfor %}
</div>

