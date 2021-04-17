# server.py

from flask import Flask
app = Flask(__name__)


#@app.route('/')
#def hello_world():
#    return "Hello World!\n"
@app.route('/')
def fake_response():
    with open('data/1078711.txt', 'r') as f:
        return f.read()


@app.route('/flask')
def fake_flask_response():
    with open('data/1078711.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    app.run()
