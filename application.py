
from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

with app.app_context():
  db.create_all()

class Drink(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name= db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(120))

  def __repr__(self):
    return f"{self.name} - {self.description}"

@app.route('/')
def index():
  return 'hello!!'

@app.route('/drinks')
def get__drinks():
  return {'drinks': 'drink-data'}