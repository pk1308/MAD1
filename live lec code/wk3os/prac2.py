from string import Template
# from jinja2 import Template
#step1 and 2
temp = Template("Today is $today and tomorrow is $tomorrow.")
#step 3
# out = temp.substitute(today="Monday")
out = temp.safe_substitute(today="Monday")
print(out)

#jinja> {{}}, string $
# both Template()
# jinja> render(), string> substitute()
#jinja> no value of variable>blank, string it throws error
# string> no value of variable>safe_substitute  $variable

# temp = Template("Today is {{today}} and tomorrow is {{tomorrow}}.")
# #step 3
# out = temp.render(today="Monday")
# print(out)