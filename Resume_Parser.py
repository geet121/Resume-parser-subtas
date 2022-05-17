import os
from flask import (Flask,session,flash, redirect, render_template, request, url_for, send_from_directory)
import csv


app = Flask(__name__,template_folder="templates")
app.config.from_object(__name__) 

app.config['UPLOAD_FOLDER'] = 'Upload-Resume'
app.config['UPLOAD_JD_FOLDER'] = 'Upload-JD'


def getfilepath(loc):
    temp = str(loc).split('\\')
    return temp[-1]


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
    

@app.route("/jobs", methods=['GET', 'POST'])
def job():
    error = None
    x = os.listdir(app.config['UPLOAD_JD_FOLDER'])
    return render_template('jobs.html',name=x)


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
    x = os.listdir(app.config['UPLOAD_FOLDER'])
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/JD_files'
    return render_template('jobs.html', name = x)
    #return send_from_directory(name = x)

@app.route('/Upload-Resume/<path:filename>')
def custom_static(filename):
    print(filename)
    return send_from_directory('./Upload-JD', filename)

# Upload files
@app.route("/upload", methods=['POST'])
def upload_file():
    Error = None
    if request.method=='POST':
        #upload Job Description
        if 'Jdfiles'in request.files:
            filelist = [ f for f in os.listdir(app.config['UPLOAD_JD_FOLDER']) ]  
            x = os.listdir(app.config['UPLOAD_JD_FOLDER'])
            for f in request.files.getlist('Jdfiles'):
                if f.filename in x:
                    Error = "All Ready "+f.filename +" Existed"
                else:
                    f.save(os.path.join(app.config['UPLOAD_JD_FOLDER'], f.filename))   
            x = os.listdir(app.config['UPLOAD_JD_FOLDER'])
            return render_template('jobs.html', name = x)
    
        #upload Resume
        if 'Resumefiles' in request.files:
            filelist = [ f for f in os.listdir(app.config['UPLOAD_FOLDER']) ]  
            x = os.listdir(app.config['UPLOAD_FOLDER'])
            for f in request.files.getlist('Resumefiles'):
                if f.filename in x:
                    Error = "All Ready "+f.filename +" Existed"
                else:
                    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))   
            x = os.listdir(app.config['UPLOAD_FOLDER'])
            return render_template('candidate_resume.html',name = x)
"""        
# Fetch data
def source_data():
    x = os.listdir(app.config['UPLOAD_FOLDER'])
    fields = ['Candidate', 'Name', 'Email', 'Phone no','Skills','Qualification','Experience','Company Name'] 
    
    # name of csv file 
    filename = "records.csv"
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + 'Results'
    # writing to csv file 
    with open((os.path.join(filepath, filename)), 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 

        # writing the fields 
        csvwriter.writerow(fields) 

        # writing the data rows 
        #csvwriter.writerows(rows)
    df = pandas.read_csv((os.path.join(filepath, filename), index_col=False, header=0);
    serie = df.ix[0,:]
    print(serie)                  
"""    
if __name__ == '__main__':
   app.run(debug=True ,use_reloader=False)