#pip install jinja2

from jinja2 import Template

name="Shivani"
place="Delhi"
profession="Course instructor"

#step 1: Text

temp= " My name is {{name}}, I live in {{place}}, I am a {{profession}}"

print(temp)

#step 2:Template

# made_temp = Template(temp)

#step 3: render with data

# output= made_temp.render(name= name,place=place,profession= profession)

# print(output)



