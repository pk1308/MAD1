from jinja2 import Template
name="Shivani"
place="Chennai"
profession="Data Analyst"

#step 1: create text
# (wherever you want to manipulate data, use variable in double curly brackets i.e place holders)

temp="My name is {{name}}, I live in {{place}} and I am a {{profession}} "

#step 2: use template function to convert it to template
#converting to template because we want to manipulate text according to our data
 
made_temp = Template(temp)

#step 3: render with data
#data of choice is passed to this template, accordingly output will come

output = made_temp.render(name=name, place=place, profession=profession)
#LHS refers too the variable used in jinja template, RHS refers to data variables to be assigned

print(output)

