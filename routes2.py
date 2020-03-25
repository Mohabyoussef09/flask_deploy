from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    #return "<h1> hii </h1>"
    return render_template('index.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
       return render_template('login.html')
      #user = request.args.get('nm')
      #return redirect(url_for('success'))

@app.route('/success/<name>')
def success(name):
   return 'welcome {}'.format(name)

if __name__ == '__main__':
   app.run(debug = True)