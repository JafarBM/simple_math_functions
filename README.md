### simple calculator application

this calculator, provides 3 rest apis that calculate fibonacci series, factorial and ackermann function.
more details about these functions can be found in links below:

https://en.wikipedia.org/wiki/Fibonacci_number
https://en.wikipedia.org/wiki/Factorial
https://en.wikipedia.org/wiki/Ackermann_function

### how to install and run the application

first you need docker installed on your system, in the link below you can learn how:

https://docs.docker.com/engine/install/ubuntu/


second  with make help you can run your desired command:

make dependencies --> install project dependencies
make test --> run project tests
make coverage --> run coverage and shows coverage report as a result
make docker --> builds a docker image from the project
make dev-deploy --> deploys the docker image builded

for running the app you only need to perform these commands:
1. ```make dependencies```
2. ```make docker```
3. ```make deploy```

then you can check http://localhost:8080/


### run tests and coverage

for running tests do these steps:
1. ```make dependencies``` (do this if you have not done this already)
2. ```make tests```


for getting coverage do these steps:
1. ```make dependencies``` (do this if you have not done this already)
2. ```make coverage```
