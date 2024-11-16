FROM python:3.13-slim-bookworm

WORKDIR /j-awth

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=Dauth.settings

ENV PYTHONUNBUFFERED=1

CMD ["python" , "manage.py" , "runserver" , "0.0.0.0:8000"]

