# Simple Calculator

This calculator, provides 3 rest apis that calculate fibonacci series, factorial and ackermann function.
More details about these functions can be found in links below:

[Wikipedia: Fibonacci Number](https://en.wikipedia.org/wiki/Fibonacci_number)  
[Wikipedia: Factorial](https://en.wikipedia.org/wiki/Factorial)  
[Wikipedia: Ackermann Function](https://en.wikipedia.org/wiki/Ackermann_function)  

## How to install and run the application
>Install Docker
First you need docker installed on your system. 
*Tutorial: [install Docker](https://docs.docker.com/engine/install/)*

> type make help to show available options and commands.

* `make dependencies`
install project dependencies
* `make test`
run project tests
* `make coverage`
 run coverage and shows coverage report as a result
* `make docker`
builds a docker image from the project
* `make dev-deploy`
deploys the docker image builded

For running the app you only need to perform these commands:
1. `make dependencies`
2. `make docker`
3. `make deploy`

Then you can check [http://localhost:8080/](http://localhost:8080/)


## Run tests and coverage

#### For running tests do these steps:
1. `make dependencies` (do this if you have not done this already)
2. `make test`


#### For getting coverage do these steps:
1. `make dependencies` (do this if you have not done this already)
2. `make coverage`


## Monitoring of project

After you ran deployed project you can access monitoring dashboard with link below:  
[http://localhost:8080/dashboard](http://localhost:8080/dashboard)

I have used flask_monitoringdashboard for this project which is easy to use.
Here is the documentation for this monitoring tool (for further information). </br>

[flask_monitoringdashboard](https://flask-monitoringdashboard.readthedocs.io/en/latest/)


## Further notices

1. Default port on starting project is `8080` so make sure port is available.
2. `flask_monitoringdashboard` creates a database for monitoring. Make sure that the device you are running project, has enough space on it.
3. I have assumed that we have no domain so therefore the domains of links on document are `localhost`.
