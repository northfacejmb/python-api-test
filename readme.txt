trying to follow along from 
https://www.youtube.com/watch?v=qbLc5a9jdXo


Import and create database using flask 

>>> from application import db
>>> from application import app
>>> app.app_context().push()
>>> db.create_all()

create a new drink: 
python3
>>> from application import drink
>> drink = Drink(name="Grape Soda", description="Tastes like grapes")
>>> db.session.commit()


Setup python virtual environment
cd root
create:
>>> python 3 -m venv venv
activate:
>>> source venv>bin>activate


add dependencies to requirements
>>> pip3 freeze > requirements.txt

add a new drink
from application import Drink
drink = Drink(name="orange soda",description="tastes orange")

commit entries to db
db.session.add(drink)



https://python-adv-web-apps.readthedocs.io/en/latest/flask_db3.html

https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application


My isue: according to chatGPT:
If you want to add a drink in the Python shell, you can do the following steps:

Import your Flask app and database models:
from your_app import app, db
from your_app.models import Drink
Create an instance of the 
Drink
 model with the desired attributes:
drink = Drink(name="My Drink", description="This is my favorite drink.")
Within a Flask application context, add the 
drink
 object to the 
db.session
 and commit the changes:
with app.app_context():
    db.session.add(drink)
    db.session.commit()
Note that you need to be inside a Flask application context to access the 
db.session
 object. Wrapping your code inside a 
with app.app_context():
 block creates a temporary application context where you can interact with the database.

Once you have added the drink to the database, you can query it using the 
Drink.query.all()
 method or any other query methods provided by SQLAlchemy.