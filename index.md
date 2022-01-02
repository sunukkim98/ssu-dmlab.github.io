---
layout: article
# titles:
  # @start locale config
  # en      : &EN       Welcome To Data Science Lab @ JBNU
  # @end locale config
---


<div class="video-container">
<iframe src="https://vasturiano.github.io/react-force-graph/example/large-graph/" allowfullscreen="" frameborder="0"></iframe>
<div id="main">
    <div id="typeStyle"></div>
</div>
</div>

## About DSLAB @ JBNU
<div style="hyphens: auto;">
Welcome to Data Science Laboratory in the Division of Computer Science and Engineering at Jeonbuk National University. 
Our research group is interested in data science with artificial intelligence and machine learning to develop effective and scalable algorithms for analyzing real-world data. 
We specifically study for understanding relationships between entities on graph data with interesting applications such as ranking, recommender system, and anomaly detection. 
</div>

## Announcement

{% for notice in site.data.announcements %}
<div class="item" id="largescreen">
  <div class="item__image">
      <i class="{{ notice.icon }} fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--primary button--rounded button--sm" 
                {% if notice.link != nil %}
                  href="{{ notice.link }}" target="_blank"
                {% endif %}
                >
                {{ notice.keyword }}
                </a> 
                {{ notice.content }}
            </div>
            <div class="cell cell--2" style="padding-left: 13px">
                <i class="far fa-calendar-alt fa-fw"></i> <span>{{ notice.date }}</span>
            </div>
        </div>
    </div>
  </div>
</div>

<!-- division for small screen-->
<div class="item" id="smallscreen">
  <div class="item__image">
      <i class="far fa-calendar-alt fa-fw"></i> <span>{{ notice.date }}</span>
      <a class="button button--{{ notice.button_color }} button--rounded button--sm" 
      {% if notice.link != nil %}
        href="{{ notice.link }}" target="_blank"
      {% endif %}
      >
      {{ notice.keyword }}
      </a>
  </div>  
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <i class="{{ notice.icon }} fa-fw"></i> 
                {{ notice.content }}
            </div>
        </div>
    </div>
  </div>
</div>

{% if forloop.last == false %}
<div class="mt-2" id="largescreen"></div>
<div class="mt-3" id="smallscreen"></div>
{% endif %}

{% endfor %}



## News

{% for news in site.data.news %}
<!-- division for large screen-->
<div class="item" id="largescreen">
  <div class="item__image">
      <i class="{{ news.icon }} fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--{{news.button_color}} button--rounded button--sm"
                {% if news.link != nil %}
                  href="{{ news.link }}" target="_blank"
                {% endif %}
                >
                {{ news.keyword }}
                </a> 
                {{ news.content }}
            </div>
            <div class="cell cell--2" style="padding-left: 13px;">
                <i class="far fa-calendar-alt fa-fw"> </i>
                <span>{{ news.date }}</span>
            </div>
        </div>
    </div>
  </div>
</div>

<!-- division for small screen-->
<div class="item" id="smallscreen">
  <div class="item__image">
      <i class="far fa-calendar-alt fa-fw"></i> <span>{{ news.date }}</span>
      <a class="button button--{{news.button_color}} button--rounded button--sm"
      {% if news.link != nil %}
        href="{{ news.link }}" target="_blank"
      {% endif %}  
      >
      {{ news.keyword }}
      </a>
  </div>  
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <i class="{{ news.icon }} fa-fw"></i> 
                {{ news.content }}
            </div>
        </div>
    </div>
  </div>
</div>

{% if forloop.last == false %}
<div class="mt-2" id="largescreen"></div>
<div class="mt-3" id="smallscreen"></div>
{% endif %}

{% endfor %}


## Contact Information

{% for contact in site.data.contact %}
<div class="item" id="largescreen">
  <div class="item__image">
      <i class="{{ contact.icon }} fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--success button--rounded button--sm">{{ contact.type }}</a> {{ contact.content}}
            </div>
        </div>
    </div>
  </div>
</div>

<div class="item" id="smallscreen">
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--success button--rounded button--sm">{{ contact.type }}</a> {{ contact.content}}
            </div>
        </div>
    </div>
  </div>
</div>
{% if forloop.last == false %}
<div class="mt-2"></div>
{% endif %}
{% endfor %}
