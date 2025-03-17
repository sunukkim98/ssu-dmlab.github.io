---
layout: article
title: ""
---

{% if site.data.preprints != blank %}
## Preprints
{% endif %}

{% for paper in site.data.preprints %}
    {% if paper.international == true %}
<div class="grid">
  <div class="cell cell--auto">
	  <div style="font-size: 1.2em; font-weight: bolder;">{{paper.title}}</div>
	  <div style="font-size: 1em;">
        {% for author in paper.authors %}
            {% if forloop.last == true %}
                and {{ author }}
            {% else %}
                {{ author }},
            {% endif %}
        {% endfor %}
	  </div>
	  <div style="color: #606060; font-size: 1em;">
        {% if paper.publisher.link != nil %}
        <a href="{{ paper.publisher.link }}" style="color: #606060;" target="_blank">
            {{ paper.publisher.venue }}
        </a>
        {% else %}
            {{ paper.publisher.venue }}
        {% endif %}
	  </div>
	  <div style="font-size: 0.9em;">
        {% if paper.type == "conference" %}
            <a class="button button--info button--rounded button--sm">Conference</a>
        {% elsif paper.type == "journal" %}
            <a class="button button--primary button--rounded button--sm">Journal</a>
        {% elsif paper.type == "arxiv" %}
            <a class="button button--success button--rounded button--sm">Preprint</a>
        {% endif %}
        <i class="far fa-calendar-alt fa-fw"></i> {{ paper.month }} {{ paper.year }}
        {% if paper.pdf != nil %}
            <i class="fas fa-file-pdf fa-fw"></i><a href="{{ paper.pdf }}" style="color: #606060;" target="_blank">Paper</a>
        {% endif %}
        {% if paper.bib != nil %}
            <i class="fas fa-file-import fa-fw"></i><a href="{{ paper.bib }}"  style="color: #606060;" target="_blank">BibTex</a>
        {% endif %}
        {% if paper.slide != nil %}
            <i class="fas fa-file-powerpoint fa-fw"></i><a href="{{ paper.slide }}"  style="color: #606060;" target="_blank">Slide</a>
        {% endif %}
        {% if paper.code != nil %}
            <i class="fab fa-github-square fa-fw"></i><a href="{{ paper.code }}"  style="color: #606060;" target="_blank">Code</a>
        {% endif %}
	  </div>
  </div>
  <!--
  <div class="cell cell--shirink">
    {% if paper.type == "conference" %}
        <a class="button button--info button--rounded button--sm">Conference</a>
    {% elsif paper.type == "journal" %}
        <a class="button button--primary button--rounded button--sm">Journal</a>
    {% endif %}
  </div>
  -->
</div>

<div class="m-3"></div>
    {% endif %}
{% endfor %}


## International Conference

{% assign sorted_IC = site.data.international_conference | sort: 'Date' | reverse %}
{% for paper in sorted_IC %}
<div class="grid">
  <div class="cell cell--auto">
	  <div style="font-size: 1.2em; font-weight: bolder;">{{paper.Title}}</div>
	  <div style="font-size: 1em;">
        {% for author in paper.Authors %}
            {% if forloop.last == true %}
                and {{ author }}
            {% else %}
                {{ author }},
            {% endif %}
        {% endfor %}
	  </div>
	  <div style="color: #606060; font-size: 1em;">
        {% if paper.Venue.url != nil %}
        <a href="{{ paper.Venue.url }}" style="color: #606060;" target="_blank">
            {{ paper.Publisher }} {{ paper.FullVenue}} ({{ paper.Venue.text }}) {{paper.Year}}
        </a>
        {% else %}
            {{ paper.Publisher }} {{ paper.FullVenue}} ({{ paper.Venue.text }}) {{paper.Year}}
        {% endif %}
	  </div>
	  <div style="font-size: 0.9em;">
            <a class="button button--info button--rounded button--sm">Conference</a>
        <i class="far fa-calendar-alt fa-fw"></i> {{ paper.Date | date: "%b %Y" }}

        {% if paper.Paper.url != nil %}
            <i class="fas fa-file-pdf fa-fw"></i><a href="{{ paper.Paper.url }}" style="color: #606060;" target="_blank">Paper</a>
        {% endif %}
        {% if paper.BIB.url != nil %}
            <i class="fas fa-file-import fa-fw"></i><a href="{{ paper.BIB.url }}"  style="color: #606060;" target="_blank">BibTex</a>
        {% endif %}
        {% if paper.Slide.url != nil %}
            <i class="fas fa-file-powerpoint fa-fw"></i><a href="{{ paper.Slide.url }}"  style="color: #606060;" target="_blank">Slide</a>
        {% endif %}
        {% if paper.Code.url != nil %}
            <i class="fab fa-github-square fa-fw"></i><a href="{{ paper.Code.url }}"  style="color: #606060;" target="_blank">Code</a>
        {% endif %}
	  </div>
  </div>
  <!--
  <div class="cell cell--shirink">
    {% if paper.type == "conference" %}
        <a class="button button--info button--rounded button--sm">Conference</a>
    {% elsif paper.type == "journal" %}
        <a class="button button--primary button--rounded button--sm">Journal</a>
    {% endif %}
  </div>
  -->
</div>

<div class="m-3"></div>
{% endfor %}

## International Journal

{% assign sorted_IJ = site.data.international_journal | sort: 'Date' | reverse %}
{% for paper in sorted_IJ %}
<div class="grid">
  <div class="cell cell--auto">
	  <div style="font-size: 1.2em; font-weight: bolder;">{{paper.Title}}</div>
	  <div style="font-size: 1em;">
        {% for author in paper.Authors %}
            {% if forloop.last == true %}
                and {{ author }}
            {% else %}
                {{ author }},
            {% endif %}
        {% endfor %}
	  </div>
	  <div style="color: #606060; font-size: 1em;">
        {% if paper.Venue.url != nil %}
        <a href="{{ paper.Venue.url }}" style="color: #606060;" target="_blank">
            {{ paper.Publisher }} {{ paper.FullVenue}} ({{ paper.Venue.text }}) {{paper.Year}}
        </a>
        {% else %}
            {{ paper.Publisher }} {{ paper.FullVenue}} ({{ paper.Venue.text }}) {{paper.Year}}
        {% endif %}
	  </div>
	  <div style="font-size: 0.9em;">
            <a class="button button--primary button--rounded button--sm">Journal</a>
        <i class="far fa-calendar-alt fa-fw"></i> {{ paper.Date | date: "%b %Y" }}
        {% if paper.Paper.url != nil %}
            <i class="fas fa-file-pdf fa-fw"></i><a href="{{ paper.Paper.url }}" style="color: #606060;" target="_blank">Paper</a>
        {% endif %}
        {% if paper.BIB.url != nil %}
            <i class="fas fa-file-import fa-fw"></i><a href="{{ paper.BIB.url }}"  style="color: #606060;" target="_blank">BibTex</a>
        {% endif %}
        {% if paper.Slide.url != nil %}
            <i class="fas fa-file-powerpoint fa-fw"></i><a href="{{ paper.Slide.url }}"  style="color: #606060;" target="_blank">Slide</a>
        {% endif %}
        {% if paper.Code.url != nil %}
            <i class="fab fa-github-square fa-fw"></i><a href="{{ paper.Code.url }}"  style="color: #606060;" target="_blank">Code</a>
        {% endif %}
	  </div>
  </div>
  <!--
  <div class="cell cell--shirink">
    {% if paper.type == "conference" %}
        <a class="button button--info button--rounded button--sm">Conference</a>
    {% elsif paper.type == "journal" %}
        <a class="button button--primary button--rounded button--sm">Journal</a>
    {% endif %}
  </div>
  -->
</div>

<div class="m-3"></div>
{% endfor %}

## Domestic Conference

{% assign sorted_DC = site.data.domestic_conference | sort: 'Date' | reverse %}
{% for paper in sorted_DC %}
<div class="grid">
  <div class="cell cell--auto">
	  <div style="font-size: 1.2em; font-weight: bolder;">{{paper.Title.en}}</div>
	  <div style="font-size: 1em;">
        {% for author in paper.Authors %}
            {% if forloop.last == true %}
                and {{ author }}
            {% else %}
                {{ author }},
            {% endif %}
        {% endfor %}
	  </div>
	  <div style="color: #606060; font-size: 1em;">
        {% if paper.Venue.url != nil %}
        <a href="{{ paper.Venue.url }}" style="color: #606060;" target="_blank">
            {{ paper.Publisher }} {{ paper.FullVenue.en }} ({{ paper.Venue.text }}) {{paper.Year}}
        </a>
        {% else %}
            {{ paper.Publisher }} {{ paper.FullVenue.en }} ({{ paper.Venue.text }}) {{paper.Year}}
        {% endif %}
	  </div>
	  <div style="font-size: 0.9em;">
            <a class="button button--info button--rounded button--sm">Conference</a>
        <i class="far fa-calendar-alt fa-fw"></i> {{ paper.Date | date: "%b %Y" }}
        {% if paper.Paper.url != nil %}
            <i class="fas fa-file-pdf fa-fw"></i><a href="{{ paper.Paper.url }}" style="color: #606060;" target="_blank">Paper</a>
        {% endif %}
        <!-- {% if paper.bib != nil %}
            <i class="fas fa-file-import fa-fw"></i><a href="{{ paper.bib }}"  style="color: #606060;" target="_blank">BibTex</a>
        {% endif %} -->
        {% if paper.Slide.url != nil %}
            <i class="fas fa-file-powerpoint fa-fw"></i><a href="{{ paper.Slide.url }}"  style="color: #606060;" target="_blank">Slide</a>
        {% endif %}
        {% if paper.Code.url != nil %}
            <i class="fab fa-github-square fa-fw"></i><a href="{{ paper.Code.url }}"  style="color: #606060;" target="_blank">Code</a>
        {% endif %}
	  </div>
  </div>
  <!--
  <div class="cell cell--shirink">
    {% if paper.type == "conference" %}
        <a class="button button--info button--rounded button--sm">Conference</a>
    {% elsif paper.type == "journal" %}
        <a class="button button--primary button--rounded button--sm">Journal</a>
    {% endif %}
  </div>
  -->
</div>

<div class="m-3"></div>
{% endfor %}


<!--
## Domestic Publications


## Patents
-->
