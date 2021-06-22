from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return os.getenv('mytext')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
