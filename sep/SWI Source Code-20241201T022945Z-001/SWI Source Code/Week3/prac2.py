from string import Template
temp = Template("Today is $today and tomorrow is $tomorrow.")
out = temp.substitute(today="Monday",tomorrow="Tuesday")
out = temp.substitute(today="Monday")#KeyError: 'tomorrow'
print(out)

#jinja> {{}},render, doesnt throw error if value not passed
#string> $, substitute, throws error if value not assigned