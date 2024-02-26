FROM ubuntu:latest

# Set the working Directory 
WORKDIR /app

#Copy files from host file system to image file system
COPY . /app

#Install necessary packages 
RUN apt-get update && apt-get install -y python3 python3-pip

#Set Environment Variable
ENV NAME world

#Run Command to start application
CMD [ "python3" , "ex1.py"]