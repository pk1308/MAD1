from jinja2 import Template
#step 1 :create text
data=["Programmer","Analyst","Scientist"]

temp = """
      {% for i in data %}
         {% if "z" in i %}
            {{i}}
         {% endif %}
         
      {% endfor %}
      No data found   
      """
made_temp = Template(temp)

out = made_temp.render(data = data )#x=3
print(out)

