# Productions

{% for production in productions -%}
<a name="{{ production.path }}"></a>
## {{ production.nom }}

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
    <th>nom</th>
    <th>type</th>
    <th>description</th>
  </tr>
</thead>
<tbody>
{% for id, c in production.colonnes.items() -%}
  <tr>
    <th>`{{ id }}`</th>
    <td>{{ c.nom }}</td>
    <td>`{{ c.type }}`</td>
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
