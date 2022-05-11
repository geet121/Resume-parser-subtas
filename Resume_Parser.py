from flask import Flask
import os
from flask import (Flask,session,flash, redirect, render_template, request, url_for, send_from_directory)

app = Flask(__name__,template_folder="templates")
app.config.from_object(__name__) 

# @app.route("/")
# def index():
#     return render_template('Sign_in.html')

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        if request.form['username'] != 'admin@gmail.com' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('Sign_in.html', error=error)


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/candidate")
def main():
    return render_template('candidate_resume.html')
    

@app.route("/jobs")
def job():
    return render_template('jobs.html')


@app.route("/checker")
def ch():
    return render_template('resume_checker.html')

@app.route("/res")
def res1():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/resume_files'
    return send_from_directory(filepath, 'Akhil.profile.pdf')

@app.route("/res2")
def res2():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/resume_files'
    return send_from_directory(filepath, 'AnilAgarwal.pdf')

@app.route("/res3")
def res3():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/resume_files'
    return send_from_directory(filepath, 'Dhruvi.pdf')

@app.route("/res4")
def res4():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/resume_files'
    return send_from_directory(filepath, 'Jennifer  M. Conte.pdf')

@app.route("/res5")
def res5():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/resume_files'
    return send_from_directory(filepath, 'Akhil.profile.pdf')

@app.route("/res6")
def res6():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/resume_files'
    return send_from_directory(filepath, 'Rajesh_k.pdf')

@app.route("/JD")
def JD():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/JD_files'
    return send_from_directory(filepath, 'Yabble Machine Learning Engineer Job Description.pdf')



# @app.route('/<id>')
# def show_pdf(id=None):
#     if id is not None:
#         return render_template('doc.html', doc_id=id)


if __name__ == '__main__':
   app.run(debug=True ,use_reloader=False)