#Custom docker image that has nodejs v14, python 3.9, docker, curl, awscli and awssamcli installed.
FROM python:3.9-buster
#The number of instructions and layers should be kept to a minimum as it ultimately affects the build performance and time.
#Tried to keep it at a minimum, but it surely can be optimised to be much better.
RUN cd ~  &&\  
    apt-get update &&\ 
    apt-get install curl &&\ 
    curl -sL https://deb.nodesource.com/setup_14.x -o setup_14.sh &&\ 
    bash ./setup_14.sh &&\
    curl -fsSL https://get.docker.com -o get-docker.sh &&\
    bash ./get-docker.sh
RUN apt install nodejs  &&\ 
    pip3 install awscli --upgrade 
RUN pip3 install aws-sam-cli --upgrade


      
    
