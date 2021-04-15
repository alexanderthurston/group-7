
# Big Blue Parking Genie

This app is a marketplace for parking space/lot owners to rent parking spaces for local events. 

## Workspace layout

The Big Blue Parking Genie web app will be stored in this repository. 

The documentation and resources for this project will be kept in the "docs" folder. This includes use case diagrams, the project plan, database diagrams, and more as the project progresses. 

The project will kept in the folder "app". 

## Version-control procedures
Collaborators should have a forked repository of the app in Alex’s account of the project "group-7", in their Github. Each collaborator should clone the forked repository. Before each meeting, collaborators should submit a pull request so we can monitor progress and discuss issues. 

## Tool stack description and setup procedure
Django – convenient framework for this app since it comes with a simple SQLLite database. Since this app will use the database features while staying relatively small, Django was the obvious choice.  
Python – Django uses Python, and we are all very familiar with it.   
Bootstrap - Useful for UI styling purposes and a consistent UI experience.  

## Build instructions
Clone the project in gitbash.
```bash
$ git clone https://github.com/alexanderthurston/group-7
```

Create and start a virtual environment
```bash
$ cd group-7/source
```

Migrate in bash
```bash
$ python manage.py migrate
```



Create an admin account and follow steps
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

Visit local host address in a browser to see the app running. The address should be displayed in terminal after running the server.


## Unit testing instructions
Unit tests will cover all use cases laid out in the use case diagrams. They can be found in the ```tests.py```file. Run the tests.py file to see the unit tests completed.


## System testing instructions

Start by running an instance of the web app by first entering the correct repository and then by entering the following
```bash
$ python manage.py runserver
```
Now that the app is running, open an internet browser and enter the address ``` localhost:8000 ```.
Create a user in the parkingapp/sign-up page. Create an event, reserve a lot, and view your profile. There are more pages but this is the basic usage.

Visit the parkingapp/admin site to view the data.

## Other development notes, as needed
High Fidelity Prototype - Database Diagram
Low Fidelity Prototype - UX Diagram

See grading instructions in /docs
