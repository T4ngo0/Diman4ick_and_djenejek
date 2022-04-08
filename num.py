from flask import flask


add = Flask(__name__)


@app.route('/')
def index():
  return "Привет, мир!"


app.run(port='0000')
