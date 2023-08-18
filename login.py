from flask import Flask, render_template, request, redirect, session

app = Flask(_name_)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    # Get the email and password entered by the user
    email = request.form['email']
    password = request.form['password']

    # Check if the email and password are correct (e.g. by querying a database)
    if email == 'user@example.com' and password == 'password':
        # If the user is authenticated, store their email in a session variable
        session['email'] = email
        return redirect('/home')
    else:
        # If the email and/or password are incorrect, show an error message
        return render_template('home.html', error='Invalid email or password')

@app.route('/home')
def dashboard():
    # Check if the user is logged in (i.e. if their email is stored in the session variable)
    if 'email' in session:
        # If the user is logged in, show the dashboard page
        return render_template('home.html', email=session['email'])
    else:
        # If the user is not logged in, redirect them to the login page
        return redirect('/home')