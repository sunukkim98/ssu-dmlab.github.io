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
Welcome to Data Science Laboratory in the Department of Computer Science and Engineering at Jeonbuk National University. Our research interests lie in artificial intelligence (AI), data mining, and machine learning to find models, algorithms, and systems for data analysis. Specifically, we focus on the following research topics: deep learning & machine learning, recommendation system, graphs/tensors, and financial AI.
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
                <a class="button button--primary button--rounded button--sm" href="">Join Our Lab!</a> 
                I am looking for self-motivated graduate students and undergraduate students.
                Please click the buttom if you're interested!
            </div>
            <div class="cell cell--2" style="padding-left: 13px">
                <i class="far fa-calendar-alt fa-fw"></i> <span>Oct 23, 2021</span>
            </div>
        </div>
    </div>
  </div>
</div>

## News

{% for news in site.data.news %}
<div class="item">
  <div class="item__image">
      <i class="{{ news.icon }} fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--{{news.button_color}} button--rounded button--sm">
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
{% if forloop.last == false %}
<div class="mt-2"></div>
{% endif %}

{% endfor %}


## Contact Information


<div class="item">
  <div class="item__image">
      <i class="fas fa-phone fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--success button--rounded button--sm">Phone</a> +82–63–270–3402
            </div>
        </div>
    </div>
  </div>
</div>

<div class="mt-2"></div>

<div class="item">
  <div class="item__image">
      <i class="fas fa-inbox fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--success button--rounded button--sm">E-mail</a> jinhongjung (at) jbnu.ac.kr
            </div>
        </div>
    </div>
  </div>
</div>

<div class="mt-2"></div>

<div class="item">
  <div class="item__image">
      <i class="fas fa-location-arrow fa-fw"></i>
  </div>
  <div class="item__content">
    <div class="item__header">
        <div class="grid">
            <div class="cell cell--auto">
                <a class="button button--success button--rounded button--sm" href="https://goo.gl/maps/zkKZAcivanuTbdFa6" target="_blank">Address</a> Room 627, Engineering Building 7, Jeonbuk National University, 567 Baekje-daero, Jeonju
            </div>
        </div>
    </div>
  </div>
</div>
