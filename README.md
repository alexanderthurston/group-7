
# Big Blue Parking Genie

This app creates a marketplace for parking space/lot owners to list parking spaces for local events. 

## Workspace layout

The Big Blue Parking Genie web app will be stored in this repository. 

The documentation and resources for this project will be kept in the "docs" folder. This includes use case diagrams, the project plan, database diagrams, and more as the project progresses. 

The project will kept in the folder "app". 

## Version-control procedures
Collaborators should have a forked repository of the app in Alex’s account of the project "group-7", in their Github. Each collaborator should clone the forked repository. Before each meeting, collaborators should submit a pull request so we can monitor progress and discuss issues. 

## Tool stack description and setup procedure
  Django – convenient framework for this app since it comes with a simple SQLLite database. Since this app will use the database              features while staying relatively small, Django was the obvious choice.
  Python – Django uses Python, and we are all very familiar with it. 

## Build instructions
Clone the project in gitbash.
```bash
$ git clone https://github.com/alexanderthurston/group-7
```

Create and start a virtual environment
```bash
$ virtualenv --no-site-packages
```

Install the project dependencies
```bash
$ pip install -r requirements.txt
```

Create a file named "secret.sh"
```bash
touch secrets.sh
```

Obtain a secret from MiniWebTool key and add to secret.sh
```bash
export SECRET_KEY='<secret_key>'
```

Add secret.sh to .gitignore file
Create a postgres db and add the credentials to settings.py

```python
DATABASES = {
    'default':  {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '', 
        }
    }
```

Migrate in bash
```bash
$ python manage.py migrate
```

Create an admin account
```bash
$ python manage.py createsuperuser
```

Then complete migrations
```bash
$ python manage.py makemigrations group-7
```

Then migrate again
```bash
$ python manage.py migrate
```

and finally
```bash
$ python manage.py runserver
```

Type localhost:8000 in a browser to see the app running.


## Unit testing instructions
Unit tests will cover all use cases laid out in the use case diagrams. They can be found in the ```unittests.py```file. The unit test class will prompt the user to select which use cases should be executed. The following use cases will be offered.  
```bash
Select which tests to perform. (ex. -> 1 3 8)
1. Customer order
2. Attendant validates customer at parking lot
3. Owner lists parking lot
4. Supervisor lists event
5. User creates account
6. User updates account
7. Supervisor requests income data
8. Customer adds money to current balance
9. Customer cancels order
```
At the end of the test run, the results will be given. 
```bash
1. Customer order was completed successfully
3. Owner lists parking lot has failed
8. Customer adds money to current balance was completed successfully
```
## System testing instructions

Start by running an instance of the web app by first entering the correct repository and then by entering the following
```bash
$ python manage.py runserver
```
Now that the app is running, open an internet browser and enter the address ``` localhost:8000 ```.
Login to the web app using the following credentials. Username: SystemTest, Password: systest

These credentials allow access to perform all actions as a customer, supervisor, owner, and attendant in a test environment. 

## Other development notes, as needed
