from jinja2 import Template
subject="MAD 1"

temp = """
      {% if "2" in sub %}
        {{sub}}
      {%else%}
      Required subject not found
      {% endif %}
"""
made_temp = Template(temp)

out = made_temp.render(sub= subject)
print(out)