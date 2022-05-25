from flask import Flask, render_template
app = Flask(__name__)
@app.route("/sa2")
def sWebpage():
    name = 'sayan'
    return render_template('/templates/index.html',student_name = name)
app.run(debug = True)