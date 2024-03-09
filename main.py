from flask import Flask


app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Hello'

@app.route('/video')
def main_page():
    return 'Hello'

@app.route('/mimo')
def main_page():
    return 'Hello'

@app.route('/manual')
def main_page():
    return 'Hello'

@app.route('/author')
def main_page():
    return 'Hello'




app.run(debug=True)