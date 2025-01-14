# Productions

{% for section, productions in sections %}
- [{{ section }}](#{{ section|slugify }})
{%- for prod in productions %}
  - [{{ prod.nom }}](#{{ prod.path }})
{%- endfor %}
{%- endfor %}


{% for section, productions in sections %}
<a name="{{ section|slugify }}"></a>
## {{ section }}

{% for production in productions -%}
<a name="{{ production.path }}"></a>
### {{ production.nom }}

| Propriété | Valeur |
| --------- | ------ |
{% for prop, val in production.proprietes().items() -%}
| {{ prop }} | {{ val }} |
{% endfor %}
{{ production.description }}

{% if production.colonnes -%}
### Colonnes

<table>
<thead>
  <tr>
    <th>id</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
{% for id, c in production.colonnes.items() -%}
  <tr>
    <td><code>{{ id }}</code></td>
    <td><code>{{ c.type }}</code></td>
    <td>{{ c.description }}</td>
  </tr>
{% endfor %}
</tbody>
</table>
{%- endif %}

### Sources

Cette production dépend des sources suivantes :

{% for source in production.sources() -%}
- [{{ source.nom }}](sources.md#{{ source.path }})
{% endfor -%}
{% endfor %}
{% endfor %}