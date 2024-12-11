from jinja2 import Template

#step 1 :create text

temp="""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Document</title>
</head>
<body>
    <h1>My name is {{name}}</h1>
    <h1>I live in {{place}}</h1>
    <h1>I am an {{profession}}</h1>
</body>
</html>
"""
# step2: use template fn

made_temp= Template(temp)

# step3: Render with data

output=made_temp.render(name="Shivani", place="Chennai",profession="Analyst")
print(output)
