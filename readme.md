# Gara website

## Description
It is a website that helps advertise Gums and reisins association(Gara). it is a group of well organized gum and reisin businesses .
## API Endpoints V1

| **LINKS** | **DESCRIPTION** |
| --- | --- |
| `localhost:8000/admin` | Admin panel |
| `localhost:8000/` | Home page |


### Installation, Running  the gara website
###### fork the repository and clone it to your computer
```
cd into backend
```

###### create virtual enviroment
```
virtualenv venv
```
*Note : virtual enviroment can be created at any directory.
it is advisable to create it outside the git repository , create it just outside the project.
###### Activate the virtual enviroment
```
For windows
venv/Script/activate

for unix related systems
venv/bin/activate
```
###### Install the dependencies in the requirements.txt
*Note : After activating the virtual enviroment navigate to the requirements.txt file directory and run the below command 
```
pip install -r requirements.txt
```
*Note :  The -r flag is important it allows repetitive installation of all the project dependencies

###### The database is mysql so make sure you install.

```
create a database gara and the rest of the setting related to the database can be configured
in the django settings
```
*Note : it is advisable to first open the django project setting to set the required database credentials before running the below commands e.g user, password
###### Run migration to create relevant tables in the gara database

```
python manage.py makemigrations

python manage.py migrate
```
###### creating a superuser to access the admin panel

```
python manage.py createsuperuser
```
*Note : make sure you type the necesary details prompted by the command prompt e.g email,password and  username

###### Running the website 

```
python manage.py runserver
```

###### helpful links

```
localhost:8000   : this is the homepage
```

###### Author

```
Developers at Acacia Epza
```