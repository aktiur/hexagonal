# Données sources

{% for source in sources -%}
<a name="{{ source.path }}"></a>
## {{ source.nom }}

| Propriété | Valeur |
| --------- | ------ |
{% for prop, val in source.proprietes().items() -%}
| {{ prop }} | {{ val }} |
{% endfor %}
{{ source.description }}
{% endfor %}
