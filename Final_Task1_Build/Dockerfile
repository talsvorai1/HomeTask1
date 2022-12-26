FROM python:3.8-alpine
#Create and deside working directory
RUN mkdir /home/hello
WORKDIR /home/hello
#First installing requirements to save time and effort
COPY /requirements.txt /home/hello/
RUN pip3 install -r ./requirements.txt
#Copying relevant files for app to run
COPY /app.py /home/hello/
COPY /templates/index.html /home/hello/templates/
#Deploying it in localhost port 443
CMD ["gunicorn", "--bind", "0.0.0.0:443", "app:app"]
