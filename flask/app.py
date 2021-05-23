from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Hello, World!"

@app.route("/user/<user_name>/<int:user_id>")
def user(user_name, user_id):
    return "Hello, %s, %s" % (user_name, user_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
