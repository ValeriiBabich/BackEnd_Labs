FROM python:3.10.6

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD export FLASK_APP=__init__
CMD flask run
