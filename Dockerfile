FROM python:3.9

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /HW_26

CMD python3 -m gunicorn /HW_26/app:app -b 0.0.0.0:80 -w 1 --threads 4