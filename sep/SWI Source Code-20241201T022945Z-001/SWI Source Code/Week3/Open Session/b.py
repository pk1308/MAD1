#pip install jinja2
from jinja2 import Template
name="Divya"
place="Delhi"
# profession="Data Analyst"

#step 1: text
#step2: Template
#step 3: render it info
#step 1
# temp = "My name is {{Name}}, I live in {{Place}}"
temp = "My name is {{Name}}, I live in {{Place}}"

#step 2
made_temp = Template(temp)

#step3

out = made_temp.render(Name= name ,Place= place)  #x=3
print(out)

