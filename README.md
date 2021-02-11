

## An explanation of the organization and name scheme for the workspace

## Version-control procedures
Collaborators should have a forked repository of the app in Alex’s account, in their Github. Each collaborator should clone the forked repository. Before each meeting, collaborators should submit a pull request so we can monitor progress and discuss issues. 

## Tool stack description and setup procedure
Django – convenient framework for this app since it comes with a simple SQLLite database. Since this app will use the database features while staying relatively small, Django was the obvious choice.
Python – Django uses Python, and we are all very familiar with it. 

## Build instructions
What they need to do to get it to work on their computer

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

## Other development notes, as needed
