from flask import Flask


#create instance
app = Flask(__name__)

@app.route("/") #decorator
def index():
    return "<p>Home</p>"

@app.route("/about") #decorator
def hello_world():
    return "<p>about</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5005)
