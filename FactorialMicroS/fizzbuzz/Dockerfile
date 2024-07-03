FROM python:3.8

RUN apt update

RUN apt install python3-pip -y

RUN mkdir /opt/fizzbuzz

COPY . /opt/fizzbuzz

WORKDIR /opt/fizzbuzz

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]