FROM python:3.10-alpine

WORKDIR ./app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
