from jinja2 import Template

data = ["Analyst","Programmer", "Instructor"]

temp="""
      {% for i in data %}
         {% if "z" in i %}
           {{i}}
         {% endif %}
      {% endfor %}
"""
# print(temp)
made_temp= Template(temp)

out= made_temp.render(data= data)#x=8

print(out)