<blockquote>
({{ ctx.id }}) {{ ctx.related('languageReference').name }}{% if ctx.references %}
 ( [{{ ctx.references[0].source.id }}](#user-content-source-{{ ctx.references[0].source.id }}){% if ctx.references[0].description %}
: {{ ctx.references[0].description }}{% endif %}){% endif %}


| {% for word in ctx.cldf.analyzedWord %}{% if loop.first != True %} | {% endif%}{{ word.replace("<", "\<") }}{% endfor %} |
| {% for word in ctx.cldf.analyzedWord %}{% if not loop.first %}|{% endif%} --- {% endfor %} |
| {% for word in ctx.cldf.gloss %}{% if not loop.first %} | {% endif%}{{ word.replace("<", "\<") }}{% endfor %} |


‘{{ ctx.cldf.translatedText }}’
</blockquote>
