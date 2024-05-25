FROM python:3.10.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
RUN python manage.py migrate
RUN python manage.py loaddata fixture.json

CMD python manage.py runserver 0.0.0.0:8000 --noreload