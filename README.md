# 					Django Channel Example


#					Install the Python, Virtual Envirment and 	   									Django

step : 1	sudo apt update<br>
step : 2	python3 -V

#	Next, let's install pip from the  repositories:
step : 3	sudo apt install python3-pip


#	Once pip is installed, you can use it to install the venv package:

step : 4	sudo apt install python3-venv<br>


#	Next, create a virtual environment:
step : 5	python3.6 -m venv my_env

#	To install packages into the isolated environment, you must activate it by typing:

step : 6	source my_env/bin/activate



#				Project Configurations

#	Install django
step : 7	pip install django==2.2.4

#	Install crispy forms
step : 8	pip install django-crispy-forms==1.7.2

#	Install Channels
step : 9	pip install -U channels==2.2.0

#	Install Channels Redis
step : 10	pip install channels_redis==2.4.0


# Migrate the project

(env) >>> python manage.py makemigrations<br>
(env) >>> python manage.py migrate

#	Runserver
(env) >>> python3 manage.py runserver<br>
if perfect work than create superuser<br>
(env) >>> python3 manage.py createsuperuser<br>
in browser type : 127.0.0.1:8000<br>
open another tab 127.0.0.1:8000/admin <br>
login <br>
click on user and create a user<br>
go to 127.0.0.1:8000<br>