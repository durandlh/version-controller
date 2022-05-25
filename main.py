import flask 
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Nothing is here "

@app.route("/mpr-cracker")
def mpr_cracker():
    info = {
        'version': '1', 
        'setup': 'https://github.com'
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)