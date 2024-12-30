FROM python:2.7
CMD ['mkdir','/dec30']
COPY ./flaskapp.py /dec30
CMD ['python','/dec30/flaskapp.py'] 
