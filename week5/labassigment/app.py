from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]  = "sqlite:///database.sqlite3"

db = SQLAlchemy(app=app)


COURSES = {"course_1":"MAD I","course_2":"DBMS","course_3":"PDSA","course_4":"BDM"}

class student(db.Model):
    student_id = db.Column(db.Integer , autoincrement=True, primary_key = True )
    roll_number = db.Column(db.String, unique = True , nullable = False)
    first_name = db.Column(db.String,  nullable = False)
    last_name = db.Column(db.String)
    
class course(db.Model):
    course_id = db.Column(db.Integer , autoincrement=True, primary_key = True )
    course_code = db.Column(db.String(), unique = True , nullable = False)
    course_name = db.Column(db.String(),  nullable = False)
    course_description = db.Column(db.String())
    
class enrollments(db.Model):
    enrollment_id= db.Column(db.Integer , autoincrement=True, primary_key = True )
    estudent_id = db.Column(db.Integer ,db.ForeignKey(student.student_id), 
                            primary_key=True, nullable=False )
    ecourse_id = db.Column(db.Integer ,db.ForeignKey(course.course_id), 
                            primary_key=True, nullable=False )
    
    
    
 
@app.route("/", methods=["GET", "POST"])
def home():
    students= student.query.all()
    return render_template("index.html", students=students)

 
@app.route("/student/create", methods=["GET", "POST"])
def create_student():
    if request.method == "POST":
        form_roll_number = request.form.get("roll")
        form_first_name = request.form.get("f_name")
        form_last_name = request.form.get("l_name")
        form_courses = [COURSES.get(course_value) for course_value in request.form.getlist("courses")]
        
        if student.query.filter_by(roll_number=form_roll_number).first():
          return render_template("create_exist.html")
        else:
            data_to_insert = student(roll_number = form_roll_number , first_name = form_first_name,
                                     last_name = form_last_name)

            db.session.add(data_to_insert)
            db.session.commit() 
            sid = data_to_insert.student_id
            for course_name in form_courses:
                course_ = course.query.filter_by(course_name=course_name).first()
                if course_:
                    en = enrollments(estudent_id=sid, ecourse_id=course_.course_id)
                    db.session.add(en)
            db.session.commit()
            return redirect("/") 
    else:
        return render_template("create.html")
    
@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def student_data_update(student_id):
    if request.method == "POST":
        f_name = request.form["f_name"]
        l_name = request.form["l_name"]
        courses = [COURSES.get(course_value) for course_value in request.form.getlist("courses")]
        stu = student.query.filter_by(student_id=student_id).first()
        stu.first_name = f_name
        stu.last_name = l_name
        db.session.add(stu)
        enrollments_master = enrollments.query.filter_by(estudent_id=student_id).all()
        for enrollment in enrollments_master:
            db.session.delete(enrollment)

        # Add new enrollments
        for course_name in courses:
            if course_name:  # Ensure course_name is not None
                course_ = course.query.filter_by(course_name=course_name).first()
                if course_:
                    new_enrollment = enrollments(estudent_id=student_id, ecourse_id=course_.course_id)
                    db.session.add(new_enrollment)

        db.session.commit()
        return redirect("/")
    stu = student.query.filter_by(student_id=student_id).first()
    return render_template("update.html",student=stu)


@app.route("/student/<int:student_id>/delete", methods=["GET","POST"])
def destroyer(student_id):
    stu = student.query.filter_by(student_id=student_id).first()
    db.session.delete(stu)
    db.session.commit()
    return redirect("/")
        
@app.route("/student/<int:student_id>", methods=["GET"])
def viewer(student_id):
    stu = student.query.filter_by(student_id=student_id).first()
    en = enrollments.query.filter_by(estudent_id=student_id)
    enroll = []
    for i in en:
        cour = course.query.filter_by(course_id=i.ecourse_id).first()
        enroll.append({"code":cour.course_code,"name":cour.course_name,"desc":cour.course_description})
    return render_template("view.html",student=stu,enroll=enroll)


if __name__=="__main__":
    app.run()
        
    
            
        
        

        