# Données sources

{% for editeur, sources in editeurs %}
- [{{ editeur }}](#{{ editeur|slugify }})
{%- for source in sources %}
  - [{{ source.nom }}](#{{ source.path }})
{%- endfor %}
{%- endfor %}

{% for editeur, sources in editeurs %}

<a name="{{ editeur|slugify }}"></a>
## {{ editeur }}

{% for source in sources -%}
<a name="{{ source.path }}"></a>
### {{ source.nom }}

| Propriété | Valeur |
| --------- | ------ |
{% for prop, val in source.proprietes().items() -%}
| {{ prop }} | {{ val }} |
{% endfor %}
{{ source.description }}
{% endfor %}
{% endfor %}