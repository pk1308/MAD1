from jinja2 import Template
import matplotlib.pyplot as plt
import sys
import csv
import os


class Lab_assignment:
    def __init__(self, data_path="data.csv") -> None:
        self.file_name = data_path

    def render_save_file(self, data: dict, template: Template):
        rendered_html = template.render(data=data)

        # Open a file for writing with UTF-8 encoding
        with open("output.html", "w", encoding="utf-8") as my_html_document_file:
            # Write the rendered HTML content to the file
            my_html_document_file.write(rendered_html)

    def plot_save(self, data: dict):
        plt.hist(data)
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.title("Histogram of Marks")
        file_path = os.path.join(os.getcwd(), "plot.png")
        plt.savefig(file_path)
        plt.close()
        return file_path

    def get_data(self, student_id=None, course_id=None):
        student_data = []
        course_data = {}
        file_path = os.path.join(os.getcwd(), self.file_name)
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            header = [j.strip() for j in next(reader)]
            if student_id is not None:
                for row in reader:
                    if int(row[0]) == int(student_id):
                        student_data.append(dict(zip(header, [int(i) for i in row])))
                return student_data
            elif student_id is None:
                data = []
                for row in reader:
                    if int(row[1]) == int(course_id):
                        data.append(int(row[2]))
                course_data["average_marks"] = sum(data) / len(data)
                course_data["max"] = max(data)
                return course_data, data
            else:
                pass

    def get_template( self,):
        TEMPLATE = """<!doctype html>
            <html>
            <head>
                <meta charset="UTF-8" />
                <title>{{ data['title'] }}</title>
                <meta name="description" content="Lab assignment " />
            </head>
            <body>
                <h1>{{ data['heading'] }}</h1>

                {% if data['student_data'] %}
                <table border="1" style="padding: 1px">
                <thead>
                    <tr>
                    <th>Student id</th>
                    <th>Course id</th>
                    <th>Marks</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in data['student_data'] %}
                    <tr>
                    <td>{{ row["Student id"] }}</td>
                    <td>{{ row["Course id"] }}</td>
                    <td>{{ row["Marks"] }}</td>
                    </tr>
                    {% endfor %}
                    <tr>
                    <td align="center" colspan="2">Total</td>
                    <td>{{ data["total_marks"] }}</td>
                    </tr>
                </tbody>
                </table>
                {% endif %} {% if data["course_data"] %}
                <table border="1" style="padding: 1px">
                <thead>
                    <tr>
                    <th>Average Marks</th>
                    <th>Maximum Marks</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>{{data["course_data"]["average_marks"] }}</td>
                    <td>{{ data["course_data"]["max"] }}</td>
                    </tr>
                </tbody>
                </table>
                <img src="{{ data['plot_path'] }}" alt="Plot" />
                {% endif %}
                
                {% if data["wrong_data"] %}
                <p> {{ data["wrong_data"]}}</p>                
                {% endif %}
            </body>
            </html>
            """
        template = Template(TEMPLATE)
        return template

    def run_script( self, ):
        data_to_render = {}
        template = self.get_template()
        c_index = sys.argv.index("-c") if "-c" in sys.argv else -1
        s_index = sys.argv.index("-s") if "-s" in sys.argv else -1
        # check order
        if s_index == 1 and c_index == -1:
            student_id = sys.argv[s_index + 1]
            data_to_render["title"] = "Student Data"
            data_to_render["heading"] = "Student Details"
            data_to_render["student_data"] = self.get_data(student_id=student_id)
            data_to_render["total_marks"] = sum(
                [d.get("Marks") for d in data_to_render["student_data"]]
            )
            print(data_to_render)
            self.render_save_file(data=data_to_render, template=template)
        elif c_index == 1 and s_index == -1:
            course_id = sys.argv[c_index + 1]
            data_to_render["title"] = "Course Data"
            data_to_render["heading"] = "Course Details"
            data_to_render["course_data"], data_to_plot = self.get_data(
                course_id=course_id
            )

            data_to_render["plot_path"] = self.plot_save(data=data_to_plot)
            self.render_save_file(data=data_to_render, template=template)
        else:

            data_to_render["title"] = "Something Went Wrong"
            data_to_render["heading"] = "Wrong Input"
            data_to_render["wrong_data"] = "Something Went Wrong"
            self.render_save_file(data=data_to_render, template=template)


if __name__ == "__main__":
    lab = Lab_assignment()
    lab.run_script()
