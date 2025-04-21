from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, this is a small text message! \n I hope you like it"

if __name__ == '__main__':
    app.run(debug=True)
