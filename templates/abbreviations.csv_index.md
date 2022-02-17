Abbreviation | Definition
--- | ---
{% for obj in ctx %}
{{ obj['ID'] }} | {{ obj['Description'] }}
{% endfor %}