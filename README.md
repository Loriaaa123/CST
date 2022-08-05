to start project first of all activate venv
```
source ./venv/bin/activate
```
then make migrations 
```
python manage.py migrate
```
and then run the server or before you can create super user
```
python manage.py createsuperuser
```
```
python manage.py runserver
```