FROM python:3.8-alpine

RUN mkdir /home/hello
WORKDIR /home/hello

COPY /requirements.txt /home/hello/
RUN pip3 install -r ./requirements.txt

COPY /app.py /home/hello/
COPY /templates/index.html /home/hello/templates/

CMD ["gunicorn", "--bind", "0.0.0.0:443", "app:app"]
