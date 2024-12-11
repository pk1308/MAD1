from jinja2 import Template

data=["Programmer","Analyst","Scientist"]
#step 1 :create text

temp="""
<!DOCTYPE html>
<html>
<head>
    <title>Document</title>
</head>
<body>
    <h1>My name is {{name}}</h1>
    <h1>I live in {{place}}</h1>
    {% for i in data %}
    <h1>I am {{i}}</h1>
    {% endfor %}
</body>
</html>
"""
# step2: use template fn

made_temp= Template(temp)

# step3: Render with data

output=made_temp.render(name="Shivani", place="Chennai",data=data)
print(output)

# Please note unlike python there is no concept of indentation in Jinja, so when we start a condition or loop in jinja we also need to tell when it ends, hence end for is used. In python, it is directly done with the indentations.