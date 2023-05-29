from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'development key'

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'rmccormick314@gmail.com'
app.config["MAIL_PASSWORD"] = 'nwdhuhmdzigotxdy'
mail.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)

    else:
      msg = Message(form.subject.data,
                    sender='contact@songbird.com',
                    recipients=['rmccormick314@gmail.com'])
      msg.body = """
                 From: %s <%s>
                 %s
                 """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template("confirm-contact.html")

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
