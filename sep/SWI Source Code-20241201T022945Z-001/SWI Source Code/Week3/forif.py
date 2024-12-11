from jinja2 import Template
#step 1 :create text
data=["Programmer","Analyst","Scientist"]
temp="""
    {% for i in data %}
      {% if "t" in i %}
      {{i}}
      {% endif %}
    {% endfor %}
"""
# step2: use template fn

made_temp= Template(temp)

# step3: Render with data

output=made_temp.render(data=data)
print(output)
