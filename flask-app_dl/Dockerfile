FROM centos:latest

LABEL "Maintainer"="Muhammad Tabish Khanday"
LABEL "Email"="mtabishkhanday@gmail.com"

RUN dnf install python3 -y
RUN dnf install python3-devel -y
RUN mkdir /deep-learning-app 
WORKDIR /deep-learning-app

RUN pip3 install --upgrade pip
RUN pip3 install tensorflow==2.4.1
RUN  pip3 install keras==2.4.3
RUN pip3 install flask
RUN pip3 install jsonify==0.5

ADD  . /deep-learning-app/ 

CMD ["python3", "app.py"]

EXPOSE 8080
