from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Matan Hamami did it again!"

if __name__ == "__main__":
    app.run()

