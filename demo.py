from flask import Flask, render_template, request,url_for,session,redirect,g
import model
app=Flask(__name__)
app.secret_key="Mohammad"
username=''
user=model.cs()

@app.route('/',methods=['GET'])
def home():
    if 'username' in session:
        g.user=session['username']
        p = model.profile(session['username'])
        return render_template('dash.html' ,p=p,username = session['username'])
    return render_template('homepage.html',message="Log in to page or sign up")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        session.pop('username',None)
        ayr=request.form['username']
        pwd=model.cp(ayr)
        if request.form['password']==pwd:
            session['username']=request.form['username']
            return redirect(url_for('home'))
    return render_template('index.html')

"""if request.method == 'GET':
            return render_template('index.html')
        else:
            username = request.form['user']
            password = request.form['passw']
            db = model.cp(username)
            if password==db:
                message=model.show_color(username)
                return render_template('structure.html',message=message)
            else:
                return render_template('index.html',message='Unable to Login Successfull')"""

@app.before_request
def before_request():
    g.username=None
    if 'username' in session:
        g.username = session['username']

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/dash')
def desh():
    if request.method == 'GET':
        return render_template('dash.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))

@app.route('/index/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about/',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/signup/',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        message="Please signup!"
        return render_template('signup.html',message=message)
    else:
        fullname= request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password=request.form['password']
        mobile =request.form['mobile']
        adderss=request.form['adde']
        skill=request.form['skill']
        message=model.signup(fullname,email,username,password,mobile,adderss,skill)
        return render_template('signup.html',message=message)
if __name__=='__main__':
    app.run(debug=True)
