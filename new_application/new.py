from flask import Flask, render_template
from flask import request

app = Flask(__name__)
app.debug = True

@app.route('/color_form')
def form1():
	return render_template('color_form.html')

@app.route('/colorinfo',methods = ['POST', 'GET'])
def p_results():
	if request.method == 'GET':
		results = request.args
	primary = {"red", "blue", "yellow"}
	for x in primary:
		if x == results['color']:
			return render_template('primary.html', results = results)
	secondary = {"green", "orange", "purple"}
	for y in secondary:
		if y ==results['color']:
			return render_template('secondary.html', results = results)
		if y not in results['color']:
			return render_template('unique.html', results = results)



