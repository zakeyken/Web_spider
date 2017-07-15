FROM django:latest

RUN apt-get update;\
    apt-get install mysql-server;\
    true
RUN pip install requests;\
    true
RUN mkdir /root/notifier
WORKDIR /root/notifier

