from flask import Flask, request, redirect, render_template
import cgi
import string

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/welcome_page', methods=['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome_page.html', username=username)
#this might break shit - review boolean values
def field_filled(field_value):
    return field_value !=''

def validate_entries():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    password2_error = ''
    email_error = ''

#check for username errors

    if not field_filled(username):
        username_error = 'Please fill in a username'
        username = ''
    else:
        if len(username)< 3 or len(username)>20:
            username_error = 'Username must be between 3-20 characters'
            
        elif " " in username:
            username_error = "Sorry, you cannot have spaces in your username. All other characters are fine!"
            

    if not field_filled(password):
        password_error = "Please create a password"
        password = ''

    if not field_filled(password2):
        password_error = "Please verify your password"
        password2 = ''

    if password != password2:
        password_error = "Password and password verification do not match"
        password = ''
        password2 = ''

    if (email.count('@') != 1)or (email.count('.') != 1):
        email_error = "Please enter a valid email"
    elif " " in email:
        email_error = "Please enter a valid email"

    #check if there is anything in the error strings

    if not username_error and not password_error and not password2_error and not email_error:
        return redirect('welcome_page?username={0}'.format(username))
    else:
        return render_template('index.html',username_error=username_error, password_error=password_error,password2_error=password2_error,email_error=email_error)
        

app.run()