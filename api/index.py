from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Giovani!'

@app.route('/about')
def about():
    return 'Yeas, it''s me'