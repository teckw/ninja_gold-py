from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'sshh'

@app.route('/')
def index():
	if 'gold' in session:
		session['gold'] = session['gold']
	else:
		session['gold'] = 0
	if 'log' not in session:
		session['log'] = []

	session['farm'] = random.randrange(10, 21)
	session['cave'] = random.randrange(5, 11)
	session['house'] = random.randrange(2, 6)
	session['casino'] = random.randrange(-50, 51)
	return render_template('ninja_gold.html')

@app.route('/process_money', methods=['POST'])
def gold():
	if request.form ['building'] == 'farm':
		session['gold'] += session['farm']
		session['log'].insert(0, 'Gained ' + str(session['farm']) + ' from the farm.')
	
	if request.form ['building'] == 'cave':
		session['gold'] += session['cave']
		session['log'].insert(0, 'Gained ' + str(session['cave']) + ' from the cave.')
	
	if request.form ['building'] == 'house':
		session['gold'] += session['house']
		session['log'].insert(0, 'Gained ' + str(session['house']) + ' from the house.')
	
	if request.form ['building'] == 'casino':	
		session['gold'] += session['casino']
		session['log'].insert(0, 'Gained ' + str(session['casino']) + ' from the casino.')
	return redirect('/')
	
def log():
	if request.form['building'] == 'farm':
		session['log'] = str(session['gold'])
	return redirect('/', log = session['log'])

@app.route('/reset')
def reset():
	session.pop('gold')
	session['log']=[]
	return redirect('/')

app.run(debug=True)