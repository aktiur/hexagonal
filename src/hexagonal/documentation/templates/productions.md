{% macro render_tree(d) -%}
    <ul>
    {% for (nom, lien),v in d.items() -%}
        <li><a href="{{ lien }}">{{ nom }}</a>
        {% if v -%}
        {{ render_tree(v) }}
        {% endif -%}
        </li>
    {% endfor -%}
    </ul>
{%- endmacro %}
# Productions

{% for section, productions in sections %}
- [{{ section }}](#{{ section|slugify }})
{%- for prod in productions %}
  - [{{ prod.nom }}](#{{ prod.path }})
{%- endfor %}
{%- endfor %}


{% for section, productions in sections %}
## {{ section }}
<a name="{{ section|slugify }}"></a>

{% for production in productions -%}
### {{ production.nom }}
<a name="{{ production.path }}"></a>

| Propriété | Valeur |
| --------- | ------ |
{% for prop, val in production.props.items() -%}
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

{{ render_tree(production.deps) }}

{% endfor %}
{% endfor %}
