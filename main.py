from worldbankapp import app
from worldbankapp.forms import ContactForm

from flask import render_template, jsonify, flash
from flask import Flask,redirect, url_for, request
app = Flask(__name__)
app.secret_key = 'development key'
@app.route('/')
@app.route('/index/')
def index():
    d={"Details":{"Name":"Mohab","Age":26}}
    #return "<h1> hii </h1>"
    return jsonify(d)
    
@app.route('/project-one')
def project_one():
    #pass
    return render_template('project_one.html')

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

'''
@app.route("/interact")
def interact():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('interact.html',result = dict)
'''

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      u = request.form['nm']
      #print("post:",user)
      dict = {'phy': 50, 'che': 60, 'maths': 70}
      return render_template('interact.html', result=dict,user=u)
   else:
       return render_template(('login.html'))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            return render_template('success.html')

    if request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
   app.run(debug=True)