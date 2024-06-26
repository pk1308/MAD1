from jinja2 import Template

data=["Programmer","Analyst","Scientist"]
#step1
temp = "My data is: {%for i in Data %} {{i}} {% endfor %}"
                     
#step2:
made_temp = Template(temp)

# print(made_temp)

#step3
out = made_temp.render(Data=data)#x=3
print(out)