from jinja2 import Template
name="Divya"
place="Delhi"
 #step1:

temp= """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        </head>
        <body>
            <h2>My name is {{name}}</h2>
            <h2>I live in {{place}}</h2>
        </body>
        </html>
"""
#step 2:
made_temp = Template(temp)
#step3:
out = made_temp.render(name=name,place=place)
print(out)