from flask import Flask

app = Flask(__name__)

@app_route('/')
def index:
  return "Hello, world. I am a Heroku Flask application"
