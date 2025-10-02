FROM python:3.11-alpine3.16

WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
EXPOSE 8000

RUN pip3 install -r requirements.txt

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]