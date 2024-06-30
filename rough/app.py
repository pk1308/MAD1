from flask import Flask, render_template, url_for , redirect
app = Flask (__name__)
@app.route("/if")
def ifelse():
    user = "MAD I"
    return render_template("if_example.html", name=user)

@app.route("/for")
def for_loop():
    # list_of_courses = ['Java', 'Python', 'DBMS', 'PDSA']
    return "test"
@app.route("/choice/<pick>")
def choice (pick):
    if pick == 'if':
        return url_for('ifelse')
    if pick =='for':
            return redirect(url_for('for_loop'))
    else:
        pass

if __name__ == "__main__":
    
    app.run(debug=True)