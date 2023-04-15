




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
