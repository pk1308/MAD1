#pip install jinja2

from jinja2 import Template

name="Shivani"
place="Delhi"
# profession="Course instructor"

#step 1: Text

temp= " My name is {{name}}, I live in {{place}}, I am a {{profession}}"

# temp= """
#     <h1>{{name}}</h1>
#     <h1>{{place}}</h1>
#     <h1>{{profession}}</h1>
# """

#step 2:Template

made_temp = Template(temp)

#step 3: render with data

output= made_temp.render(name= "Baalajee",place=place)#x=8

print(output)



