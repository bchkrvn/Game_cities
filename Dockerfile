FROM python:3.9

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /HW_26

CMD flask --app /HW_26/app.py run -h 0.0.0.0 -p 80