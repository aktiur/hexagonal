# Données sources

{% for editeur, sources in editeurs %}
- [{{ editeur }}](#{{ editeur|slugify }})
{%- for source in sources %}
  - [{{ source.nom }}](#{{ source.path }})
{%- endfor %}
{%- endfor %}

{% for editeur, sources in editeurs %}

## {{ editeur }}
<a name="{{ editeur|slugify }}"></a>

{% for source in sources -%}
### {{ source.nom }}
<a name="{{ source.path }}"></a>

| Propriété | Valeur |
| --------- | ------ |
{% for prop, val in source.props.items() -%}
| {{ prop }} | {{ val }} |
{% endfor %}
{{ source.description }}
{% endfor %}
{% endfor %}