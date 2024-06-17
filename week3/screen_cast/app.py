# Import Jinja2 templating library
from jinja2 import Template

# Sample data for Jnanpith awardees
janapith_data = [
    {"year": 1965, "awardees": "G. Sankara Kurup", "language": "Malayalam"},
    {"year": 1966, "awardees": "Tarashankar Bandopadhyaya", "language": "Bengali"},
    {"year": 1967, "awardees": "Kuppali Venkatappagowda Puttappa", "language": "Kannada"},
]

# Define Jinja2 template string
TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Jnanpith Awardees</title>
    <meta name="description" content="This page lists Jnanpith Awardees">
</head>
<body>
    <h1>Jnanpith Awardees</h1>

    {% if janapith_data %}
    <table>
        <thead>
            <tr>
                <th>Year</th>
                <th>Awardees</th>
                <th>Language</th>
            </tr>
        </thead>
        <tbody>
            {% for janapith in janapith_data %}
            <tr>
                <td>{{ janapith["year"] }}</td>
                <td>{{ janapith["awardees"] }}</td>
                <td>{{ janapith["language"] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    {% endif %}

</body>
</html>
"""

def main( TEMPLATE  : str, janapith_data : dict):
        # Create a Jinja2 template object from the string
    template = Template(TEMPLATE)

    if janapith_data is not None:
    # Render the template with data
        rendered_html = template.render(janapith_data=janapith_data)
    else:
        rendered_html = template.render()

    # Open a file for writing with UTF-8 encoding
    with open('janapith.html', 'w', encoding='utf-8') as my_html_document_file:
        # Write the rendered HTML content to the file
        my_html_document_file.write(rendered_html)

    # (Optional) Print the rendered HTML content for debugging 
    # print(rendered_html)


if __name__ == "__main__":
    main(TEMPLATE , None )