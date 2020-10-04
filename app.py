from flask import Flask, render_template, url_for, flash, redirect
from form import MessageForm
from flask_mail import Mail, Message 

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')



mail = Mail(app)


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')



@app.route('/products')
def products():
	return render_template('products.html', title='Products')


@app.route('/services')
def services():
	return render_template('services.html', title='Services')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = MessageForm()
	if form.validate_on_submit():
		msg = Message(form.title.data, recipients=['demo@email.com']) # Provide email address you want to send emails to from your default email provided above
		msg.body = f'''From: {form.name.data}, {form.email.data},
		Message: {form.message.data}'''
		mail.send(msg)
		flash('Your message has been sent.', 'success')
		return redirect(url_for('home'))
	return render_template('contact.html', title='Contact Us', form=form)

if __name__ == '__main__':
	app.run()