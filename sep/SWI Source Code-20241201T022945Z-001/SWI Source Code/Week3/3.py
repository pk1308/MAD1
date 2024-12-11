from jinja2 import Template
sub= " MAD 1"
temp="""
      {% if "1" in subject %}
        The course is {{subject}}
      {% else %}
        The course is different
      {% endif %}      
"""
made_temp= Template(temp)
out=made_temp.render(subject=sub)#x=8
out=made_temp.render(subject="MAD 2")
print(out)