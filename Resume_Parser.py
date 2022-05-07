from flask import Flask
import os
from flask import (Flask,session,flash, redirect, render_template, request, url_for, send_from_directory)

app = Flask(__name__,template_folder="templates")
app.config.from_object(__name__) 



@app.route("/")
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
def tos():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/resumes_files'
    return send_from_directory(filepath, 'tos.pdf')

# @app.route('/<id>')
# def show_pdf(id=None):
#     if id is not None:
#         return render_template('doc.html', doc_id=id)


if __name__ == '__main__':
   app.run(debug=True ,use_reloader=False)