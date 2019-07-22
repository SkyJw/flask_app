from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db  = SQLAlchemy(app)

@app.route('/')
def index():
   return render_template('__base__.html')

   
@app.route('/tags/coding')
def test():
    return 'Hello world!'

if __name__ == '__main__':
   app.run(debug = True)