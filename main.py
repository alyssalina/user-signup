from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

#@app.route('/welcome_page', methods=['POST'])
#def welcome():


app.run()