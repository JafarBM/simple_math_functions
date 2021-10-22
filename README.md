### Simple calculator application

This calculator, provides 3 rest apis that calculate fibonacci series, factorial and ackermann function.
more details about these functions can be found in links below:

https://en.wikipedia.org/wiki/Fibonacci_number </br>
https://en.wikipedia.org/wiki/Factorial </br>
https://en.wikipedia.org/wiki/Ackermann_function </br>

### How to install and run the application

First you need docker installed on your system, in the link below you can learn how:

https://docs.docker.com/engine/install/ubuntu/


Second  with make help you can run your desired command:

make dependencies --> install project dependencies </br>
make test --> run project tests </br>
make coverage --> run coverage and shows coverage report as a result </br>
make docker --> builds a docker image from the project </br>
make dev-deploy --> deploys the docker image builded </br>

For running the app you only need to perform these commands:
1. ```make dependencies```
2. ```make docker```
3. ```make deploy```

Then you can check http://localhost:8080/


### Run tests and coverage

For running tests do these steps:
1. ```make dependencies``` (do this if you have not done this already)
2. ```make tests```


For getting coverage do these steps:
1. ```make dependencies``` (do this if you have not done this already)
2. ```make coverage```


### Monitoring of project

After you ran deployed project you can access monitoring dashboard with link below:
http://localhost:8080/dashboard

I have used flask_monitoringdashboard for this project which is easy to use.
Here is the documentation for this monitoring tool (for further information). </br>

https://flask-monitoringdashboard.readthedocs.io/en/latest/


### Further notices

1. Default port on starting project is 8080 so make sure nothing is listening on this port already.
2. flask_monitoring_dashboard creates a database for monitoring so make sure that the device you are running project, has enough space on it.
3. I have assumed that we have no domain so therefor the domains of links on document are "localhost".
