from jinja2 import Template
my_statement = Template("The special series is:{% for n in range(1,15)   %} {{n%3}}{% endfor %}")
out = my_statement.render()
print(out)

# {% for n in range(1,15)   %} #[1, 2,3.....14]
# {{n%3}}
# {% endfor %}