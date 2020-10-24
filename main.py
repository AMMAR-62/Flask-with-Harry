from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/about")
def About():
    return render_template("about.html")

@app.route("/Contacts")
def Contacts():
    return render_template("contact.html")

@app.route("/Post")
def Posts():
    return render_template("post.html")
    
app.run(debug=True)