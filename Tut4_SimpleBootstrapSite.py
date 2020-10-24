from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Hello():
    return render_template("index.html")
@app.route("/about")
def Ammar():
    name="Shaikh Ammar"
    return render_template("about.html",name2=name)

@app.route("/bootstrap0")
def Bootstrap():
    return render_template("Bootstrap.html")
app.run(debug=True)