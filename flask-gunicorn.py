from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h4 style='color:yellow'>Welcome To Page</h4>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000)
