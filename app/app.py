import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "🚀 Hello from Flask inside Docker on Azure VM!"

@app.route("/secret")
def show_secret():
    secret = os.getenv("SECRET_TOKEN", "Secret not set")
    return f"Secret Token: {secret}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# trigger rebuild
