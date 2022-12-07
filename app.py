# Importing the necessary Libraries
# from flask_cors import cross_origin
from flask import Flask, render_template, request
from main import text_to_speech

app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')
@app.route('/', methods=['POST', 'GET'])
# @cross_origin()
def homepage():
    if request.method == 'POST':
        texT = request.form['text']
        lang = request.form['voices']
        text_to_speech(texT,lang)
        return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/pdf')
def home():
    return render_template('index2.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)