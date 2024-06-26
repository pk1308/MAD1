import csv
import os
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, send_from_directory
plt.switch_backend("agg")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        id_type = request.form.get('ID')
        id_value = request.form.get('id_value')
        app_run = Lab_assignment3()
        data_to_tender =  app_run.run_script(id_type=id_type, id_value=id_value)
        return render_template("output.html" , data =data_to_tender )

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

class Lab_assignment3:
    def __init__(self) -> None:
        self.data = self.get_data()

    def plot_save(self, data: dict):
        plt.hist(data)
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.title("Histogram of Marks")
        file_dir_plot = os.path.join(os.getcwd(), "static")
        file_path_plot = os.path.join(file_dir_plot, "plot.png")
        os.makedirs(file_dir_plot, exist_ok=True)
        plt.savefig(file_path_plot)
        plt.close()
        return 

    def get_data(self, file_name = "data.csv"):
        try:
            master_data= {
            "student_data_list" : [] , 
            "course_data_list" : [], 
            "master_data_list" : [] }
            
            
            file_path = os.path.join(os.getcwd(), file_name)
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                header = [j.strip() for j in next(reader)]
                for row in  reader:
                    data_to_insert= []
                    data_to_insert ={key : int(value) for key , value in zip(header, row)}
                    master_data["student_data_list"].append(data_to_insert["Student id"])
                    master_data["course_data_list"].append(data_to_insert["Course id"])
                    master_data["master_data_list"].append(data_to_insert)
        except Exception as e :
            print(e)
    
        return master_data
    
    def render_error(self,):
        data_to_render= {}        
        data_to_render["title"] = "Something Went Wrong"
        data_to_render["heading"] = "Wrong Input"
        data_to_render["wrong_data"] = "Something Went Wrong"
        return data_to_render
        

    def run_script(self, id_type, id_value):

        data_to_render = {}
        if id_type == "student_id":
            student_id = id_value
            if student_id in self.data["student_data_list"]:
                
                data_to_render["title"] = "Student Data"
                data_to_render["heading"] = "Student Details"
                student_Data = ""
                data_to_render["student_data"] = student_Data
                data_to_render["total_marks"] = sum([d.get("Marks") for d in data_to_render["student_data"]])
                return data_to_render
            else:
                pass 
            
        elif id_type == "course_id":
            course_id = id_value
            if course_id in self.data["course_data_list"]:                
                data_to_render["title"] = "Course Data"
                data_to_render["heading"] = "Course Details"
                data_to_render["course_data"], data_to_plot = self.get_data(course_id=course_id)          
                self.plot_save(data=data_to_plot)
                return data_to_render
            else:
                return self.render_error()
        else:
             return self.render_error()
        return 

if __name__ == "__main__":
    app.run()
