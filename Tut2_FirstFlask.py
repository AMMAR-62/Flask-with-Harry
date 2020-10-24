"""
If you google search "Minimal flask app", you will find some code written in the flask documentation. 
The code doesnt contains the app.run() line which I have written in the code section of this page. 
In my opinion, it becomes very difficult to run their first flask app for beginners without the app.run() function.
The flask documentation uses command line to create environment variables and then run them through the command line 
contary to my code which accomplishes this task inside the python program itself. 
Let me know what you think about this in the comments below!
I have created only one endpoint as of now, we will create more endpoints very soon. 
You can create more endpoints if you want now or follow the tutorial to see whats next! Hope you like the video!
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"
    return render_template("index.html")

@app.route('/about')
def Ammar():
    return "Hello, Ammar!"
    return render_template("about.html")
app.run()