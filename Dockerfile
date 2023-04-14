FROM python:3.9

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD gunicorn app:app -b 0.0.0.0:80