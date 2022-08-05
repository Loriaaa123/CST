```
git clone https://github.com/Loriaaa123/CST.git
```
then 
```
cd CST
```
to start project first of all activate venv in CST directory
```
source ./venv/bin/activate
```
then make migrations in cstsocial directory ( cd sctsocial)
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
