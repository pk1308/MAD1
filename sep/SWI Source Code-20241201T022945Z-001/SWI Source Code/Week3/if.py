from jinja2 import Template
subject="MAD 2"
#step 1
temp="""
{% if "1" in sub%}
  My course is {{sub}}
{% else %}
  My course is different
{% endif %}  
"""
#step 2
made_temp= Template(temp)

#step 3
output=made_temp.render(sub=subject)
print(output)