from flask import Flask, render_template
from flask import request

app = Flask(__name__)
app.debug = True

@app.route('/color_form')
def form1():
	render_template('color_form.html')

#@app.route('/colorinfo')
#def results()
