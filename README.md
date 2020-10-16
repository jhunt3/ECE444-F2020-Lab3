Jeremy Hunt
this repo is a clone of
https://github.com/miguelgrinberg/flasky

How to Build and Start the system
Include the Dockerfile and requirements.txt files as in this directory
Run the build then run commands:
docker build -t flask-sample:latest .
![Image 1](https://github.com/jhunt3/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ss1.PNG)

docker run -d -p 5000:5000 flask-sample
![Image 2](https://github.com/jhunt3/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ss4.PNG)
![Image 3](https://github.com/jhunt3/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ss3.PNG)
![Image 4](https://github.com/jhunt3/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/ss2.PNG)

Docker vs VM:
VMs are essentially fully functioning computers while docker only is a functioning process and thus is much lighter weight than a vm.
