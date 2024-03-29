# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!!!!'


if __name__ == "__main__":
    app.run(debug=True, port=8000, host='0.0.0.0')