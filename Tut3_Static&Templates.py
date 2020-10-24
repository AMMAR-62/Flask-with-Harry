"""
In this video, I have explained the reason for using static and templates folder in Flask.
Flask uses its template folder for storing the raw templates which can be filled through the python program. 
The static folder on the other hand contains the public content like the images, css, javascript and other files. 
These files can also be viewed using the www.website-url/static address.
You can view the static folder of codewithharry website by going to static folder of this website as an exercise.
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return render_template("index.html")

@app.route('/about')
def Ammar():
    name = "Ammar"
    return render_template("about.html",name2=name)
app.run(debug=True)