---
layout: article
titles:
  # @start locale config
  en      : &EN       
---

## International Publications


{% for paper in site.data.papers %}
    {% if paper.international == true %}
<div class="grid">
  <div class="cell cell--auto">
	  <div style="font-size: 22px; font-weight: bolder;">{{paper.title}}</div>
	  <div style="font-size: 20px;">
        {% for author in paper.authors %}
            {% if forloop.last == true %}
                and {{ author }}
            {% else %}
                {{ author }},
            {% endif %}
        {% endfor %}
	  </div>
	  <div style="color: #606060;">
        {% if paper.publisher.link != nil %}
        <a href="{{ paper.publisher.link }}" style="color: #606060;" target="_blank">
            {{ paper.publisher.venue }}
        </a>
        {% else %}
            {{ paper.publisher.venue }}
        {% endif %}
	  </div>
	  <div>
        {% if paper.type == "conference" %}
            <a class="button button--info button--rounded button--sm">Conference</a>
        {% elsif paper.type == "journal" %}
            <a class="button button--primary button--rounded button--sm">Journal</a>
        {% endif %}
        <i class="far fa-calendar-alt fa-fw"></i> {{ paper.month }} {{ paper.year }}
        {% if paper.pdf != nil %}
            <i class="fas fa-file-pdf fa-fw"></i><a href="{{ paper.pdf }}" style="color: #606060;" target="_blank">Paper</a>
        {% endif %}
        {% if paper.bib != nil %}
            <i class="fas fa-file-import fa-fw"></i><a href="{{ paper.bib }}"  style="color: #606060;" target="_blank">BibTex</a>
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


<!--
## Domestic Publications


## Patents
-->
