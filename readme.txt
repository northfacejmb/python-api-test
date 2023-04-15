




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
